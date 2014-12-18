#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
simple orm frame
"""

__author__ = 'shibao.xing'

from _pyio import __metaclass__

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
        

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        
        print 'Found Model : %s' % name
        mappings = dict()
        
        for k, v in attrs.iteritems():
            print 'Found mapping %s ==> %s' % (k, v)
            if isinstance(v, Field):
                mappings[k] = v
        
        for k in mappings.keys():
            attrs.pop(k)
        
        attrs['__table__'] = name    
        attrs['__mappings__'] = mappings
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass
    
    def __init(self, **kw):
        super(Model, self).__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
        
    def __setattr__(self, key, value):
        self[key] = value
        
    def save(self):
        keys = []
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            keys.append(k)
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL : %s' % sql)
        print('ARGS : %s' % str(args)) 
        print keys

class User(Model):
    uid = IntegerField('uid')
    username = StringField('username')
    password = StringField('password')
    
user = User(uid = 1, username = 'eric', password = 'password')
user.save()





    
