#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

f = os.popen("bluetoothctl info | grep Connected")
now = f.read()
if 'yes' in now:
    os.popen("amixer -q -D pulse sset Master unmute")
    color = "#42bff4"
else:
    os.popen("amixer -q -D pulse sset Master mute")
    color = "#FF0000"
print('')
print('')
print(color)
