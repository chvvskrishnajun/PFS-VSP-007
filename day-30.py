'''
f=open('new.text')
print(f.read())
f.close()
'''
'''
#best practice is we will use with use with statement
with open('new.txt','r')as file:
    print(file)
    print(file.read())

#writing to a file
#'w'mode will create a new file if not exsisting,else if already exists
#it will override the content
g = open('new.txt','w')
print(g)
g.write("saketh")
g.close()

h=open("today.txt","w")
h.write("pfs-vsp-007 is good but sometimes mischevious")
h.write("\n they make it is as gang")
logs=['\n First ID','\n vinay','\tAjay']
#h.write(logs)#it needs only text
h.writelines(logs)
#write lines(iteratle)-->writes an iterable of
#strings(such as list or tuple)
h.close()
print("done")

subjects=['python','\nsql','\n Aptitude']
with open("qwerty.txt","w") as file:
    file.writelines(subjects)
    print(file>read())#Io error
#when we use with block,we need not use close()
'''
#Appending to a file-->if file is already existing no change u can add the
#content,if not new file will be created
with open('today,txt','a') as file:
    file.write("\n Students need to finish last week Ai mock Interview")
#usecase: logging system
def log_activity(activity):
    """user logs to be stored"""
    try:
        with open('log.txt','a') as log_file:
        log_file.write(activity+'\n')
        log_file.read()#it will get into except block
    except Exception as e:
        print("error is",e)
    finally:
        print("file handing is important")
log_activity("vinay logged in for ai mock interview...")
log_activity("vinay is testing his microphone and a camera")
log_activity("vinay started his mock interview")
log_activity("vinay is writig  the code")
log_activity("vinay has finished and report created")

#r+--->read and write -->Preserves the existing content (data),
#new writes overwrite the characters from the start of the cursor...
with open ('log.txt','r+') as log file:
    log_file.writ("psf-vsp-007")
    print(log_file.read())
#in above case we are performing write first content is overwritten
#from the start of the cursor and when u read it rmg content will
#be shown
#use case:Modifying or updating parts of an exisitin file

    
    
    
    
