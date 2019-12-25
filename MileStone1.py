def board_reset():
    '''
    Function to reset the Board Values for next Games
    :return:
    resetted Board Values List
    '''
    global board
    board = []
    for i in range(0, 10):
        k = str(i)
        board.append(i)


def display_board(board):
    '''
    Function to Display the current Board
    :param board: board is the list variable which stores the board values.
    :return: 
    '''
    #print('\n' * 100)
    #    print('   |   |')
    print(' ' + str(board[7]) + ' | ' + str(board[8]) + ' | ' + str(board[9]))
    #    print('   |   |')
    print('-----------')
    #    print('   |   |')
    print(' ' + str(board[4]) + ' | ' + str(board[5]) + ' | ' + str(board[6]))
    #    print('   |   |')
    print('-----------')
    #    print('   |   |')
    print(' ' + str(board[1]) + ' | ' + str(board[2]) + ' | ' + str(board[3]))


def player_input():
    '''
    Function to Allow user to Choose their Symbol. i.e X or O
    if player 1 chooses X, player 2 is automatically assigned O.
    if player 1 chooses O, player 2 is automatically assigned X.
    No values other than X or O are permitted for input.
    :return: 
    '''
    global p1
    global p2
    while True:
        p1 = input("Please choose your letter X or O")
        if p1 == 'X' or p1 == 'O':
            print("Player 1 has Chosen {}".format(p1))
            if p1 == 'X':
                p2 = 'O'
            else:
                p2 = 'X'
            print("Player 2 has Chosen {}".format(p2))
            break
        else:
            print("Invalid Option")
            continue


def player(k, val):
    '''
    Function to ask user the move.
    :param k: corresponds to Player number i.e 1 or 2
    :param val: Corresponds to Player Symbol chosen in last function i.e X or O
    :return: updated List board with player's response and prints the Updated Board
    '''
    display_board(board)
    while True:
        i = input("PLAYER {} Please select your square box input [1-9] only. E to Exit here".format(k))
        if i == 'E' or i == 'e':
            print ("PLAYER {} has Chosen to EXIT. Thanks for Playing.....".format(k))
            exit()
        elif int(i) not in range(1, 10) and (i != 'e' or i != 'E') :
            print("Enter only value betweek 1-10 ")
            continue
        if board[int(i)] == 'X' or board[int(i)] == 'O':
            print ("You can not choose already chosen value. Please select spot where X or O is not present")
            continue
        board[int(i)] = val
        print("Updated BOARD After PLAYER {} MOVE IS".format(k))
        #print(board)
        #display_board(board)
        break

def checkwin(val):
    '''
    Checks for possible match after player's Move.
    :param val: Corresponds to player number i.e 1 or 2.
    :return: True or False. If any of the player wins, True is returned.
    '''
    for i in pattern:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            print("Player {} has Won".format(val))
            return True


def checkmove():
    '''
    Checks if all the boxes have been filled by users.
    :return: True if all the 9 boxes have been used.
    '''
    j = 0
    for i in range(0, 10):
        if str(board[i]) != str(i):
            j += 1
    if j == 9:
        print("Moves Finished, No Player has Won")
        return True

def game():
    while True:
        player(1, p1)
        if checkwin(1):
            break
        elif checkmove():
            break
        player(2, p2)
        if checkwin(2):
            break
        elif checkmove():
            break


def main():
    global pattern
    pattern = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

    while True:
        board_reset()
        player_input()
        game()
        n = 0
        while n == 0:
            x = input("Do You want to Continue Y/N. ?")
            if x == 'Y' or x == 'y':
                print ("GAME IS ON!!!")
                n = 1
            elif x == 'N' or x == 'n':
                print ("Exiting the GAME. Thanks for Playing")
                n = 2
            else:
                print("Invalid Option. Please Try Again")
        if n == 2:
            break
        elif n == 1:
            continue

main()