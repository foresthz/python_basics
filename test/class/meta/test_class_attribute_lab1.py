'''
Created on 2018-10-19

@author: steven
'''

from clz.meta.class_meta1 import ClassFieldLab

meta1 = ClassFieldLab()
# instance attribute can be accessed even when it has not been defined, if there is a class attribute which have the same name
# as current instance attribute name, it's default value is the same as class attribute. this instance name is the same as class attribute
# but they are different values. 
print ('instance attribute of meta1 class_count 1 : ',meta1.class_count, 'this is default value')
# not class attribute, this is instance attribute
meta1.class_count = 101
print ('instance attribute of meta1 class_count 1 : ',meta1.class_count)


ClassFieldLab.class_count = 111
print('class __class__ : \n\t', ClassFieldLab.__dict__)

meta2 = ClassFieldLab()
meta2.name = 'define_var_by_assignment'
print ('instance attribute class_count 2(after class attribute is changed) : ',meta2.class_count)
print ('class attribute class_count 2 : ',ClassFieldLab.class_count)
ClassFieldLab.class_count = 222
print ('instance attribute class_count 2(class attribute changed the second time) : ',meta2.class_count)

meta3 = ClassFieldLab()
meta3.class_count = 1000
print('class attribute ClassFieldLab.class_count: ClassFieldLab.class_count', ClassFieldLab.class_count)
print('meta3 __dict__: ', meta3.__dict__)

print('class __class__ : \n\t', ClassFieldLab.__dict__)
print('meta1 instance __class__ : \n\t', meta1.__dict__)
print(meta1.class_count, ClassFieldLab.class_count)
print('meta2 instance __class__ : \n\t', meta2.__dict__)