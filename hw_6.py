#угадай число
import random

count = 0
guessnumber = random.randint(0, 100)
number = 0
while True:
    number = int(input("Угадайте число от 1 до 100: "))
    count += 1
    if(number < guessnumber):
        print("Загаданное число больше. Попробуйте еще раз")
    elif(number > guessnumber):
        print("Загаданное число меньше. Попробуйте еще раз")
    elif(number == guessnumber):
        print(f"Вы выиграли с {count} попытки! Спасибо за игру!")
        print("""
                         ------------
                         |           |
                         |  0     0  |
                         |     <     |
                         |  .     .  |
                         |   `...`   |
                         ------------
                            """)
        if input("Сыграем еще? 'n|y':") == 'y':
            guessnumber = random.randint(0, 100)
            count = 0
        else:
            print("Спасибо за игру: ")
            break