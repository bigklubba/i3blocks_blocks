#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from lxml import html
# import urllib.request
# import lxml.html
STOCK_PAGE = "http://www.di.se/stockwatch/net-insight/overview/"
STOCK_NAME = "NETI"
STOCK_UP = ""
STOCK_DOWN = ""
STOCK_STALE = ""
STOCK_COLOR_UP = "#A8FF00"
STOCK_COLOR_DOWN = "#FF0000"
STOCK_COLOR_STALE = "#A8ff00"
X_STR = '//table[@class="fh-table-simple-decorate"]/tr/td/text()'


def get_latest_stock_value():
    """docstring for get_stock_page"""
    response = request.urlopen(STOCK_PAGE)

    content = response.read()
    tree = html.fromstring(content)
    stock_table = tree.xpath(X_STR)
    return [stock_table[2], stock_table[1]]


def transform_to_float(string_float):
    """docstring for transform_to_float"""
    pos = string_float.index(',')
    if pos < 0:
        return float(string_float)
    else:
        return float(string_float[:pos]+'.'+string_float[pos+1:])


def main():
    """docstring for main"""
    stock_values = get_latest_stock_value()
    latest_value = stock_values[0]
    diff = stock_values[1]
    full_text = latest_value+'('+diff+')'
    short_text = full_text

    if transform_to_float(diff) < 0:
        color = STOCK_COLOR_DOWN
        progression = STOCK_DOWN
    elif transform_to_float(diff) > 0:
        color = STOCK_COLOR_UP
        progression = STOCK_UP
    else:
        color = STOCK_COLOR_STALE
        progression = STOCK_STALE

    full_text = latest_value+'('+diff+')'
    short_text = latest_value+progression

    print(full_text)
    print(short_text)
    print(color)


if __name__ == '__main__':
    main()
