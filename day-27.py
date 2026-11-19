'''
reduce()--->it will try to its reduce in to single   value...it
repeatedly appiles a function to combine elements...

we can use it  from functools syntax --> reduce (function,iterable)

import functools
from functools import reduce
#sum of numbers from a itterable
numbers=[1,5,2,3,4]
result = reduce(lambda a,b:a+b,numbers)         
print(result)

#Largest numbers from a collection
data=list(map(int,input("enter").split()))
print(data)
result=reduce(lambda a,b:a if a>b else b,data)
print(result)
#Return the longest word in a group of strings

words = ['python','developer','sql','programing']
longest_word = reduce(lambda a,b: a if len(a)>len(b) else b,words)
print(f'Longest word : {longest_word}')

map---> transformation
filter---->selection
reduce---->aggregation (functools)
'''
#list comprehensions ---> inpytho, it is a precise way to create
#lists
#syntax--->[expression for item in iterable]
#itterable ---->list,set,dict,or range()
'''
li=[]
for i in range(10):
    li.append(i)
print(li)

li=[i for i in range(10)]
print(i)

squares = [i**2 for i in range(1,11)]
print(squares)

even=[i for i in range(1,11)if i%2==0]
print(even)

#update scores of each person with 10 marks
scores=[25,45,50,60,55]
f_scores = [i+10 for i in scores]
print(f_scores)
'''
names=['saketh','codegnaa','vizag']
capital = [i.upper()for i in names]
print(capital)

result=list(map(lambda i:i.upper(),names))
print(result)

#List Comprehension with if-else usage
#[true_value if condition else false_value for item in iterable]
data=[12,4,5,6,8,9]
result=["even" if i%2==0 else "odd" for i in data]
print(result)
result=[i**2 if i%2==0 else i**3 for i in data]
print(result)

#nested lsit comperhensions---> one inside anther
#[expression for i in iterabel 1 for j in iterable2]
sizes=['red','blue','white']
colors=['s','m','l','xl']
dress=[(color,size)for color in colors for size in sizes]
print(dress)

d=[(i,j) for i in range(1,5) for j in range(1,5)]
print(d)
print(*d)

