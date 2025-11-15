# Дан список чисел. Удалите все элементы, которые больше среднего арифметического списка.
def main() :
    array = [1.09,4.66,3.88,1,1,1,1,1,88,88,67]
    average = sum(array) / len(array)
    result = []
    for x in array :
        if x <= average :
            result.append(x)

    print(result)


main()


    