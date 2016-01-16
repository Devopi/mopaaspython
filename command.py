#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests, base64

while True:
    str = raw_input('>>> ')
    str = base64.b64encode(str)
    r = requests.get('http://pythont.carp.mopaasapp.com/run/'+str)
    print r.text
