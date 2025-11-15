def checkpassword(string) :
    
    if len(string) < 16 :
        print("Too short!")
    elif string.isalpha() or string.isdigit() :
        print("Weak password!")
    else :
        print("secure password!")

if __name__ == "__main__"  :
    string = input("Create a password : ")  
    result = checkpassword(string)
