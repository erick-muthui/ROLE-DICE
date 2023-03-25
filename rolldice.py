# Importing random
import random

randomNumberList = []
face_1 = []
face_2 = []
face_3 = []
face_4 = []
face_5 = []
face_6 = []

# declared funtion to RollDice the dice


def rollDice():
    for i in range(1000):
        # generating random num of floats btwn 0-1 for random number list.
        n = random.random()
        randomNumberList.append(n)
    return


# function to Group the content of randomNumberList according to faces


def groupOfDiceFaces():
    # for every number generated if...
    for num in randomNumberList:
        if num >= 0 and num < 1/6:
            face_1.append(num)
        elif num >= 1/6 and num < 2/6:
            face_2.append(num)
        elif num >= 2/6 and num < 3/6:
            face_3.append(num)
        elif num >= 3/6 and num < 4/6:
            face_4.append(num)
        elif num >= 4/6 and num < 5/6:
            face_5.append(num)
        elif num >= 5/6 and num < 1:
            face_6.append(num)

    return


# RollDiceing the dice and grouping the groupOfDiceFaces
rollDice()
groupOfDiceFaces()


# generate length(frequency) of the elements in the groupOfDiceFaces
f1 = len(face_1)
f2 = len(face_2)
f3 = len(face_3)
f4 = len(face_4)
f5 = len(face_5)
f6 = len(face_6)

# Calculating the percentage
p1 = round(f1/1000*100, 1)
p2 = round(f2/1000*100, 1)
p3 = round(f3/1000*100, 1)
p4 = round(f4/1000*100, 1)
p5 = round(f5/1000*100, 1)
p6 = round(f6/1000*100, 1)

# Display the table
print("DICE_FACE   | FREQUENCY  |  PERCENTAGE")
print("_____________________________________")
print(f" 1          |  {f1}     |    {p1}%")
print(f" 2          |  {f2}     |    {p2}%")
print(f" 3          |  {f3}     |    {p3}%")
print(f" 4          |  {f4}     |    {p4}%")
print(f" 5          |  {f5}     |    {p5}%")
print(f" 6          |  {f6}     |    {p6}%")
print("_____________________________________")
print("            |  1000     |    100%   ")
print("_____________________________________")
