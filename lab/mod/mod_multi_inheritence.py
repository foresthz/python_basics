'''
Created on 2018-10-19

@author: steven
'''


class StoreFacade(object):
    a=11
    def store(self):
        print('store facade')
        pass

class ComputeFacade(object):
#     @property
    def compute(self):
        print('compute facade')
        pass

class Facade(StoreFacade, ComputeFacade):
    def __init__(self):
        pass
    

