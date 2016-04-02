# Задача 6. Вариант 0.

#Разработайте систему начисления очков для задачи 6, в соответствии с которой 
#игрок получал бы большее количество баллов за меньшее количество попыток.

# Krasnikov A. S.
# 02.03.2016

import random

print("Программа случайным образом загадывает название одного из четырех животных, встреченных Колобком в лесу, а игрок должен его угадать.\nЧем меньше попыток вы используете, тем больше баллов заработаете.")

animal_numbers = random.randint(1,4)

if animal_numbers == 1 :
    animal = 'Зайц'
elif animal_numbers == 2 :
    animal = 'Волк'
elif animal_numbers == 3 :
    animal = 'Медведь' 
elif animal_numbers == 4 :
    animal = 'Лиса'

trial = 3
bonus = 3000

while trial > 0 :
    answer = input('\nНазовите одно из животных, встреченных Колобком в лесу: ')
    if answer == animal :
        print('\nВы угадали!')
        print('Вам начислено', bonus, 'баллов.')
        break
    else :
        print('\nВы не угадали!!!')
        if trial > 1 :
            print('Попробуйте еще раз.')
        else :
            print('Правильный ответ: ', animal)
        
    trial -= 1
    bonus -= 1000

		
input("\n\nНажмите Enter для выхода.")
