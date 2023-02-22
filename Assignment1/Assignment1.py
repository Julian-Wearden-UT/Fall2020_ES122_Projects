# File: Assignment1.py
# Student: Julian F. Wearden
# UT EID: jfw864
# Course Name: ES122
#
# Date Created: 10/04/2020
# Date Last Modified: 10/04/2020

# Imported for use in star_travel
import re
from math import sqrt


# ##########################STAR WARS#####################################################################
def star_wars():
    # Dictionary to store characters and number of lines
    characters = {}

    # Open and read starwars.txt line by line
    with open("starwars.txt", "r") as starWarsFile:
        while True:
            line = starWarsFile.readline()

            # End loop when we reach the end of the file
            if not line:
                break

            # Find characters name
            name = line.split('"')[3]
            name = name.replace('"', '')

            # Add characters name to dictionary and add 1 to their number of lines
            characters[name] = characters.get(name, 0) + 1

    # Sort the dictionary by item value, and then alphabetically
    characters = sorted(characters.items(), key=lambda k: (-k[1], k[0]))

    # Print the dictionary
    for key, value in iter(characters):
        print(key, value)


star_wars()

# #########################STAR TRAVEL####################################################################


def star_travel():

    try:
        # First count the number of rows in the file
        with open("stars.txt", "r") as starsFile:
            rows = 0
            content = starsFile.read()
            contentList = content.split("\n")

            for i in contentList:
                if i:
                    rows += 1
        # Create a 2d array to store information about stars (Name, x, y, z)
        w, h = 4, rows
        starInfo = [[0 for x in range(w)] for y in range(h)]

        # Open file and parse information needed and store into 2d array
        currentLine = 0
        with open("stars.txt", "r") as starsFile:
            while True:
                line = starsFile.readline()

                # Break when we reach end of file
                if not line:
                    break

                # Parse information in text file into two objects
                lineFormat = re.search(r'(.+)\s\[(.+)\]', line)

                # Assign parsed info to a variable
                name = lineFormat.group(1)
                coordinates = lineFormat.group(2)
                x = coordinates.split()[0]
                y = coordinates.split()[1]
                z = coordinates.split()[2]

                # Store variable in 2d array
                starInfo[currentLine][0] = name
                starInfo[currentLine][1] = x
                starInfo[currentLine][2] = y
                starInfo[currentLine][3] = z
                currentLine += 1

    # Exit program if file is missing or if file is incorrectly formatted
    except IOError:
        print("Error reading file")

    # Iterate through every star and find the distance of each one to another
    for i in range(rows):
        for j in range(rows):
            # Make sure we aren't comparing a star to itself
            if i != j:
                x1 = int(starInfo[i][1])
                y1 = int(starInfo[i][2])
                z1 = int(starInfo[i][3])
                x2 = int(starInfo[j][1])
                y2 = int(starInfo[j][2])
                z2 = int(starInfo[j][3])

                # Calculate distance between stars
                distanceSquared = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
                distance = sqrt(distanceSquared)
                distance = round(distance, 3)

                # Use first distance between two stars to initialize base max and min
                if i == 0 and j == 1:
                    currentMax = distance
                    currentMin = distance
                    star1F = starInfo[i][0]
                    star2F = starInfo[j][0]
                    star1C = starInfo[i][0]
                    star2C = starInfo[j][0]

                # If the distance between the stars is higher than the current max, update the current max
                if distance >= currentMax:
                    currentMax = distance
                    star1F = starInfo[i][0]
                    star2F = starInfo[j][0]
                # If the distance between the stars is lower than the current min, update the current min
                if distance <= currentMin:
                    currentMin = distance
                    star1C = starInfo[i][0]
                    star2C = starInfo[j][0]

    print("Farthest stars are", star1F, "and", star2F, "at a distance of:", currentMax)
    print("Closest stars are", star1C, "and", star2C, "at a distance of:", currentMin)


star_travel()


# ##########################CALCULATOR####################################################################
def calculator():
    while True:
        operation = input("Enter operation: ")
        # Quit program when q is entered
        if operation == 'q':
            break

        firstNumber = input("Enter first number: ")
        secondNumber = input("Enter second number: ")

        # If no number is entered, make the number 0 by default
        if firstNumber == '':
            firstNumber = 0
        if secondNumber == '':
            secondNumber = 0

        # Convert values from string to floats
        firstNumber = float(firstNumber)
        secondNumber = float(secondNumber)

        # Complete desired operation
        if operation == '+':
            answer = firstNumber + secondNumber
        elif operation == '-':
            answer = firstNumber - secondNumber
        elif operation == '*':
            answer = firstNumber * secondNumber
        elif operation == '/':
            answer = firstNumber / secondNumber
        elif operation == '^':
            answer = firstNumber ** secondNumber
        # Note: "Else" not needed per assignment instructions, but added for consistency purposes
        else:
            answer = "Invalid operation dummy"

        print(answer)


calculator()
