ARTICLES := $(wildcard articles/*.md)
PAGES := $(patsubst articles/%.md,_site/articles/%.html,$(ARTICLES))
PANDOC := pandoc --standalone --from=markdown --to=html5 --syntax-highlighting=none --strip-comments --wrap=none --template=site/article-template.html
ARTICLE_LANG ?= en

.PHONY: build check clean doctor index new pandoc-check preview serve

build: pandoc-check _site/style.css $(PAGES) index

check: doctor
	@python3 scripts/check_articles.py
	@python3 scripts/check_skills.py
	@$(MAKE) --no-print-directory build
	@python3 site/check_site.py

doctor:
	@command -v python3 >/dev/null 2>&1 || { echo "error: python3 is required"; exit 1; }
	@command -v pandoc >/dev/null 2>&1 || { echo "error: pandoc is required (https://pandoc.org/installing.html)"; exit 1; }
	@python3 --version
	@pandoc --version | sed -n '1p'
	@echo "local toolchain ok"

new:
	@python3 scripts/new_article.py --slug "$(SLUG)" --title "$(TITLE)" --lang "$(ARTICLE_LANG)"

preview: pandoc-check _site/style.css
	@[ -n "$(FILE)" ] || { echo "usage: make preview FILE=drafts/example.md"; exit 1; }
	@[ -f "$(FILE)" ] || { echo "error: $(FILE) does not exist"; exit 1; }
	@mkdir -p _site/articles
	@$(PANDOC) --output=_site/articles/preview.html "$(FILE)"
	@echo "wrote _site/articles/preview.html"

pandoc-check:
	@if [ -n "$(strip $(ARTICLES))$(FILE)" ] && ! command -v pandoc >/dev/null 2>&1; then \
		echo "error: pandoc is required for article rendering (https://pandoc.org/installing.html)"; \
		exit 1; \
	fi

_site _site/articles:
	@mkdir -p $@

_site/style.css: site/style.css | _site
	@cp $< $@

_site/articles/%.html: articles/%.md site/article-template.html | _site/articles
	@$(PANDOC) --output=$@ $<

index: | _site
	@python3 site/build_index.py

serve: build
	@echo "serving http://localhost:8000/"
	@cd _site && python3 -m http.server 8000

clean:
	@rm -rf _site
