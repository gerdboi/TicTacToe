#Tic Tac Toe - Written by Jack Call
#Sources: Hafeezul Kareem Shaik of GeekFlare
#Description: I coded this game of tic tac toe based on the written instructions provided by GeekFlare. I took some
#liberties where I saw fit, such as allowing the user to select which symbol they want to have and determining whether
#the chosen coordinates of the next placement are valid (ie. in one of rows 1, 2, or 3; and assuring there isn't already)
#a symbol there).

#ROOM FOR IMPROVEMENT: Make the computer smarter, give it a way to learn strategy.

import random

#Blank game board
gameboard = [['-','-','-'],['-','-','-'],['-','-','-']]


#Check if game board is full
def boardFilled(gb):
    for r in gb:
        for c in r:
            if c == '-':
                return False
    return True        


#Check if there is a winner     
def gameWon(gb):
    #horizontal wins
    for r in range(3):
        if gb[r][0] == gb[r][1] == gb[r][2] and gb[r][0] != '-':
            return True
    
    #vertical wins
    for c in range(3):
        if gb[0][c] == gb[1][c] == gb[2][c] and gb[0][c] != '-':
            return True

    #diagonal wins
    if gb[0][0] == gb[1][1] == gb[2][2] and gb[1][1] != '-':
        return True

    if gb[0][2] == gb[1][1] == gb[2][0] and gb[1][1] != '-':
        return True

    return False


#Print the game board
def printBoard(gb):
    print(f' {gb[0][0]} | {gb[0][1]} | {gb[0][2]} ')
    print('--- --- ---')
    print(f' {gb[1][0]} | {gb[1][1]} | {gb[1][2]} ')
    print('--- --- ---') 
    print(f' {gb[2][0]} | {gb[2][1]} | {gb[2][2]} ')  


#Playing the game
def startGame():
    #Initialize a blank game board
    gb = gameboard

    #Allow the user to pick their symbol, and assign the computer to whatever symbol wasn't picked
    print('Would you like to play as X\'s or O\'s?')
    userSymbol = input('Enter X or O (case sensitive)')
    while userSymbol != 'X' and userSymbol != 'O':
        userSymbol = input('Please pick either X or O (case sensitive)')
    if userSymbol == 'X':
        computerSymbol = 'O'
    else:
        computerSymbol = 'X'

    #'flip a coin' to decide who goes first
    coin = random.randint(0, 1)
    if coin == 1:
        print('You go first!')
        turn = 1
    else:
        print('Computer goes first.')
        turn = 0
    
    #The game continues to go on until the board is full
    while not boardFilled(gb):
        printBoard(gb)
        #User's turn
        if turn == 1:
            #User picks a row to place in
            placeRow = int(input('What row would you like to place in?'))
            
            #Determine if the first pick is valid
            validRow = False
            if placeRow == 1 or placeRow == 2 or placeRow == 3:
                for i in gb[placeRow-1]:
                    if i == '-':
                        validRow = True

            #If first pick isn't valid, continue to prompt user for a valid choice
            while not validRow:
                placeRow = int(input('Please enter a valid row.'))
                if placeRow == 1 or placeRow == 2 or placeRow == 3:
                    for i in gb[placeRow-1]:
                        if i == '-':
                            validRow = True

            #User picks a column to place in
            placeCol = int(input('What column would you like to place in next?'))

            #Determine if the first pick is valid
            validCol = False
            if placeCol == 1 or placeCol == 2 or placeCol == 3:
                if gb[placeRow-1][placeCol-1] == '-':
                    validCol = True

            #If first pick isn't valid, continue to prompt user for a valid choice          
            while not validCol:
                placeCol = int(input('Please enter a valid column.'))
                if placeCol == 1 or placeCol == 2 or placeCol == 3:
                    if gb[placeRow-1][placeCol-1] == '-':
                        validCol = True

            #Places user symbol in the selected square
            gb[placeRow-1][placeCol-1] = userSymbol

        #Computer's turn
        else:
            print('Computer moves')

            #Picks a random row and random column
            computerCol = random.randint(0,2)
            computerRow = random.randint(0,2)
            
            #If this square is not empty, generate a new random coordinate
            while gb[computerRow][computerCol] != '-':
                computerCol = random.randint(0,2)
                computerRow = random.randint(0,2)

            #Place computer symbol in the selected square
            gb[computerRow][computerCol] = computerSymbol

        #Determine if there is a winner
        if gameWon(gb):
            #The winner will always be whoever's turn it is on this iteration
            #User wins
            if turn == 1:
                print('CONGRATULATIONS YOU WIN!')
                printBoard(gb)
                return

            #Computer wins
            else:
                print('YOU LOST! OMG YOU SUCK! THAT COMPUTER WAS PLAYING COMPLETELY AT RANDOM AND YOU LOST???? EMBARASSING!')
                printBoard(gb)
                return

        #Change whose turn it is at the end of the iteration    
        if turn == 1:
            turn = 0
        else:
            turn = 1

    #If the board fills without ever returning due to a game win, then the game is a draw
    print('GAME DRAW')

startGame()