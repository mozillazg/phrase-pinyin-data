# -*- coding: utf-8 -*-

import os
import time
import zipfile

import requests

ROOT = os.path.dirname(os.path.realpath(__file__))

DOWNLOAD_URL = 'https://cc-cedict.org/editor/editor_export_cedict.php?c=zip'
FALLBACK_DOWNLOAD_URL = (
    'https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip'
)
MAX_RETRIES = 5


def download(url, file_path):
    last_exc = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with requests.get(url, stream=True, timeout=(10, 120)) as response:
                response.raise_for_status()
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024 * 1024):
                        if chunk:
                            f.write(chunk)
            if not zipfile.is_zipfile(file_path):
                raise ValueError(f'{url} did not return a zip file')
            return
        except (requests.RequestException, OSError, ValueError) as e:
            last_exc = e
            if attempt < MAX_RETRIES:
                wait = attempt * 2
                print(f'Download failed (attempt {attempt}/{MAX_RETRIES}): {e}')
                print(f'Retrying in {wait} seconds...')
                time.sleep(wait)
    raise last_exc


if __name__ == '__main__':
    zip_file_path = os.path.join(ROOT, 'cc-cedict.zip')

    try:
        download(DOWNLOAD_URL, zip_file_path)
    except Exception as e:
        print(f'Failed to download {DOWNLOAD_URL}: {e}')
        print(f'Trying fallback URL: {FALLBACK_DOWNLOAD_URL}')
        download(FALLBACK_DOWNLOAD_URL, zip_file_path)

    with zipfile.ZipFile(zip_file_path) as z:
        z.extractall(ROOT)
