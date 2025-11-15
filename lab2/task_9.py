#Создайте словарь, где ключами будут слова из предложения, а значениями — длина этих слов
def main() :
    string = input("Введите предложение :")
    word = string.split()
    dict = {}

    for x in word :
        dict[x] = len(x)
    
    print(dict)

main()


