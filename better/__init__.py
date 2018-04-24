# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2018-02-28 14:11:34
# @Last Modified 2018-03-02
# @Last Modified time: 2018-04-24 10:07:46

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

class defaultdict(dict):
    ''' this works a lot like collections.defaultdict, except instead of the default
        needing to be a class, you can hand it a function to call each time it
        needs to load a new default or simply some variable youd prefer as the default

        examples:

            # just like before, this creates a bool when a key is missing
            defaultdict(bool)

            # 5 is the default value for missing keys
            defaultdict(5)

            # runs garbage collection and returns 'hello' when a key is missing
            defaultdict(
                lambda:[gc.collect(1), 'hello'][1]
            )
    '''
    def __init__(self, constructor):
        if not callable(constructor):
            constructor = lambda o=constructor: o
        self._constructor = constructor

    def __getitem__(self, target):
        if target in self:
            return dict.__getitem__(self, target)
        else:
            dict.__setitem__(self, target, self._constructor())
            return dict.__getitem__(self, target)

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

    print(print(5))

    print(print(dict(hi=5).update({6:10})).update({10:1}))

    bool_default = defaultdict(bool)
    print('hi' in bool_default)
    print(bool_default['hi'])
    print(bool_default['hi'])
    print('hi' in bool_default)

    five_default = defaultdict(5)
    print('hi' in five_default)
    print(five_default['hi'])
    print(five_default['hi'])
    print('hi' in five_default)


    print_yay_default = defaultdict(lambda:[print('yay'),10][1])
    print('hi' in print_yay_default)
    print(print_yay_default['hi'])
    print(print_yay_default['hi'])
    print('hi' in print_yay_default)

