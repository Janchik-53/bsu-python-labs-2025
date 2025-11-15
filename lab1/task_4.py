def calculate() :
    sum =int(input("Write sum : "))
    print("The number of bills : ")
    counter = 0
    money = 0
    while (sum - money) >= 100 :
        money += 100
        counter += 1
    print(f"100 : {counter}")
    counter = 0

    while (sum - money) >= 50 :
        money += 50
        counter += 1
    print(f"50 : {counter}")
    counter = 0

    while (sum - money) >= 10 :
        money += 10
        counter += 1
    print(f"10 : {counter}")
    counter = 0

    while (sum - money) >= 5 :
        money += 5
        counter += 1
    print(f"5 : {counter}")
    counter = 0

    while (sum - money) >= 2 :
        money += 2
        counter += 1
    print(f"2 : {counter}")
    counter = 0
    
    while (sum - money) >= 1 :
        money += 1
        counter += 1
    print(f"1 : {counter}")
    counter = 0

calculate()
