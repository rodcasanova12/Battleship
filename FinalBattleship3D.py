import random
#By Rodrigo Casanova
#   Example gameboard of 2 dimensions
#     0 0 0 0 0 0 0
#     0 x 0 0 0 0 0
#     0 0 0 0 0 0 0
#     0 0 0 0 0 0 0
#     0 0 0 0 0 0 0
#     0 0 0 4 4 4 4

levelDimension = 3
rowDimension = columnDimension = 6


def main():
    print("Inside the Main Method.")
    boats = [2,3,3,4,5]
    gameBoard = generateGameBoard()
    fillGameBoard(gameBoard, boats)
    printGameBoard(gameBoard)
    


def generateGameBoard():
    print("Inside generateGameBoard Method.")
    
    return [[['-' for c in range(12)]for r in range(12)]for l in range(3)]
    

def generateRandomIndex(maxValue):
    print("Generating Random Index Value")
    return random.randint(0, maxValue-1)

def fillGameBoard(gameBoard, boats):
    print("Inside fillGameBoard Method")
    for boatSize in boats:
        boatIdentifier = boatSize
        placeBoat(gameBoard, boatIdentifier, boatSize)

def checkValidPlacement(gameBoard, boatSize, levelIndexStart, rowIndexStart, columnIndexStart, defaultVerticalDirection=True):
    levelIndex = levelIndexStart
    rowIndex = rowIndexStart
    columnIndex = columnIndexStart
    for piece in range(boatSize):
        print("placing piece of number: {} at the following coordinates: {},{},{} ".format(piece, levelIndex, columnIndex, rowIndex))
        if(gameBoard[levelIndex][columnIndex][rowIndex] == '-'):
            if(defaultVerticalDirection):
                rowIndex += 1
                
            else:
                rowIndex -= 1
                

            if(rowIndex > rowDimension-1):
                defaultVerticalDirection = False
                rowIndex = rowIndexStart - 1
                columnIndex = columnIndexStart - 1
            
        else:
            return False

    return True

def placeBoat(gameBoard, boatIdentifier, boatSize, defaultVerticalDirection=True):
    #print("Inside placeBoat Method.")

    levelIndex = levelIndexStart = generateRandomIndex(levelDimension)
    rowIndex = rowIndexStart = generateRandomIndex(rowDimension)
    columnIndex = columnIndexStart = generateRandomIndex(columnDimension)

    #GameBoard is 3D array, only interacting with one level so will index by [x][y][0]
    print("level index: {}".format(levelIndex))
    print("row index: {}".format(rowIndex))
    print("column index: {}".format(columnIndex))

    if(checkValidPlacement(gameBoard, boatSize, levelIndexStart, rowIndexStart, columnIndexStart)):
        for piece in range(boatSize):
            print("placing piece of number: {} at the following coordinates: {},{},{} ".format(piece, levelIndex, columnIndex, rowIndex))
            gameBoard[levelIndex][columnIndex][rowIndex] = boatIdentifier
            if(defaultVerticalDirection):
                rowIndex += 1
       
            else:
                rowIndex -= 1
                
                
            if(rowIndex > rowDimension-1):
                defaultVerticalDirection = False
                rowIndex = rowIndexStart - 1
            
    else:
        placeBoat(gameBoard, boatIdentifier, boatSize)


def printGameBoard(gameBoard):
    for l in range(3):
        print('level',1+l)
        for r in range(12):
            print()
            for c in range(12):
                print(gameBoard[l][r][c],end = ' ')
        print()

    



if __name__ == "__main__":
    print("This file is being ran directly!")
    main()
    
