#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

f = os.system('xset -q | grep "Caps Lock: *on" 1>/dev/null')
if f == 0:
  status = "on"
  color = "#FF0000"
else:
  status = "off"
  color = "#A8FF00"
print(status)
print(status)
print(color)
