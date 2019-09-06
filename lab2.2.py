def string_alternative():
    Input=input("Enter the String \n")
    output=''
    for character in Input[::2]:
        output=output+character
    print(output)



if __name__=='__main__':
    string_alternative()
