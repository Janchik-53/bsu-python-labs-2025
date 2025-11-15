def main() :
    number = int(input("Введите число : "))
    if number % 7 == 0 :
        print(f"Число {number} магическое !")
    else :
        total = 0
        while number > 0 :
          total += number % 10
          number //= 10 
        print(f"Сумма цифр : {total}")

main()


