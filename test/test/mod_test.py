'''
Created on 2018-10-18

@author: steven
'''

import mod
from mod import mod1

print ('mod: ', mod)
print ('mod.mod1: ', mod.mod1)
print ('mod.mod1.Mod1: ', mod.mod1.Mod1)


from mod.mod2 import Animal, Cat, Dog, HuntAway

animal = Animal()

cat = Cat()
dog = Dog()

huntaway = HuntAway()

