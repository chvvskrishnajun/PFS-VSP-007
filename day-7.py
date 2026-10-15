#3)usage of string formting --->str.fromat()
name="codegnan";branch="vizag";age=8
print("{} is in {} and its of {} years in edtech INDUSTRY".format(name,branch,age))

a,b=2,45
print("{1},{0}".format(a,b))
print("value of a is {} and value of b is {}".format(a,b))

#f-string notation-->python 3.9+ versions
print(f'{name} is in {branch}')

#make sure to denote the variables only in curly braces
print(f'vlaue of a is {a} and b is {b}')
print(f'"codegnan is in {branch} and of {age} years in trainings"')
