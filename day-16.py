'''
usage of for with conditional statements --->for with else
normal completion-->
notifications=[0,1,0,1,1,]
#0--->notification read
#1-->unread notification
#notification checker
for notification in notifications:
    if notification == 1:
        print("unread notification")
    else:
       print("all notification are caught up")
#Searching scenario same above program to be transformed--->
#if target if found
''''''
#break--->terminate the loop
notifications =[0,0,1,1,0,0]
#0-->nothification read
#1--->unread notification
#notificatoion checker
for notify in notifications :
    if notify == 1:
        print("unread notification")
        break
else:
    print("all notification are caught up")
    
'''
'''
fruits=["apple","banana","kiwi","cherrie"]
item  = input("which fruit u want:").lower()
for fruit in fruits:
    if item == fruit:
        print(f'you got your desires {item}')
        break
    else:
        print(f'could not find {item} in the fruits')
 '''
'''#break
#continue -->will skip the current iteration and proceeds for the
#rmng iteration
notifications= list(map(int,input("enter the values:").split(',')))
print(notifications)
for notify in notifications:
     if notify == 1:
         print("read notification")
     else:
         print("unread")

'''
#while True:
    #print("yes")# it runs an infinite loop we need to keyboard
#intializer"i=0
#while i>=1:
    #i=i+1
    #print(i)

i=10
while i>=1:
    print(i)
    i=i-1

    
