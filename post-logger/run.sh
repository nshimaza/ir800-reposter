#!/bin/sh
if ! [ -e bottle.py ]; then
	curl -O https://raw.githubusercontent.com/bottlepy/bottle/0.12.17/bottle.py
fi
python post-logger.py $@
