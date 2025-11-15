def math() :
    a = int(input("Введите целое число а : "))
    b = int(input("Введите целое число b : "))
    print(f"сумма a и b : {a + b}")
    print(f"разность a и b : {a - b}")
    print(f"произведение a и b : {a * b}")
    if b == 0 :
        print("Нельзя делить на ноль!")
    else :
        print(f"частное от деления a на b : {a / b}")
        print(f"остаток от деления a на b : {a % b}")

    print(f"результат возведения числа a в степень b : {a ** b}")

math()