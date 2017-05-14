
import random
sput =  ["Фобос", "Деймос"]
rsput = random.choice(sput)
score = 10
psput = ""
while psput != rsput:
	psput = input("Назовите один из спутников Марса: ")
	if psput == rsput:
		print("\nХорооош!")
		print("У вас", score,"баллов.")

	else:
		score-=5
		print("\nНе правильно((\nПопробуйте еще раз\n\n")
input("\n\nНажмите Enter для выхода")
