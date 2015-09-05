#!/usr/bin/env python2
# -*- coding: utf-8 -*- 

from os import path
from chinese_cloud.chinese_cloud import ChineseCloud


text_dir = path.dirname(__file__)
text = open(path.join(text_dir, 'TopLabel.txt')).read()
chinese_cloud = ChineseCloud(width=800, height=400, max_font=100, min_font=10).generate(text).to_image('TopLabel3.png')
