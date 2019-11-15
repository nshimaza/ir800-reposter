#!/bin/sh
if ! [ -e bottle.py ]; then
	curl -O https://raw.githubusercontent.com/bottlepy/bottle/0.12.17/bottle.py
fi
CAF_APP_CONFIG_FILE=package_config.ini python reposter.py $@
