#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
from lxml import html
STOCK_PAGE = "http://www.di.se/stockwatch/net-insight/overview/"
STOCK_NAME = "NETI"

def get_latest_stock_value():
    """docstring for get_stock_page"""
    response = urllib2.urlopen(STOCK_PAGE)
    content = response.read()
    tree = html.fromstring(content) 
    stock_table = tree.xpath('//table[@class="fh-table-simple-decorate"]/tr/td/text()')
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
        color = "#FF0000"
    else:
        color = "#A8FF00"
    print full_text
    print short_text
    print color 


if __name__ == '__main__':
    main()
