#Создайте два множества. Найдите их симметрическую разность
def main() :
    set1 = {1,2,3,4,5,6}
    set2 = {5,6,7,8,9,10}
    symmetric_difference = set1 ^ set2
    print(symmetric_difference)

main()