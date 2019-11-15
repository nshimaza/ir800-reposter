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
import datetime
import httplib
import os
import sys

@bottle.route('/')
def hello():
    return "Hello Python runs on IOx!  Now it is " + str(datetime.datetime.utcnow())

@bottle.post('/')
def log_post():
    with open('posted.log', 'a') as l:
        l.write(str(datetime.datetime.utcnow()) + ' ' + bottle.request.body.getvalue() + '\n')
    bottle.response.status = httplib.NO_CONTENT
    return ('')

bottle.run(host='0.0.0.0', port=8081, debug=True)
