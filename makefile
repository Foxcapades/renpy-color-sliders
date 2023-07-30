VERSION := $(shell grep 'define config.version' game/options.rpy | sed 's/.\+"\(.\+\)"/\1/')
FEATURE := $(shell grep 'define config.version' game/options.rpy | sed 's/.\+"\(.\+\)"/\1/;s/\([0-9]\+\.[0-9]\+\).\+/\1.0/')

BUILD_DIR := .build

SLIM_ZIP_NAME := $(BUILD_DIR)/cs-slim-$(VERSION).zip
FULL_ZIP_NAME := $(BUILD_DIR)/cs-project-$(VERSION).zip

.PHONY: default
default:
	@echo "What are you doing?"


.PHONY: clean
clean:
	@echo "Cleaning directory."
	@find . -name '*.rpyc' -o -name '*.rpyb' -o -name '*.rpymc' | xargs -I'{}' rm '{}'


.PHONY: release
release: pre-release build-base-project-zip build-slim-zip build-distributions


.PHONY: pre-release
pre-release: clean
	@rm -rf $(BUILD_DIR)


.PHONY: build-base-project-zip
build-base-project-zip: clean
	@mkdir -p $(BUILD_DIR)
	@rm -f "$(FULL_ZIP_NAME)"
	@cp license color-picker-license
	@zip -r "$(FULL_ZIP_NAME)" game color-picker-license -x game/saves/**\* -x game/cache/**\*
	@rm color-picker-license


.PHONY: build-slim-zip
build-slim-zip: clean
	@mkdir -p $(BUILD_DIR)
	@rm -f "$(SLIM_ZIP_NAME)"
	@cp license color-picker-license
	@zip -r "$(SLIM_ZIP_NAME)" game/lib/fxcpds/color_picker color-picker-license
	@rm color-picker-license


.PHONY: build-distributions
build-distributions: clean
	@mkdir -p $(BUILD_DIR)
	@renpy-8.1.1 /opt/renpy/8.1.1/launcher distribute . --package=pc --dest=$(BUILD_DIR)
	@renpy-8.1.1 /opt/renpy/8.1.1/launcher distribute . --package=mac --dest=$(BUILD_DIR)
	@renpy-8.1.1 /opt/renpy/8.1.1/launcher distribute . --package=linux --dest=$(BUILD_DIR)


.PHONY: docs
docs:
	@mkdir -p docs/versions/$(FEATURE)
	@asciidoctor -b html5 -o docs/index.html -a revnumber=$(FEATURE) docs/index.adoc
	@asciidoctor -b html5 -o docs/versions/$(FEATURE)/index.html -a revnumber=$(FEATURE) docs/reference/index.adoc
	@asciidoctor -b html5 -o docs/versions/$(FEATURE)/tutorial.html -a revnumber=$(FEATURE) docs/reference/tutorial.adoc