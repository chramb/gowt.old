PYTHON ?= $(shell command -v python)
MAKEFILE =$(abspath $(lastword $(MAKEFILE_LIST)))

.PHONY: doc man test format run help clean

# Usage:
# 	make [rule]
# rules:
#

# 	help	- print this help message
help:
	@grep '\# ' $(MAKEFILE) | grep -v \@  | sed -e 's:# ::'

# 	run	- run gowt directly, pass arguments through RUNCMD variable
# 		    e.g.: make run RUNCMD="--gentoo $GENTOO_REPO --repo $OVERLAY"
run:
	@$(PYTHON) -m gowt $(RUNCMD)

# 	test	- run all tests
test: unit lint type

#TODO
unit:
# 	lint	- run linters (black, flake8)
lint:
	@echo == black ==
	@black --check gowt/
	@echo
	@echo == flake8 ==
	@flake8 -v gowt/
	@echo

#	type	- run mymy - type checker
type:
	@echo == mypy ==
	@mypy -m gowt
