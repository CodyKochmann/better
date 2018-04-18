# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2018-02-28 14:11:34
# @Last Modified 2018-03-02
# @Last Modified time: 2018-04-18 09:54:23

'''
Python builtins, just better
'''

from __future__ import print_function
del print_function

from functools import wraps

_print = print
_dict = dict

@wraps(_print)
def print(*a, **k):
    ''' like print, except this actually returns the value '''
    _print(*a, **k)
    return a if len(a)>1 else a[0]


class dict(_dict):
    ''' like dict, just with tiny improvements '''
    def update(self, *a, **k):
        ''' dict.update that actually returns the object so you can inline it '''
        _dict.update(self, *a, **k)
        return self

''' # this is for automation of this library later
def return_self_if_none(fn):
    @wraps(fn)
    def wrapper(self, *a, **k):
        if isinstance(self, NoneType):
            return fn(*a, **k)
        else:
            out = fn(*a, **k)
            return self if out is None else out

for a in dir(dict):
    att = getattr(dict, a)
    if callable(att) and a not in {'__class__','__init__','__getattr__'}:
        setattr(dict, a, return_self_if_none(att))
'''

if __name__ == '__main__':
    import sys
    p = lambda i:sys.stdout.write('{}\n'.format(i))

    p(print(5))

    print(print(dict(hi=5).update({6:10})).update({10:1}))
