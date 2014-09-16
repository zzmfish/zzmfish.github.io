
MKD_FILES=$(shell ls markdown/*.mkd)
HTML_FILES=$(foreach path, $(MKD_FILES:.mkd=.html), $(shell basename $(path)))

TARGET: $(HTML_FILES) index

%.html: markdown/%.mkd
	./tools/make_html $< > $@

index:
	./tools/make_index > index.mkd
	./tools/make_html index.mkd > index.html
	rm index.mkd

clean:
	rm -f $(HTML_FILES) index.html
