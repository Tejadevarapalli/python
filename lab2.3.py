R=open("input.txt","r")
wordc={}
Input=R.read().split()
for i in Input:
    if i not in wordc.keys():
        wordc.update({i:1})
    else:
        wordc.update({i:wordc[i]+1})
o=open("output.txt","w+")
o.write(str(wordc))



