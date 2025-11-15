

def main() :
    fio = input("Введите ФИО : ")
    surname,name,patronymic = fio.split()
    print(f"{surname} {name[0]}.{patronymic[0]}.")

if __name__ == "__main__":
    main()    