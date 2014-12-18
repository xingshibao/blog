#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
annotation
"""

__author__ = 'shibao.xing'

try:
    import cPickle as pickle
except:
    import pickle

import json

d = dict(name = 'Eric', age = 24)
print json.dumps(d)


f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
 
f = open('dump.txt', 'rb')
dd = pickle.load(f)
f.close()
