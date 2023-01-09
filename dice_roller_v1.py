import random

def dice_roll():
	rolls = int(input("How many rolls? "))
	sides = int(input("How many sided dice? "))
	for num in range(0, rolls):
			number = random.randint(1, sides)
			print(number)

play = True
while play == True:
	dice_roll()
	again = input("Roll again y/n? ")
	again = again.lower()
	if again == "n":
		play = False
		print("Thanks for rolling")