inputstr=input("Enter the string \n")
liststr=[]
for i in inputstr:
    liststr.append(i)
lenlist=len(liststr)
middle=int(lenlist/2)
secondchar=int((lenlist/2)-1)
liststr.remove(liststr[middle])
liststr.remove(liststr[secondchar])
rev=liststr[::-1]
output=''.join(rev)
print(output)





