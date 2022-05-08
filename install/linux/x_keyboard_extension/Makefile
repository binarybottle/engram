TARGET_SYM := /usr/share/X11/xkb/symbols/us
SOURCE_SYM := usr-share-X11-xkb-symbols-us
TARGET_RULE := /usr/share/X11/xkb/rules/evdev.xml
SOURCE_RULE := usr-share-X11-xkb-rules-evdev

all: reinstall

install: $(SOURCE_SYM) $(TARGET_SYM) $(SOURCE_RULE) $(TARGET_RULE)
	echo '//ENGRAM//BEGIN' >> $(TARGET_SYM)
	cat $(SOURCE_SYM) >> $(TARGET_SYM)
	echo '//ENGRAM//END' >> $(TARGET_SYM)
	sed -i "$$(awk '/variantList/ {print NR; exit}' $(TARGET_RULE)) r $(SOURCE_RULE)" $(TARGET_RULE)

uninstall: $(TARGET_SYM) $(TARGET_RULE)
	sed -i '/^\/\/ENGRAM\/\/BEGIN$$/,/^\/\/ENGRAM\/\/END$$/d' $(TARGET_SYM)
	sed -i '/ENGRAM BEGIN/,/ENGRAM END/d' $(TARGET_RULE)

reinstall:
	$(MAKE) uninstall
	$(MAKE) install

.PHONY: all install uninstall reinstall
