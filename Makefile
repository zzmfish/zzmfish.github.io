
MKD_FILES=$(shell ls markdown/*.md)
HTML_FILES=$(foreach path, $(MKD_FILES:.md=.html), $(shell basename $(path)))

TARGET: $(HTML_FILES) index

%.html: markdown/%.md
	./tools/make_html $< > $@

index:
	./tools/make_index > index.md
	./tools/make_html index.md > index.html
	rm index.md

clean:
	rm -f $(HTML_FILES) index.html
