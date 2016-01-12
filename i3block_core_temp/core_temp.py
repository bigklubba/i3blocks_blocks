#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

f = os.popen("sensors | grep Core | awk '{printf $3}'")
now = f.read()
# only print the core with the highest temperature
max_temp = 0.0
for temp in filter(None, now.split('°C')):
    core_temp = float(temp)
    if core_temp > max_temp:
        max_temp = core_temp
if max_temp < 60.0:
    color = "#A8FF00"
elif max_temp < 70:
    color = "#FF8000"
else:
    color = "#FF0000"
max_temp = str(max_temp)+'°C'
print max_temp 
print max_temp 
print color
