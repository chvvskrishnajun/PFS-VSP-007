'''
PYTHON-->POP,OOP
POP--> PROCEDURE ORIENTED PROGRAMING --> FUNCTIONS
FUNCTION-->A function is a block of code (statements) which performs a  speifi task.it is a reusable  code--> readibility
and easy to  main....

user defined function : def
Built in functions--> python by default (print,len,min,max,sorted,str,list,bool,dict...)
Anonymouns functions--> nameless functions --> lamda (map,filter) reduce
recursive functions-->recursion-->recursion --> factorial, fibanoccci --> decorators

syntax :
def fname(parameters): this is call a #function header
      """"Doc string (description of funtion)"""
      statements(s)....#body of the function
      .................
      return value(s)
fname(args)#function call

'''

#simple function to understand the reusebility
'''a=10
b=15
print(a+b)
'''
'''
def add(a,b):
    """this function returns the sum of given objects"""
    c = a+b
    #print(c) or return c
print(add(22,26))
print(add(8,6))
print(add(12,24))
print(add('code ','gnan'))
print(add('codegnan ,','vizag'))
print(add([1,2],[3,4,5,6,7,8]))
print(add([1,2],[2,1]))
'''
def add(a,b):
    """Sample Add function"""
    return f'Result is {a+b}'
c,d=map(int,input().split())
print(add(c,d))
print(add('code','gnan'))
g,h = 67,-45.5
e= add(g,h)
print(e)

#Function are also obects

def greeting():
    """Greeting to the user """
    return "hey guys", "welcome ","to codegnan" # a function can have multiple values to return but not multiple retunr statements.
print(greeting()*5)
print(type(greeting)) # return function
print(type(greeting()))# returns type of function


































































































