# Name:
# Period
# Dice Rolling Simulator

import random

print("Welcome to the Dice Rolling Simulator")

rolls = int(input("How many rolls? "))

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

rollNumber = 1

def printScore():
	 print("Ones: " + str(one))
	 print("Twos: " + str(two))
	 print("Threes: " + str(three))
	 print("Fours: " + str(four))
	 print("Fives: " + str(five))
	 print("Sixes: " + str(six))

while rollNumber <= rolls:
	diceNumber = random.randint(1,6)
	print("Roll number: " + str(rollNumber) + " result: " + str(diceNumber))
	if diceNumber == 1:
		one += 1
	elif diceNumber == 2:
		two += 1
	elif diceNumber == 3:
		three += 1
	elif diceNumber == 4:
		four += 1
	elif diceNumber == 5:
		five += 1
	else:
		six += 1
	
	rollNumber += 1
rollNumber = rollNumber - 1
print("")
print("Total rolls: " + str(rollNumber))
print("")
printScore()
totalScore = (int(one) + int(two) + int(three) + int(four) + int(five) + int(six))
oneX = one / totalScore * 100
twoX = two / totalScore * 100
threeX = three / totalScore * 100
fourX = four / totalScore * 100
fiveX = five / totalScore * 100
sixX = six / totalScore * 100
print("")
print("Ones: " + str(oneX) + "%")
print("Twos: " + str(twoX) + "%")
print("Threes: " + str(threeX) + "%")
print("Fours: " + str(fourX) + "%")
print("Fives: " + str(fiveX) + "%")
print("Sixes: " + str(sixX) + "%")



