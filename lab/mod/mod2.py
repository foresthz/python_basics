'''
Created on 2018-10-18

@author: steven
'''


class Animal(object):
    def __init__(self):
        print('init from animal ..')
    def sayHello(self, name='default_name'):
        print('hello from Animal ..', name)

class Cat(Animal):
    def __init__(self):
        print('init Cat ..')

class Dog(Animal):
    def __init__(self):
        print('init Dog ...')
        super().__init__()
        super().sayHello()
        print('init Dog ... finished')
        
class DogX(Cat, Dog):
    pass
        
class HuntAway(Dog):
    def __init__(self):
        print('init HuntAway ..')
        print('m1: ')
        m1 = super(Dog, self)
        print(m1)
        m1.sayHello()
        print("m2: ")
        m2 = super(HuntAway, self)
        print(m2)
        m2.sayHello('m2#HuntAway')
        print("m3: ")
        m3 = super(Dog, self)
        # parent class of Animal does not have a method named sayHello
#         m3 = super(Animal, self)
        print(m3)
        m3.sayHello('m3#')
