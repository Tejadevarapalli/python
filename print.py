inputstr=input("Enter the sentence \n")
words=inputstr.split()
for i in words:
    if(i=='python'):
        words=inputstr.replace(i,"pythons")
print(words)
