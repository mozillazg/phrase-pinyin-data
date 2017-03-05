.PHONY: help
help:
	@echo "merge          merge overwrite.txt"

.PHONY: merge
merge:
	python merge.py > new.txt && mv new.txt pinyin.txt
