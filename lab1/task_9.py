def main() :
    isip = 1
    string = input("Введите IP адрес : ")
    parts = string.split('.')

    if len(parts) != 4 :
        isip = 0
    
    for part in parts :
        if not part.isdigit() :
            isip = 0
        
        num = int(part)
        if num < 0 or num > 255 :
            isip = 0

    if isip == 0 :
        print("Некорректный IP адрес")
    else :
        print("корректный IP адрес")

main()   
