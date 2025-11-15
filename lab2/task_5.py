# Дан список строк. Отсортируйте его в лексикографическом порядке.
def main() :
    user_input = input("Введите строки,разделяя точками :")
    list = user_input.split(".")
    list.sort()
    print(list)

main()