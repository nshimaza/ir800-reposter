# Copyright (c) 2019 Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.1 (the "License"). You may obtain a copy of the
# License at
#
#                https://developer.cisco.com/docs/licenses
#
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

import bottle
import ConfigParser
import datetime
import httplib
import json
import os
import requests
import sys

config_file = os.path.abspath(os.getenv('CAF_APP_CONFIG_FILE'))
config = ConfigParser.ConfigParser()
config.read(config_file)
dest = config.get('destination', 'url')

@bottle.route('/')
def hello():
    return "Hello Python runs on IOx!  Now it is " + str(datetime.datetime.utcnow())

@bottle.post('/')
def log_post():
    requests.post(dest, json = { 'timestamp': str(datetime.datetime.utcnow()), 'value': bottle.request.body.getvalue() })
    bottle.response.status = httplib.NO_CONTENT
    return ('')

bottle.run(host='0.0.0.0', port=8080, debug=True)
