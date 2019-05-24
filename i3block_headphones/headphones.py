#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

f = os.popen("bluetoothctl info | grep Connected")
now = f.read()
if 'yes' in now:
    color = "#42bff4"
else:
    color = "#FF0000"
print('')
print('')
print(color)
