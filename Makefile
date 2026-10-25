PYTHON ?= python3
VENV ?= venv
VENV_PYTHON := $(VENV)/bin/python
REQUIREMENTS := tools/requirements_dev.txt

.PHONY: help
help:
	@echo "merge          update pinyin.txt and large_pinyin.txt"
	@echo "er             find r"
	@echo "check          check unexpected char"
	@echo "cedict_get     get latest cedict data"
	@echo "cedict         parse latest cedict data"
	@echo "deps           install the Python dependencies for cc-cedict tools"

$(VENV_PYTHON):
	$(PYTHON) -m venv $(VENV)

$(VENV)/.requirements-installed: $(REQUIREMENTS) | $(VENV_PYTHON)
	$(VENV_PYTHON) -m pip install -U -r $(REQUIREMENTS)
	@touch $@

.PHONY: deps
deps: $(VENV)/.requirements-installed

.PHONY: merge
merge:
	$(PYTHON) tools/merge.py pinyin.txt overwrite.txt > new.txt && mv new.txt pinyin.txt
	$(PYTHON) tools/merge.py zdic_cibs.txt zdic_cybs.txt cc_cedict.txt di.txt pinyin.txt overwrite.txt > new.txt && mv new.txt large_pinyin.txt

.PHONY: er
er:
	cat overwrite.txt|grep 儿|grep -v ér|grep -v er

.PHONY: tone_mark
tone_mark:
	ls *.txt | xargs -L 1 sed -i 's/ùo/uò/g'
	ls *.txt | xargs -L 1 sed -i 's/oǔ/ǒu/g'
	ls *.txt | xargs -L 1 sed -i 's/ùi/uì/g'
	ls *.txt | xargs -L 1 sed -i 's/íe/ié/g'
	ls *.txt | xargs -L 1 sed -i 's/ùi/uì/g'
	ls *.txt | xargs -L 1 sed -i 's/ǐe/iě/g'
	ls *.txt | xargs -L 1 sed -i 's/aō/āo/g'
	ls *.txt | xargs -L 1 sed -i 's/ìan/iàn/g'
	ls *.txt | xargs -L 1 sed -i 's/īan/iān/g'

.PHONY: check
check: tone_mark
	-rg 'ɡ|ɑ'

.PHONY: cedict_get
cedict_get: deps
	$(VENV_PYTHON) tools/get_latest_cc_cedict.py

.PHONY: cedict
cedict: cedict_get
	$(VENV_PYTHON) tools/parse_latest_cc_cedict.py
