'''
Created on 2018-10-19

@author: steven
'''


class ClassMeta(object):
    pass


class ClassFieldLab(object):
    class_count = 1000
    # class attribute must have a default value
    #class_var
    def __init__(self):
        self.internal_count = 0
    def get_class_count(self):
        return ClassFieldLab.class_count
    def get_internal_count(self):
        return self.internal_count

class ClassInstanceLab(object):
    def __init__(self):
        self.hello
    def setName(self):
        pass
