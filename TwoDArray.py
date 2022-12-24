#from array import *

def initNewBoard():
    Movs = [['-', '-', '-'], ['-','-','-'], ['-','-','-']]
    return Movs

def updateBoard(brd, r, c, val):
    brd[r][c]=val

def printBoard(mv):
    for r in mv:
        for c in r:
            print(c,end = " ")
        print()


def hasPlayerTwoWon(mv):
    won = False;

    #check all rows
    if (mv[0][0] == 'X' and mv[0][1] == 'X' and mv[0][2] == 'X'):
        return True

    if (mv[1][0] == 'X' and mv[1][1] == 'X' and mv[1][2] == 'X'):
        return True

    if (mv[2][0] == 'X' and mv[2][1] == 'X' and mv[2][2] == 'X'):
        return True

    #check all columns
    if (mv[0][0] == 'X' and mv[1][0] == 'X' and mv[2][0] == 'X'):
        return True

    if (mv[0][1] == 'X' and mv[1][1] == 'X' and mv[2][1] == 'X'):
        return True

    if (mv[0][2] == 'X' and mv[1][2] == 'X' and mv[2][2] == 'X'):
        return True

    #check the diagonals 
    if (mv[0][0] == 'X' and mv[1][1] == 'X' and mv[2][2] == 'X'):
        return True

    if (mv[0][2] == 'X' and mv[1][1] == 'X' and mv[2][0] == 'X'):
        return True
    
    return won

def hasPlayerOneWon(mv):
    won = False;

    #check all rows
    if (mv[0][0] == 'O' and mv[0][1] == 'O' and mv[0][2] == 'O'):
        return True

    if (mv[1][0] == 'O' and mv[1][1] == 'O' and mv[1][2] == 'O'):
        return True

    if (mv[2][0] == 'O' and mv[2][1] == 'O' and mv[2][2] == 'O'):
        return True

    #check all columns
    if (mv[0][0] == 'O' and mv[1][0] == 'O' and mv[2][0] == 'O'):
        return True

    if (mv[0][1] == 'O' and mv[1][1] == 'O' and mv[2][1] == 'O'):
        return True

    if (mv[0][2] == 'O' and mv[1][2] == 'O' and mv[2][2] == 'O'):
        return True

    #check the diagonals 
    if (mv[0][0] == 'O' and mv[1][1] == 'O' and mv[2][2] == 'O'):
        return True

    if (mv[0][2] == 'O' and mv[1][1] == 'O' and mv[2][0] == 'O'):
        return True
    
    return won





board = initNewBoard()
printBoard(board)

updateBoard(board,0,0,'X')
printBoard(board)
print(hasPlayerTwoWon(board))

updateBoard(board,0,1,'X')
printBoard(board)
print(hasPlayerTwoWon(board))

updateBoard(board,0,2,'X')
printBoard(board)
print(hasPlayerTwoWon(board))

# isTie
#   if playerOne has won or playerto has won 
#      return false
#    
#     if spots left return false 
#         else return True
#


