#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。'

__author__ = 'Drake-Z'

import re

def tongji(file_path):
    f = open(file_path, 'r').read()
    f = re.split(r'[\s\,\;,\n]+', f)
    print(len(f))
    return 0

if __name__ == '__main__':
    file_path = 'English.txt'
    tongji(file_path)