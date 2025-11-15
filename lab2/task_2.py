#Дан список чисел. Найдите индекс минимального элемента.
def main() :
    string = input("Введите список чисел : ")
    list1 =  string.split()
    list2 = string.split()
    list1.sort(reverse = False)#сортирова по возрастанию
    a = list1[0]
    print(list2.index(a))

main()