def sign(day,month) :
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Рыбы"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "Близнецы"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        return "Весы"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "Скорпион"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "Стрелец"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козерог"
    else:
        return "Неверная дата"
    
def main() :
    try:
        day = int(input("Введите день рождения (число): "))
        month = int(input("Введите месяц рождения (число): "))
        
        
        if month < 1 or month > 12:
            print("Ошибка: месяц должен быть от 1 до 12")
            return
        
        if day < 1 or day > 31:
            print("Ошибка: день должен быть от 1 до 31")
            return
        
        if month == 2 and day > 29:
            print("Ошибка: в феврале не может быть больше 29 дней")
            return
        elif month in [4, 6, 9, 11] and day > 30:
            print(f"Ошибка: в этом месяце не может быть больше 30 дней")
            return
        
        zodiac = sign(day, month)
        print(f"\nВаш знак зодиака: {zodiac}")
        
    except ValueError:
        print("Ошибка: введите числа для дня и месяца")

main()
    
    
    
