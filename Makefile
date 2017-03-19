.PHONY: help
help:
	@echo "merge          merge overwrite.txt"
	@echo "er             find r"

.PHONY: merge
merge:
	python merge.py > new.txt && mv new.txt pinyin.txt

.PHONY: er
er:
	cat overwrite.txt|grep 儿|grep -v ér|grep -v er
