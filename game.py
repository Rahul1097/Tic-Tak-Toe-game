#Tic Tac Toe game
import random

def display_board(board):
    '''Displays board'''
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('   |   |   ')

def player_input():
    '''Player 1 marker and player 2 marker selection.Returns marker for players'''

    marker = ''

    while marker!='X' and marker!='O':
        marker = input("Player1: Choose X or O :").upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker, position):
    '''Places the marker on the board'''
    board[position] = marker

def win_check(board, mark):
    '''Check each row, column and diagonals.Returns True if won'''
    return ((board[1] == mark and board[2] == mark and board[3]==mark) or 
    (board[4] == mark and board[5] == mark and board[6]==mark) or 
    (board[7] == mark and board[8] == mark and board[9]==mark) or 
    (board[1] == mark and board[4] == mark and board[7]==mark) or 
    (board[2] == mark and board[5] == mark and board[8]==mark) or 
    (board[3] == mark and board[6] == mark and board[9]==mark) or 
    (board[1] == mark and board[5] == mark and board[9]==mark) or 
    (board[3] == mark and board[5] == mark and board[7]==mark) )

def choose_first():
    '''Chooses which player will start the game first.Returns player'''
    flip = random.randint(0,1)

    if flip == 0:
        return ("Player1")
    else:
        return ("Player2")

def space_check(board,position):
    '''Checks if the space is free on board.Returns true if space is free'''
    return board[position]== ' '

def full_board_check(board):
    '''Checks if full board is filled. Returns True if full board is filled'''
    for i in range(1,10):
        if space_check(board,i)==True:
            return False
    return True

def player_choice(board):
    '''Take position from user to place the marker.Returns position.'''
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position(1-9) :"))

    return position

def replay():
    '''Checks if the user wants to play again'''
    choice = input("Play again?Enter Y or N").lower()

    if choice == "y":
        return True
    else:
        return False


print("Welcome to Tik Tak Toe Game....!!!")
print("\n")

while True:
    #define board, player1,player3 markers
    board = [' ']*10
    player1_marker, player2_marker = player_input()

    #Decide which player will start first
    turn = choose_first()
    print(turn + " will goes first.")

    #Check if user is ready
    play_game = input("Ready to play? y or n :").lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    #start the game
    while game_on:
        if turn == 'Player1':
            #display board
            display_board(board)
            #Ask for position to place the marker
            position = player_choice(board)
            #place marker
            place_marker(board,player1_marker,position)
            #check if the player has won or game is tie else switch to player2
            if win_check(board,player1_marker):
                display_board(board)
                print("Player 1 has won the game")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is Tie...!!!")
                    break
                else:
                    turn = "Player2"
        
        else:
            #display board
            display_board(board)
            #Ask for position to place the marker
            position = player_choice(board)
            #place marker
            place_marker(board,player2_marker,position)
            #check if the player has won or game is tie else switch to player1
            if win_check(board,player2_marker):
                display_board(board)
                print("Player 2 has won the game")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is Tie...!!!")
                    break
                else:
                    turn = "Player1"

    #check if player wants to play again
    if not replay():
        break







