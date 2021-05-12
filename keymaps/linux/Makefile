TARGET := /usr/share/X11/xkb/symbols/us
SOURCE := usr-share-X11-xkb-symbols-us

all: reinstall

install: $(SOURCE) $(TARGET)
	echo '//ENGRAM//BEGIN' >> $(TARGET)
	cat $(SOURCE) >> $(TARGET)
	echo '//ENGRAM//END' >> $(TARGET)

uninstall: $(TARGET)
	sed -i '/^\/\/ENGRAM\/\/BEGIN$$/,/^\/\/ENGRAM\/\/END$$/d' $<

reinstall:
	$(MAKE) uninstall
	$(MAKE) install

.PHONY: all install uninstall reinstall
