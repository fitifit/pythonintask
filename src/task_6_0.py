# Задача 6. Вариант 0.

#Создайте игру, в которой компьютер загадывает название одного из четырех 
#животных, встреченных Колобком в лесу, а игрок должен его угадать.

# Krasnikov A. S.
# 02.03.2016

import random

print("Программа случайным образом загадывает название одного из четырех животных, встреченных Колобком в лесу, а игрок должен его угадать.")

animal_numbers = random.randint(1,4)

if animal_numbers == 1 :
    animal = 'Зайц'
elif animal_numbers == 2 :
    animal = 'Волк'
elif animal_numbers == 3 :
    animal = 'Медведь' 
elif animal_numbers == 4 :
    animal = 'Лиса'

answer = input('\nНазовите одно из животных, встреченных Колобком в лесу: ')

if answer == animal :
    print('\nВы угадали!')
else :
    print('\nВы не угадали!!!')
    print('Правильный ответ: ', animal)

input("\n\nНажмите Enter для выхода.")
