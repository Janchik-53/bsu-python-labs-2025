#Создайте словарь, где ключами являются символы строки, а значениями — их количество.
def main():
    string = input("Введите строку : ")
    dict = {}
    for char in string :
        if dict.get(char) is None :
            dict[char] = 1

        else :
            dict[char]+= 1

    print(dict)

main()


        
        