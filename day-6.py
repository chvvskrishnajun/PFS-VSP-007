'''
Tokens,datatypes(Numeric,boolean,none type,sequences(str,lists,tuples,sets,
frozensets mapping objects(dicts)) typecasting
operators
input Formatting/out Formatting
'''
'''
#Input foramting --->input()
#Usage of input()
#we can pass any type of object as input --->result is in only sring
name=input("enter the name:")
print(name)
print(type(name))
''''''
#integer input-->int()
roll_number=int(input("enter the roll number:"))
print(roll_number)
print(type(roll_number))


#Float Input -->float()
marks =float(input("enter the marks:"))
print(marks)
print(type(marks))
''''''
''''''
#Group of strings (group of values as strings)
#return List
#group of the strings(mutiple vlues as strings)
names=input().split()# we need default values
names=input("enter the subjects:").split(',')
print(names)
print(type(names))''''''
#comma sparated value name
name,batch=input("enter the details:").split()
print(name)''''''
print(batch)
''''''
#multiple integer values
#we will use map()
order_id,cost=map(float,input().split())
print(order_id,cost)

subjects,marks=map(float,input().split())
''''''
py_marks,ap_marks,ss_marks,sql_marks=map(float,input().split())
print(py_marks,ap_marks,ss_marks,sql_marks)'''''
#Groupp of integer float values

'''stu_marks=list(map(int,input().split(',')))
print(stu_marks)'''
'''
discounts=lsit(map(float,input("enter the discount:").split(',')))
print(discounts)'''

#Accept the cost of selling the product from user and also the original cost
#of the product and determine the profit/loss amount for the user
'''
original_amount=float(input())
selling_amount=float(input())
profit=original_amount-selling_amount
print(profit)
'''
'''
#set of integers
#set of Float values--->replace in with float
ids=set(map(int,input("enter ids").split(',')))
print(ids)
print(type(ids))
'''
#passing dict data using eval
'''
stu_details=eval(input("enter the data:"))
print(stu_details)
#output formating---->print()
a,b,c=map(str,input("enter the names:").split())
print(a,b,c)
#now we will use sep--->sep is the keyword
print(a,b,c,sep="-----")
#end is specifically telling how u want end the statements
#here end=tab space charcters
print(a,b,c,sep=":")#here end=space character
print("chvvsk","pithapuram")
print(34,4.5)
'''
#using commas in print()--->we separeate by commas
'''
name="codegnan";branch="vizag";batch='pfs-vsp-007'
print(name,"is in ",branch)
print(batch,"belongs to",branch,"banch")
'''

#2)using %(modulas) formating---->old style c programing
#%d---->integers,%f--->float,%S---->strings
age=32
price=45.256
place="vizag"
print("Age=%d | price =%f | place =%s"(age,price,place))
