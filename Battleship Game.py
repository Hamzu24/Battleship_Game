#Battleships Problem
import time
import random

player1board = []
AIBoard = []
player1VisibleBoard = []

def fillBoard(board, item):
  for i in range(0, 9):
    board.append([])
    for j in range(0, 9):
      board[i].append(item)

fillBoard(player1VisibleBoard, "#")
fillBoard(player1board, " ")
fillBoard(AIBoard, " ")

def printBoard(board):
  for i in range(0, 10):
    for j in range(0, 10):
      print(board[i][j], end=" ")
      if j == 9:
        print()

location = "0 0"
wrongInputs = ["/"] #Fills this so the code runs at first
separatedStrings = [[], [], [], []]
numberLocations = [[], [], [], []]
placementDifferences = []
print("Place Battleships in the format of x y, x y, etc. except input the number of 'x y's that matches the ship length")
time.sleep(1)
print("Use the numbers 0-9 for the x and y co-ordinates")
#Placing The Battleships
for i in range(0, 4):
  wrongInputs = ["/"] #Fills this so the code runs at first
  while wrongInputs != []:
    print("Choose the locations for Battleship #"+ str(i+1) +". It has a length of "+ str(4-i) +"\n")
    if wrongInputs != ["/"] and wrongInputs != []:
      print("Your last placement didn't work because these positions weren't empty: ")
      #Prints the positions that weren't empty last attempt
      for j in range(0, len(wrongInputs)):
        print(str(wrongInputs[j-1][0]) +" "+ str(wrongInputs[j-1][1]) +"\n")
    location = input("Choose the locations: ")
    wrongInputs = [] #Resets the wrong inputs array
    #Splits your output into an array with the different strings
    separatedStrings = location.split(", ")
    if len(separatedStrings) == 4-i:
      #Makes the array numberLocations filled with arrays of the ship x and y locations as ints
      for j in range(0, 4-i):
        separatedStrings[j] = separatedStrings[j].strip()
        numberLocations[j] = [int(separatedStrings[j][0:1]), int(separatedStrings[j][2:])]
        #Checks that that space on the board is not already full
        if player1board[numberLocations[j][0]][numberLocations[j][1]] != " ":
          wrongInputs.append(numberLocations[j])
      #Fills the spaces on the board
      if wrongInputs == []:
        if 4-i == 1:
          differenceArray = [0, 0]
        else:
          differenceArray = [(numberLocations[0][0] - numberLocations[1][0]), (numberLocations[0][1] - numberLocations[1][1])]
        if (differenceArray[0] <= 1 and differenceArray[0] >= -1) and (differenceArray[1] <= 1 and differenceArray[1] >= -1):
          if 4-i > 2:
            for j in range(1, 4-i-2):
              tempValues = [(numberLocations[j][0] - numberLocations[j+1][0]), (numberLocations[j][1] - numberLocations[j+1][1])]
              if tempValues[0] != differenceArray[0] or tempValues[1] != differenceArray[1]:
                wrongInputs = ["/"]
          if wrongInputs == []:
            for j in range(0, 4-i):
              player1board[numberLocations[j][0]][numberLocations[j][1]] = "X"
        else:
          print("Those ship positions do not align in a straight line (diagonals are allowed)")
          wrongInputs = ["/"]
    else:
      print("That was not the right number of positions for a ship of length "+ str(4-i) +"\n")
      wrongInputs = ["/"]

time.sleep(1)
print("Thank you for placing your ships. The AI will now place theirs...")
time.sleep(1)
print("Note: AI ships can sometimes wrap over the sides of the board (eg. the x coords for one ship could be 7, 8, 0)")

def createNewArrangement(locationArray, directionArray):
  if random.randint(0, 1) == 0:
    if random.randint(0, 1) == 0:
      locationArray[0] = (locationArray[0]+1) % 9
    else:
      locationArray[1] = (locationArray[1]+1) % 9
  else:
    if random.randint(0, 1) == 0:
      directionArray[0] = (directionArray[0]+1) % 2
    else:
      directionArray[1] = (directionArray[1]+1) % 2
      

startingLocation = [10, 10]
shipDirection = [10, 10]
directionChoices = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
isWrongPlacement = True
for i in range(0, 4):
  startingLocation = [random.randint(0, 8), random.randint(0, 8)]
  shipDirection = random.randint(0, len(directionChoices)-1)
  isWrongPlacement = True
  while isWrongPlacement == True:
    print(shipDirection)
    print(startingLocation)
    for j in range(0, 4-i):
      if j == 0:
        if AIBoard[startingLocation[0]][startingLocation[1]] != " ":
          isWrongPlacement = True
          break
      else:
        if AIBoard[(startingLocation[0]+(shipDirection[0]*j))%9][(startingLocation[1]+(shipDirection[1]*j))%9] != " ":
          isWrongPlacement = True
          break
        elif j == 4-i-1:
          isWrongPlacement = False
    if isWrongPlacement == True:
      createNewArrangement(startingLocation, shipDirection)
  for j in range(0, 4-i):
    if j != 0:
      AIBoard[(startingLocation[0]*shipDirection[0]*j)%9][(startingLocation[1]*shipDirection[1]*j)%9] = "X"
      #print(str((startingLocation[0]*shipDirection[0]*j)%9) +", "+ str((startingLocation[1]*shipDirection[1]*j)%9))
    else:
      AIBoard[startingLocation[0]][startingLocation[1]] = "X"
      #print(str(startingLocation[0]) +", "+ str(startingLocation[1]))
    print(i)
      
    

    
    
