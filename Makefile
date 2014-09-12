
MKD_FILES=$(shell ls *.mkd)
HTML_FILES=$(MKD_FILES:.mkd=.html)

TARGET: $(HTML_FILES)

%.html: %.mkd
	./markdown $< > $@

clean:
	rm $(HTML_FILES)
