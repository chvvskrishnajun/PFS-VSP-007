'''
FUNCTIONS-->A reusable block of code which performs a  task....

def fname(args):parameters #fun def -->fromal agrguments
            """doc string"""
            statement(s)...
            .....
            return values(s)...
fname(args) #actual agrguments


positional arguments --> count of argunments be matched
default arguments--> we can make arguments as default
keyword arguments --> order/keyword name to be matched
variable length arguments (*args)--> we can pass any number of postnl agrguments
keyword variable length arguments(***kwargs)--->we can pass any number of positional agrguments
''''''
#positional arguments ---> count of arguments to be matched
def data(a,b,c):
    """function to perform airthmetic operators"""
    d=a+b+c
    e=a-b-c
    f=a*b*c
    g=a/b/c
    return d,e,f,g
print(data(12,3,1))
#print (data(23,1,))#type errors as count is mismatched
#print(data(1,4,5,6,7))#type error-->takes only 3 arguments
d,e,f=map(int,input().split())
result=data(d,e,f)
print(f'result is {result}')
'''
'''
##default arguments --> we can arguments as default
def data(a,b=2,c=5):#non-default arguments always follows default arguments
    """"funtion to perform airthmetic operators"""
    d=a+b+c
    e=a-b-c
    f=a*b*c
    g=a/b/c
    return d,e,f,g
print(data(2,4,8))
print(data(12))#here we need not mention other args as they are default
print(data(2,4))#here one default argument taken
print(data())# mandatory count to be matched
d=int(input())
print(data(d))#mandatory count to be matched
'''
#keyword arguments -->keyword name to be matched
#grocery purchase

#def grocery(item,price):
#def grocery(item="milk",price):#not at all possible
def grocery(item,price=40):
    """usage of keyword arguments"""
    print(f'Itemm is {item}')
    print(f'value of {price}')
grocery("milk",35)
#grocery (40,"bread")# in the case order differs result changes
grocery(price=40,item="bread")
#grocery(items='bread',price=60)#type error --> keyword arguments mismatch
grocery("milk")

#variable length arguments-->  we can capture any number of position
#arguments,we use (*args),captures excess positional argumentS and
#pack them into______tuple______

def sample(*a):
    """ usage of aribitray arguments"""
    print(a)
    print(type(a))
sample()



      
