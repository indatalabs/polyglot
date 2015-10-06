# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals
import math

def long_text_weighting(words_between, words_total):
    return 1.0 - words_between / (2.0 * words_total)

def short_text_weighting(words_between, words_total):
    return 1.0 / math.exp(words_between / math.sqrt(words_total))