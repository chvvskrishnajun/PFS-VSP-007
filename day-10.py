'''#copy(),sort(),reverse()
details=[['sanjay','python',50],
         ['akash','flask',45],
         ['vinay','aptitude',30]]
print(details)
print(len(details))

#copy()-->creates a shallow copy of the given collection
data=details.copy()
#print(data)
#print(len(data))

data[0].append("A")
data.append("vizag")
print(data)
print(len(data))
print(details)
print(len(details))

data.extend(["pfs","jfs"])
print(data)
print(details)
print(len(details))

details.extend(["hyd","vizag","vijaywada","codegnan"])
print(details)
print(len(details))
print(len(data))
#in the below case we have  created basic lists so orginal is not effected
subjects=['python','my sql','aptitude','softskills']
data=subjects.copy()
print(data)

data=subjects
data.insert(2,"frontend")
print(data)
print(subjects)
subjects.remove("python")
print(subjects)
print(data)
''''''
#sort() reverse()
marks=[12,15,20,24,21]
print(marks.sort())#returns none as nothing to be returned
print(marks)

marks.sort(reverse=True)#it returns in descending order
print(marks)



marks.extend([-23,12,87])
print(marks)

marks.sort(reverse=True)
print(marks)

marks.extend(['poll','sunday',123])
marks.reverse()
print(marks)
print(marks[::-1])
'''''''
#min(),max(),len(),type(),sorted()
marks=[20,12,23,25,30]
print(marks)
print(min(marks))
print(max(marks))
b=sorted(marks)
print(b)
print(marks)
'''''
#tuples-->tuples are immutable,ordered,indexed collection,it can also have
#duplicates,we use ()
#data=()
#print(type(data))
#print(len(data))

#data=1,2,3,4,
#print(data)
#print(len(data))
'''
data=[0]
print(data)
print(len(data))
data=()
print(data)
print(len(data))

data=1,2,3,4,
print(data)
print(len(data))

#be very specific when we are passing data using()
#tuples are immutable we cannot modify the eliments in it
#data[-2]='codegnan'
details=("vizag",8,("pfs","jfs","da"),["aptitude","softskills"])
print(details[2][::2])

print(details[-1])
details[-1].extend(['python','java'])
print(details)
'''
'''
temp=(23.5,24,34.5)
b=temp*2
print(b)
print(b+temp)

tuples methods-->index(),count()
data=(12,3,24,3,12,4,5)
print(data)
print(data.index(3))
print(data.inidex(3,2))
print(data.count(3))

b=sorted(data)#returns sordted elements in a list
print(tupl(b))
c=tuple(sorted(data,reverse=True))#returns tuple in descending order
print(c)

del data #it completely eliminates the variable
#print(data)#nameerror
'''
'''
set:A set is an unorderd,unquie,mutable collection

ids=set()
print(ids)
print(type(ids))

name={'saketh','raju',24,3,'raju',24}
print(names)
print(len(names))

d={12,3,4,[12,3,4],45} we cannot have lists inside a set
print(d)





























