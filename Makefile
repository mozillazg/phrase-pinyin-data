.PHONY: help
help:
	@echo "merge          update pinyin.txt and large_pinyin.txt"
	@echo "er             find r"
	@echo "check          check unexpected char"

.PHONY: merge
merge: check
	python merge.py pinyin.txt overwrite.txt > new.txt && mv new.txt pinyin.txt
	python merge.py zdic_cibs.txt zdic_cybs.txt pinyin.txt overwrite.txt > new.txt && mv new.txt large_pinyin.txt

.PHONY: er
er:
	cat overwrite.txt|grep 儿|grep -v ér|grep -v er

.PHONY: check
check:
	-rg 'ɡ|ɑ'
