import random
board = ["-","-","-",
         "-","-","-",
          "-","-","-" ]

playerOne = "X"
winner = None
gameRunning = True


# Print a tic-tac-toe board 

def printBoard(board):
    print(board[0] + "|" + board[1]+ "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4]+ "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7]+ "|" + board[8])
   


# Take player one input 
    
def playerOneInput(board):
    userInput = int(input("Enter a number 1 through 9: "))
    if userInput >= 1 and userInput <=9 and board[userInput-1] == "-":
        board[userInput-1] = playerOne
    else:
        print("Board location filled already!")    


# Check for win or tie 
        
def checkHorizontal(board):
    global winner
    if board[0] == board [1] == board[2] and board[1] != "-":
        winner = board[0]
        return True 
    elif board[3] == board [4] == board[5] and board[4] != "-": 
        winner = board[3]
        return True 
    elif board[6] == board [7] == board[8] and board[7] != "-":
        winner = board[6]
        return True 
    
def checkVertical(board):
    global winner
    if board[0] == board [3] == board[6] and board[3] != "-":
        winner = board[0]
        return True 
    elif board[1] == board [4] == board[7] and board[4] != "-": 
        winner = board[4]
        return True 
    elif board[2] == board [5] == board[8] and board[5] != "-":
        winner = board[5]
        return True 
    
def checkDiagonal(board):
    global winner
    if board[0] == board [4] == board[8] and board[4] != "-":
        winner = board[4]
        return True 
    elif board[2] == board [4] == board[6] and board[4] != "-": 
        winner = board[4]
        return True 
     
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Tie!")
        gameRunning = False


def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        print(f"The winner is {winner}")

# Player 2 turn 
        
def playerTwoInput():
    global playerOne
    if playerOne == "X":
        playerOne = "0"
    else:
        playerOne ="X"

# Add randomised computer turn 
def computer(board):
    while playerOne == "0":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "0"
            playerTwoInput()      
        

while gameRunning:
    printBoard(board)
    playerOneInput(board) 
    checkWin()
    checkTie(board)
    playerTwoInput()
    computer(board)
    checkWin()
    checkTie(board)