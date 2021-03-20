# Created by Ellie Le at 3/19/2021

# Create board structure
board = [' ' for x in range(10)]

# Add X or O on board based on position
def insertLetter(letter, pos):
    board[pos] = letter


# Add space on board
def spaceIsFree(pos):
    return board[pos] == ' ' # return True


# Define the loop of the board
def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('-'*10)
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-' * 10)
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

# Check when board is full
def isBoardFull(board):
    if board.count(' ') > 1: # count the empty space
        return False
    else:
        return True

# Check the winner
def IsWinner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))

# Create player movement
def playerMove():
    running = True
    while running:
        move = input("Please select a position to place an 'X' between (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    running = False
                    insertLetter('X' , move)
                else:
                    print("This space is occupied")
            else:
                print("Please enter a number between 1-9")

        except:
            print("Please type a number")


# Create AI movement
def AIMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    print(possibleMoves)
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move


    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    # if corner is open, move to corner
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # if center is free
    if 5 in possibleMoves:
        move = 5
        return move

    # if edges is open
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

# Create random movement for AI
def selectRandom(li):
    import random
    ln = len(li) # get index range
    r = random.randrange(0,ln)
    return li[r] # select random value from list

def main():
    print("Welcome to Tic Tac Toe")
    printBoard(board)

    # check if AI is winner
    while not(isBoardFull(board)):
        # if computer doesn't win
        if not(IsWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else: # if computer win
            print("Computer won!")
            break

        # if player doesn't win
        if not(IsWinner(board, 'X')):
            move = AIMove()
            if move == 0:
                print(' ')
            else:
                insertLetter('O' , move)
                print('Computer placed an O on position', move, ':')
                printBoard(board) # update board
        # when player won
        else:
            print("You won!")
            break


    if isBoardFull(board):
        print("Tie game")

# Make the game interface
while True:
    x = input('Do you want to play? (y/n) ')
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('-'*10)
        main()
    else:
        break