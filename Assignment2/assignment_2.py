# Use comments.
# Do not print anything else in the output other than what is mentioned.
# Give the correct filename(as given, not the one that is on your local machine) while reading a file.
# Plagiarism will be checked this time.
# Call every function after defining them, so that the function executes.
# Before submission, make sure to run the program and check whether everything is working.

# Assignment 2 ME369P
# Name: Julian Wearden
# EID : jfw864
#
# Fill in the functions and class below
import random
import numpy as np
import cmath
import math

def most_lines():
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
    characters = sorted(characters.items(), key=lambda k: k[-1], reverse=True)
    return characters[0][0]


def longest_line():
    # Open and read starwars.txt line by line
    longest = ""
    nameLong = ""
    with open("starwars.txt", "r") as starWarsFile:
        while True:
            line = starWarsFile.readline()

            # End loop when we reach the end of the file
            if not line:
                break

            # Find line
            speak = line.split('"')[5]
            speak = speak.replace('"', '')
            # Find characters name
            name = line.split('"')[3]
            name = name.replace('"', '')
            # If given line is longer than previously longest, store character in variable
            if len(speak) > len(longest):
                longest = speak
                nameLong = name
    return nameLong


def force_freq():
    characters = {}
    Force = "force"

    # Open and read starwars.txt line by line
    with open("starwars.txt", "r") as starWarsFile:
        while True:
            line = starWarsFile.readline()

            # End loop when we reach the end of the file
            if not line:
                break

            speak = line.split('"')[5]
            speak = speak.replace('"', '')
            speak = speak.split()
            # Find characters name
            name = line.split('"')[3]
            name = name.replace('"', '')

            for i in range(len(speak)):
                speak[i] = speak[i].lower()
            for i in range(len(speak)):
                if Force in speak[i]:
                    characters[name] = characters.get(name, 0) + 1

    # Sort the dictionary by item value
    characters = sorted(characters.items(), key=lambda k: k[-1], reverse=True)
    return characters[0][0]


def longest_word():
    # Open and read starwars.txt line by line
    longest = ""
    nameWord = ""
    with open("starwars.txt", "r") as starWarsFile:
        while True:
            line = starWarsFile.readline()

            # End loop when we reach the end of the file
            if not line:
                break

            # Find line
            speak = line.split('"')[5]
            speak = speak.replace('"', '')
            speak = speak.split()
            # Find characters name
            name = line.split('"')[3]
            name = name.replace('"', '')
            # If given word is longer than previously longest, store character in variable
            for i in range(len(speak)):
                if len(speak[i]) > len(longest):
                    longest = speak[i]
                    nameWord = name

    return nameWord, longest


def star_wars():
    # Write Code Here
    # Use instructions from the assignment document
    # Use starwars.txt as file

    mostLines = most_lines()
    print(mostLines, "had the most lines")
    longestLine = longest_line()
    print(longestLine, "had the longest line")
    forceFreq = force_freq()
    print(forceFreq, "said force the most")
    longestWord = longest_word()
    print(longestWord[0], "said the longest word which was", longestWord[1])



'''
Assume if a kwarg is not present, you should create the basic matrix
Assume the style is default to random
Assume the set is default to [0, 1]
kwargs can be :
    n =>  size of nxn matrix NOTE: You can assume if n is passed, i and j won't be
    i =>  number of rows     NOTE: If i is passed, assume j will be too
    j =>  number of columns
    range => [min, max] list
    set   => [number1, ..., numberN]
                NOTE: If set is specified, use that over range
                NOTE: If not specified, assume the set is the range
    style => a string which can be anything in {diagonal, upper, lower, symmetric, random}
                NOTE: any non-square matrix will be random
                NOTE: different styles will always be square matrices
    format => string that will be formatted as 1st and last element of each row
'''


class Matrix:
    def __init__(self, **kwargs):

        # Set size (n or i x j)
        if kwargs.get('n') is not None:
            self.n = kwargs.get('n')
            self.i = kwargs.get('n')
            self.j = kwargs.get('n')
        else:
            self.n = None
            self.i = kwargs.get('i')
            self.j = kwargs.get('j')

        # Set set and range
        if kwargs.get('set') is None and kwargs.get('range') is None:
            self.set = [0, 1]
            self.range = None
        elif kwargs.get('set') is not None:
            self.set = kwargs.get('set')
            self.range = None
        elif kwargs.get('set') is None:
            self.set = kwargs.get('range')
            self.range = kwargs.get('range')

        # Set style
        if self.i != self.j or kwargs.get('style') is None:
            self.style = 'random'
        else:
            self.style = kwargs.get('style')

        self.format = kwargs.get('format')

        # Build Matrix
        self.theMatrix = [[0 for x in range(self.i)] for y in range(self.j)]

    def build_matrix(self):
        # Build Matrix for each specific style
        if self.style == 'random':
            for i in range(int(self.i)):
                for j in range(int(self.j)):
                    if self.range is None:
                        self.theMatrix[i][j] = random.randint(self.set[0], self.set[1])
                    else:
                        self.theMatrix[i][j] = random.choice(self.range)
        else:
            for i in range(int(self.i)):
                for j in range(int(self.j)):
                    if self.range is None:
                        self.theMatrix[i][j] = random.randint(self.set[0], self.set[1])
                    else:
                        self.theMatrix[i][j] = random.choice(self.range)

            if self.style == 'diagonal':
                self.theMatrix = np.diag(np.diag(self.theMatrix))
            elif self.style == 'upper':
                self.theMatrix = np.triu(self.theMatrix[0])
            elif self.style == 'lower':
                self.theMatrix = np.tril(self.theMatrix[0])
            elif self.style == 'symmetric':
                self.theMatrix = np.tril(self.theMatrix).T + np.tril(self.theMatrix, - 1).T





def generateMatrix(**kwargs):
    # Write Code Here
    # print out matrix with newlines between rows
    # print out elements in rows 1 space apart, no space at the beginning
    matrix = Matrix(**kwargs)
    matrix.build_matrix()
    # Print Matrix
    for i in range(int(matrix.i)):
        print('')
        for j in range(int(matrix.j)):
            print(matrix.theMatrix[i][j], end='')


class QuadraticEquation:
    # Make sure to add all the specs the instructions ask for
    # Defualt constructor
    def __init__(self, a=0, b=0, c=0):
        self._a = a
        self._b = b
        self._c = c

    # Accessors
    def GetA(self):
        return self._a

    def GetB(self):
        return self._b

    def GetC(self):
        return self._c

    # Mutators
    def SetA(self, a):
        self._a = a

    def SetB(self, b):
        self._b = b

    def SetC(self, c):
        self._c = c

    # Calculate Discriminant
    def getDiscriminant(self):
        return (self._b ** 2) - (4 * self._a * self._c)

    #Calculate Roots
    def getRoots(self):
        # If discriminant is less than 0, we have to deal with complex math
        if self.getDiscriminant() < 0:
            root1 = (-self._b + cmath.sqrt(self.getDiscriminant())) / (2 * self._a)
            root2 = (-self._b - cmath.sqrt(self.getDiscriminant())) / (2 * self._a)
            root1 = str('{:.5f}'.format(root1))
            root2 = str('{:.5f}'.format(root2))
            Roots = (root1, root2)
        else:
            root1 = (-self._b + math.sqrt(self.getDiscriminant())) / (2 * self._a)
            root2 = (-self._b - math.sqrt(self.getDiscriminant())) / (2 * self._a)
            root1 = str('{:.5f}'.format(root1))
            root2 = str('{:.5f}'.format(root2))
            Roots = (root1, root2)
        return Roots


if __name__ == '__main__':
    star_wars()
    #generateMatrix(**kwargs)
    # # You can do any testing you want here
    # # Anycode you run here will not run when being graded...
    # # Here are some examples of how QuadraticEquation will be used..
    equation = QuadraticEquation(3, 4, 5)
    A = equation.GetA()
    equation.SetB(5)
    discr = equation.getDiscriminant()
    roots = equation.getRoots()
