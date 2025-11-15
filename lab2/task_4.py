#Напишите программу, которая находит количество делителей у числа N.
def main() :
    counter = 0
    n = int(input("Введите натуральное число : "))
    for i in range(1,n + 1) :
        if n % i == 0 :
            counter += 1

    print(counter)

main()

    