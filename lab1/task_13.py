import random

def game() :
    secretnumber = random.randint(1,100);
    attempt = 0;
    guess = 0;
    print("Я загадал число от 1 до 100,отгадай")

    while True:
        attempt +=1
        guess = int(input(f"Попытка {attempt} :"))

        if guess > secretnumber:
            print("Мое число меньше!")

        elif guess < secretnumber:
            print("Мое число больше")

        else :
            print(f"Поздравляю.Вы угадали число {secretnumber} за {attempt} попыток !")
            break

game()