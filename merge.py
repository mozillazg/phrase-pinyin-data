# -*- coding: utf-8 -*-


def parse(lines):
    """
    :yield: hanzi, others
    """
    for line in lines:
        line = line.strip()
        if line.startswith('#') or not line:
            continue

        hanzi, others = line.split(':', 1)
        yield hanzi.strip(), others.strip()


def merge(overwrite_d, origin_d):
    """
    :rtype: dict
    """
    origin_d.update(overwrite_d)
    return origin_d


def sort(pinyin_d):
    """
    :rtype: list
    """
    return sorted(pinyin_d.items(), key=lambda x: x[0])


def output(pinyin_s):
    print('# version: 0.2.0')
    print('# source: https://github.com/mozillazg/phrase-pinyin-data')
    for hanzi, pinyin in pinyin_s:
        print('{hanzi}: {pinyin}'.format(hanzi=hanzi, pinyin=pinyin))


def main():
    with open('overwrite.txt') as fp:
        overwrite_d = dict(parse(fp))
    with open('pinyin.txt') as fp:
        origin_d = dict(parse(fp))

    pinyin_d = merge(overwrite_d, origin_d)
    output(sort(pinyin_d))


if __name__ == '__main__':
    main()
