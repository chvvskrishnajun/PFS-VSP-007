'''
operators--->operators help us to perform operations between operands

arithmetic operators--->+,*,/,//(integer or floor division),
%(modules-->remainder)

assignmentm operators-->It helps to assign,update(increment),decrement
values
''''''
data=20
print(data)
print(type(data))

stock=data
print(stock)

#increment the values of stock
stock=stock+5
print(stock)
print(data)
#decrement the value of data by 2 values
data=data-2
print(data)

data=data*2
print(data)

data=data/2
print(data)

data=data//2
print(data)

data=data%2
print(data)

data=data**2
print(data)
''''''
stock=100
stock*=2
print(stock)'''
#comparision
#==,!=,<,<=,>,>=
'''
name='vinay'
vinay=attendence=75

print(vinay_attendance
print(vinay_attendance
print(vinay_attendance
print(vinay_attendance
print(vinay_attendance
print(vinay_attendance

logical opearator---> and,or,not
#an--->it needs all needs all conditions to be satisfie(two or more)-->
#or-->it needs any one condition to be statisfied
#not--->opp to existing
''''''
max_marks=80
vinay_marks=75
max_att=75
vinay_att=70

vinay_marks+=10
certificate=vinay_marks>=max_marks and vinay_att >=max_att
print(certificate)
chance=vinay_marks>=max_marks or vinay_att >=max_att
print(chance)
data=[]
print(data)
print(not(data))
data=[1,2,3,4]
print(not(data))
'''
#membership operators ---> in,not in
#check for the existance in sequence (str,,list,set,tuple,dict)
names=['vinay','vinay','bala','raju']
name='ajay'
print(name in names)
print(name not in names)
print('12'in'121')

print('ajay' in  'ajay')
print(['ajay']in ['ajay'])
#returns true as we are checking type As string
#it retures flase as its a lista-
'''
a=15
b=15
print(a==b)
print(id(a))
print(id(b))
print(b is a)'''
a=[1,2,3,4]
b=[1,2,3,4]

print(a==b)
print(id(a))
print(id(b))

# we have taken two lists eventhough with simlar values identity
print(a is b)
c=a
print(id(c))
print(c is a)
#when we checck with the interpreter mode and scripting mode above
#tuple resul changes
#bit wise operators---->it performs bitwise opearation--->&(bitwise and)
# (bitwise or),^(bitwise xor)
a=(7&3)
print(a)

print(7&3)
print(7|3)
print(7^3)

#shifting operator (<<,>>)
print(7 << 1)
