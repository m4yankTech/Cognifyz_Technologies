import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["","","","","","",""], ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if(gameBoard[x][y] == "🔵"):
                print("",gameBoard[x][y], end=" |")
            elif(gameBoard[x][y] == "🔴"):
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyTurn(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkWinner(turn):
    for row in range(rows):
        for col in range(cols - 3):
            if gameBoard[row][col] == turn and gameBoard[row][col + 1] == turn and gameBoard[row][col + 2] == turn and gameBoard[row][col + 3] == turn:
                return True

    for col in range(cols):
        for row in range(rows - 3):
            if gameBoard[row][col] == turn and gameBoard[row + 1][col] == turn and gameBoard[row + 2][col] == turn and gameBoard[row + 3][col] == turn:
                return True

    for row in range(rows - 3):
        for col in range(cols - 3):
            if gameBoard[row][col] == turn and gameBoard[row + 1][col + 1] == turn and gameBoard[row + 2][col + 2] == turn and gameBoard[row + 3][col + 3] == turn:
                return True

    for row in range(3, rows):
        for col in range(cols - 3):
            if gameBoard[row][col] == turn and gameBoard[row - 1][col + 1] == turn and gameBoard[row - 2][col + 2] == turn and gameBoard[row - 3][col + 3] == turn:
                return True

    return False

turnCounter = 0
while True:
    printGameBoard()
    if turnCounter % 2 == 0:
        print("\nPlayer 1's turn (🔵)")
        turn = "🔵"
    else:
        print("\nPlayer 2's turn (🔴)")
        turn = "🔴"

    column = input("Enter the column letter (A-G) where you want to place your disc: ").upper()
    if column not in possibleLetters:
        print("Invalid column! Please enter a valid column letter (A-G).")
        continue

    colIndex = possibleLetters.index(column)
    for row in range(rows - 1, -1, -1):
        if gameBoard[row][colIndex] == "":
            gameBoard[row][colIndex] = turn
            break
    else:
        print("Column is full! Please choose another column.")
        continue

    if checkWinner(turn):
        printGameBoard()
        if turnCounter % 2 == 0:
            print("\nPlayer 1 wins! (🔵)")
        else:
            print("\nPlayer 2 wins! (🔴)")
        break

    turnCounter += 1
