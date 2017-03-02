#!/usr/bin/env python3
# -*- coding: utf-8 -*-
BAT_LEVEL = "/sys/class/power_supply/BAT0/capacity"
BAT_CHARGING = "/sys/class/power_supply/BAT0/status"
URGENT_LOWER = 15
URGENT_HIGHER = 30
DISCHARGING = 'Discharging'

ICON_CHARGING = ""
ICON_DISCHARGING = ""
ICON_BATTERY = ["", "", "", "", ""]


def getBatteryIcon(bat_level):
    index = min(len(ICON_BATTERY)-1, bat_level//(100//len(ICON_BATTERY)))
    return ICON_BATTERY[index]


def isCharging():
    status_file = open(BAT_CHARGING, "r")
    current_status = status_file.read()
    return DISCHARGING not in current_status


def test_values():
    for i in range(0, 100):
        print("%i %s" % (i, getBatteryIcon(i)))


def main():
    bat_level_file = open(BAT_LEVEL, "r")
    bat_level = int(bat_level_file.read())
    icon = ICON_DISCHARGING
    if isCharging():
        icon = ICON_CHARGING
    print("%s %s" % (icon, getBatteryIcon(bat_level)))
    print("%s %s" % (icon, getBatteryIcon(bat_level)))
    if bat_level < URGENT_LOWER:
        """ Make sure we get urgent notification to the i3bar """
        exit(33)
if __name__ == '__main__':
    main()
