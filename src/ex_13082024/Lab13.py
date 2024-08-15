#NONE TYPE

#NO NULL CONCEPT IN PYTHON
how_many_planes_i_have = None
print(type(how_many_planes_i_have))

#outputs <class 'NoneType'>
#id returns the address of the variable where it is  stored
age = 10
age2 = 10
print(id(age))#140724289018584
print(id(age2)) #id of object ,140724289018584
#to save the memory age2 points to the same address as that of age

age = 17
age2 = 20
print(id(age))#140724289018808
print(id(age2))#140724289018904

