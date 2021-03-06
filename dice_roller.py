# random int generator
from random import randint

class Dice():
    """Create a dice"""
    def getDice(self):
        """Get dice number"""
        try:
            dice_number = int(input("How many dice would you like to roll? "))
        except ValueError:
            print("Please insert a valid option.")
        else:
            self.dice_number = dice_number 
    def get_number_of_sides(self):
        """Get side number"""
        try:
            sides = int(input("How many sides does each dice have? "))
        except ValueError:
            print("Please insert a valid option.")
        else:
            self.sides = sides
    def rollDice(self):
        """Roll the dice and return the results"""
        condition = input("Would you like to sum the results? (yes/no) ")
        if condition == 'yes':
            print("Ok, rolling %s dice with %s sides" % (self.dice_number, self.sides))
            sum_roll = 0
            for i in range(self.dice_number):
                roll = randint(0, self.sides)
                sum_roll += roll
            print(sum_roll)
        elif condition == 'no':
            print("Ok, rolling %s dice with %s sides" % (self.dice_number, self.sides))
            for i in range(int(self.dice_number)):
                roll = randint(0, self.sides)
                print(roll)
        else:
            print("Invalid command.")

# Create a dice and start the loop
while True:
    myDice = Dice()
    get_dice = myDice.getDice()
    if get_dice == 'None':
        break
    sides = myDice.get_number_of_sides()
    if sides == 'None':
        break
    myDice.rollDice()
    dice_condition = input("Would you like to quit the program? (yes/no) ")
    if dice_condition == 'yes':
        break
    elif dice_condition == 'no':
        continue
    else: 
        print("Invalid command.")
