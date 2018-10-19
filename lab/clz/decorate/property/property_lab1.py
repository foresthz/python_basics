'''
Created on 2018-10-19

@author: steven
'''

class PropertyManagerLab1(object):
    def __init__(self):
        self.count = 0
        pass
    
    @property
    # this parameter could not be invoked?
    def hello(self, name='world'):
        return 'hello %s' % name

