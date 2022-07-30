# phrase-pinyin-data [![Build Status](https://travis-ci.org/mozillazg/phrase-pinyin-data.svg?branch=master)](https://travis-ci.org/mozillazg/phrase-pinyin-data)

词语拼音数据。


## 数据介绍

拼音数据的格式：

```
{phrase}: {pinyin}
```

* 以 `#` 开头的行是注释
* 行尾的 `#` 也是注释
* `{phrase}` 汉字词语
* `{pinyin}` 词语的拼音，使用空格分隔每个汉字的拼音
* 一行一个词语的读音，有多个音的词语会出现在多行
* 示例：

  ```
  # 注释
  中国: zhōng guó
  北京: běi jīng  # 注释
  ```

文件说明:

* `overwrite.txt`: 手工纠正的拼音数据
* `pinyin.txt`: `pinyin.txt + overwrite.txt` 后的拼音数据
* `zdic_cibs.txt`: [汉典网](http://www.zdic.net/) 汉语词典拼音数据
* `zdic_cybs.txt`: [汉典网](http://www.zdic.net/) 成语词典拼音数据
* `cc_cedict.txt`: [cc-cedict.org](https://cc-cedict.org/) 拼音数据
<!-- * `espeak_zh_listx.txt`: [espeak](http://espeak.sourceforge.net/data/) 中 `zh_listx.zip` 中包含的部分词语发音 -->
<!-- * `large_pinyin.txt`: `zdic_cibs.txt + zdic_cybs.txt + cc_cedict.txt + pinyin.txt + espeak_zh_listx.txt + overwrite.txt` 后的拼音数据 -->
* `di.txt`: 纠正部分短语中 `地` 的拼音 (可以直接修改)
* `large_pinyin.txt`: `zdic_cibs.txt + zdic_cybs.txt + cc_cedict.txt + pinyin.txt + di.txt + overwrite.txt` 后的拼音数据

## 修改数据

* 修改 `pinyin.txt` 或 `overwrite.txt` 都可以了
* 执行 `make merge` 命令可以按照合并规则生成最新的 `pinyin.txt` 和 `large_pinyin.txt`


## 参考资料

* 初始数据基于 [phrases-dict.js](https://github.com/hotoo/pinyin/blob/05f74496c34ccb32db1a0fd0b358a798a22a51e5/data/phrases-dict.js) 和 [phrases\_dict.py](https://github.com/mozillazg/python-pinyin/blob/366de0363ff1fb9a718ce668448bea59de09a4bf/pypinyin/phrases_dict.py)
* [汉典 zdic.net](http://www.zdic.net/)
* [字海网，叶典网](http://zisea.com/)
* [国学大师国学网](http://www.guoxuedashi.com/)
* [CC-CEDICT download - MDBG English to Chinese dictionary](http://www.mdbg.net/chindict/chindict.php?page=cc-cedict)
* [漢語大詞典](http://www.ivantsoi.com/hydcd/search.html)


## 相关项目

* [mozillazg/pinyin-data](https://github.com/mozillazg/pinyin-data): 汉字拼音数据
* [mozillazg/python-pinyin](https://github.com/mozillazg/python-pinyin): 汉字转拼音(pypinyin)
* [mozillazg/pypinyin-dict](https://github.com/mozillazg/pypinyin-dict): 在 pypinyin 项目中使用 phrase-pinyin-data 里不同数据文件里的数据
