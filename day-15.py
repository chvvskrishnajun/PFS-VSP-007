'''#range(stop)--->takes by default minimum value as 0
for i in range(5):
    print(f'value of i is {i}')
    print(f'square of i is {i**2}')
#range(start,stop)-->u can mention start and stop postns(values)
for i in range(1,11):
    print(i,i**2)
    print('<------>')
#range (start,stop,step)
    for i in range(1,21,1):
        print(i)
    for i in range
'''
'''
#get first 10 even numbers
#print numbers from 10 to 1 in reverse order

for i in range(2,21,2)
        print(i)

#print 'A'TO 'Z' in a single line

for i in range(65,92):
 print (i,chr(i),end='')


 #char wants number
 #ordinal wants alphabet

 ''''''
names =['akash','kaushik','vijay','sanjay','lokesh']
for  name in names:
     print(name,end' ')#this returnd in horizontal

for i in range(len(names)):
    print(names[i])
'''
#ask integer input from user and get sum of numbersas per input
'''
n=int(input())
if n>0:
     result=0
     for i in range(n+1):
         result=result + i
         print(result)
else:
    print("no output")
'''
#Usecase : Checkng daily work out app usage
work_log=[1,1,1,0,1,1,]
longest_streak=0
current_streak=0
for day in work_log:
     if day==1:
         current_streak=current_streak+1
         if current_streak > longest_streak:
             longest_streak=current_streak
     else:
        current_streak=0
print(f'longest streak is {longest_streak}')
