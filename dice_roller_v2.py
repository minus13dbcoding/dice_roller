import random

# Version 2 - THis allows the user to roll seprate dice running the program only once.

#varibles to be used through out
sides = 0
num_dice = 0
rolls = []
same_dice = False

# Sets up what the user is rolling. First asks how many dice are being rolled and whether or not these are have the same amounr of sides.

def dice_to_roll():
	num_dice = int(input("How many dice? "))
	same_dice = input("Are all dice the same y/n? ")
	same_dice = same_dice.lower
	if same_dice == "y":
		same_dice = True
		print("")
		print("You have choosen to roll all the dice with the same amount of sides")
	else:
		same_dice = False
		print(" ")
		print("You have choosen to roll different sided dice.")
	return same_dice, num_dice
		
# This rolls the dice for the user. Asks how many sides the dice gave. If smae_dice = True, then it will roll all dice with the same side, while if smae_dice = False, it will ask the user to define how many sides each dice has. It will then out put a list of numbers for each dice rolled.

def dice_rolls():
		if same_dice == True:
			sides = int(input("How many sides does the dice have? "))
			for num in range(0, num_dice):
				rolled = random.randint(sides)
				rolls.append(sides)
			print("You have rolled: ")
			print(rolls)
		else:
			if same_dice == False:
				for num in range (0, num_dice):
					rolled = random.randint(sides)
					rolls.append(sides, " sided dice: ", rolled)
			print(rolls)
		
dice_to_roll()
print(same_dice)
dice_rolls()

"""
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
"""