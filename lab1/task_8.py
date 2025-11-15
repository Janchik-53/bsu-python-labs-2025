def main() :
    string = input("Введите строку : ")
    i = 0

    while i < len(string)/2 :
        if string[i] != string[len(string) - 1 - i] :
            print("Не палиндром !")
            return
        i += 1
    print("Палиндром!") 

main()
        
            

    