# -*- coding: utf-8 -*-
import sys


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


def diff(overwrite_d, origin_d):
    o_k = set(origin_d.keys())
    v_k = set(overwrite_d.keys())
    for k in (o_k & v_k):
        o_v = origin_d[k]
        v_v = overwrite_d[k]
        if o_v != v_v:
            print('{k} ? o_v: {o_v!r} => v_v: {v_v!r}'.format(
                  k=k, o_v=o_v, v_v=v_v), file=sys.stderr)


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
    print('# version: 0.4.1')
    print('# source: https://github.com/mozillazg/phrase-pinyin-data')
    for hanzi, pinyin in pinyin_s:
        print('{hanzi}: {pinyin}'.format(hanzi=hanzi, pinyin=pinyin))


def main():
    with open('overwrite.txt') as fp:
        overwrite_d = dict(parse(fp))
    with open('pinyin.txt') as fp:
        origin_d = dict(parse(fp))

    diff(overwrite_d, origin_d)
    pinyin_d = merge(overwrite_d, origin_d)
    output(sort(pinyin_d))


if __name__ == '__main__':
    main()
