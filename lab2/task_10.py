#Напишите программу, которая выводит таблицу умножения для чисел от 1 до 10
def main() :
    n = 10
    print("-" * 50)
    for i in range(1,n + 1) :
        for j in range(1,n + 1) :
            print(i," * ", j,"=", i * j)
        print("-" * 20)

main()