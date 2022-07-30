import re
import sys

"""检查不在 pinyin-data/pinyin.txt 中的拼音"""


def get_all_pinyin(fp):
    pinyins = set()
    for line in fp:
        line = line.strip()
        if line.startswith('#') or not line:
            continue
        _, pinyin = line.split('#')[0].split(':')
        pinyin = ','.join([x.strip() for x in pinyin.split() if x.strip()])

        pinyins.update(pinyin.split(','))
    return pinyins


def parse_ph(fp):
    for line in fp:
        line = line.strip()
        if line.startswith('#') or not line:
            continue
        han, pinyin = line.split('#')[0].split(':')

        pinyin = [x.strip() for x in pinyin.split() if x.strip()]
        yield han, pinyin


def check_len(han, pinyin_list):
    return len(han) != len(pinyin_list)


def check_all_none(pinyin_list):
    return len([
        pinyin
        for pinyin in pinyin_list
        if re.match(r'^[a-z]+$', pinyin)
    ]) == len(pinyin_list)


def find():
    with open('./pinyin-data/pinyin.txt') as f:
        pinyin_set = get_all_pinyin(f)

    with open(sys.argv[1]) as fp:
        for han, pinyin in parse_ph(fp):

            diff = set(pinyin) - pinyin_set
            # 忽略轻声
            if not [x for x in diff if not re.match(r'^[a-z]+$', x)]:
                continue
            if diff and diff != set(['er']):
                print('{} {}'.format(han, ' '.join(diff)))

            if check_all_none(pinyin) or check_len(han, pinyin):
                print('{} {}'.format(han, ' '.join(pinyin)))


if __name__ == '__main__':
    find()
