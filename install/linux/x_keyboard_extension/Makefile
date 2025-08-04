XKB_BASE := /usr/share/X11/xkb
TARGET_SYM := $(XKB_BASE)/symbols/us
TARGET_RULE := $(XKB_BASE)/rules/evdev.xml
SOURCE_SYM := usr-share-X11-xkb-symbols-us
SOURCE_RULE := usr-share-X11-xkb-rules-evdev

all: reinstall

install: $(SOURCE_SYM) $(TARGET_SYM) $(SOURCE_RULE) $(TARGET_RULE)
	cat $(SOURCE_SYM) >> $(TARGET_SYM)
	sed -i '/English (US)/,/<variantList>/!b ; /<variantList>/r $(SOURCE_RULE)' $(TARGET_RULE)

uninstall: $(TARGET_SYM) $(TARGET_RULE)
	sed -i '/^\/\/ENGRAM BEGIN$$/,/^\/\/ENGRAM END$$/d' $(TARGET_SYM)
	sed -i '/ENGRAM BEGIN/,/ENGRAM END/d' $(TARGET_RULE)

reinstall:
	$(MAKE) uninstall
	$(MAKE) install

.PHONY: all install uninstall reinstall
