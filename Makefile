
MKD_FILES=$(shell ls *.mkd | grep -v index.mkd)
HTML_FILES=$(MKD_FILES:.mkd=.html)

TARGET: $(HTML_FILES) index.html

%.html: %.mkd
	./mkd2html $< > $@

index.mkd: $(HTML_FILES)
	./make_index > $@

clean:
	rm -f $(HTML_FILES) index.html index.mkd
