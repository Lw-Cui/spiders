#!/usr/bin/env python2
# -*- coding: utf-8 -*- 

from os import path
import codecs
from chinese_cloud.chinese_cloud import ChineseCloud


text = codecs.open(path.join(path.dirname(__file__), 'topDirector.txt'), encoding='utf8').read()

def process(text):
    return [x for x in text.split('\n')]

chinese_cloud = ChineseCloud(width=1000, height=600, max_font=100, min_font=10, process=process).generate(text).to_image('topDirector.png')