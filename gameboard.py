class BoardClass():
    board = [['','',''],['','',''],['','','']]
    playerOneUsername = ''
    playerTwoUsername = ''
    numGamesPlayed = 0
    numWins = 0
    numTies = 0
    numLosses = 0

        
    def recordGamePlayed(self):
        self.numGamesPlayed +=1
    
    def resetGameBoard(self):
        self.board = [['','',''],['','',''],['','','']]
    
    def playMoveOnBoard_X(self, boxNum):
        self.board[self.boxNumberToRowNumber(boxNum)][self.boxNumberToColumnNumber(boxNum)] = 'X'
    
    def playMoveOnBoard_O(self, boxNum):
        self.board[self.boxNumberToRowNumber(boxNum)][self.boxNumberToColumnNumber(boxNum)] = 'O'
    
    def boxNumberToRowNumber(self, boxNumber):
        if boxNumber == 1:
            rowNumber = 0
        elif boxNumber == 2:
            rowNumber = 0
        elif boxNumber == 3:
            rowNumber = 0
        elif boxNumber == 4:
            rowNumber = 1
        elif boxNumber == 5:
            rowNumber = 1
        elif boxNumber == 6:
            rowNumber = 1
        elif boxNumber == 7:
            rowNumber = 2
        elif boxNumber == 8:
            rowNumber = 2
        elif boxNumber == 9:
            rowNumber = 2
        return rowNumber
    
    def boxNumberToColumnNumber(self, boxNumber):
        if boxNumber == 1:
            columnNumber = 0
        elif boxNumber == 2:
            columnNumber = 1
        elif boxNumber == 3:
            columnNumber = 2
        elif boxNumber == 4:
            columnNumber = 0
        elif boxNumber == 5:
            columnNumber = 1
        elif boxNumber == 6:
            columnNumber = 2
        elif boxNumber == 7:
            columnNumber = 0
        elif boxNumber == 8:
            columnNumber = 1
        elif boxNumber == 9:
            columnNumber = 2
        return columnNumber

    def isBoardFull(self):
        for row in self.board:
            for eachButton in row:
                if '' in row:
                    return(False)
        else:
            return(True)
        
    def computeStats(self):
        statsList = [self.playerOneUsername, self.playerTwoUsername, self.numWins, self.numLosses, self.numTies, self.numGamesPlayed]
        return statsList
        
    def isGameFinished(self):
        
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == 'X': 
            print('X won')
            self.numWins += 1
            self.recordGamePlayed()
            self.resetGameBoard()
            
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == 'X':
            print('X won')
            self.numWins += 1
            self.recordGamePlayed()
            self.resetGameBoard()
        
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == 'X': 
            print('X won')
            self.numWins += 1
            self.recordGamePlayed()
            self.resetGameBoard()

        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == 'X':
            print('X won')
            self.numWins += 1
            self.recordGamePlayed()
            self.resetGameBoard()
            
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == 'X':
            print('X won')
            self.numWins += 1
            self.recordGamePlayed()
            self.resetGameBoard()
            
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == 'X':
            print('X won')
            self.numWins += 1
            self.recordGamePlayed()
            self.resetGameBoard()
        
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'X':
            print('X won')
            self.numWins += 1
            self.recordGamePlayed()
            self.resetGameBoard()
            
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == 'X':
            print('X won')
            self.numWins += 1
            self.recordGamePlayed()
            self.resetGameBoard()
        
        elif self.board[0][0] == self.board[0][1] == self.board[0][2] == 'O': 
            print('O won')
            self.numLosses += 1
            self.recordGamePlayed()
            self.resetGameBoard()
            
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == 'O':
            print('O won')
            self.numLosses += 1
            self.recordGamePlayed()
            self.resetGameBoard()
        
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == 'O': 
            print('O won')
            self.numLosses += 1
            self.recordGamePlayed()
            self.resetGameBoard()
            
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == 'O':
            print('O won')
            self.numLosses += 1
            self.recordGamePlayed()
            self.resetGameBoard()
            
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == 'O':
            print('O won')
            self.numLosses += 1
            self.recordGamePlayed()
            self.resetGameBoard()
            
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == 'O':
            print('O won')
            self.numLosses += 1
            self.recordGamePlayed()
            self.resetGameBoard()
        
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'O':
            print('O won')
            self.numLosses += 1
            self.recordGamePlayed()
            self.resetGameBoard()
            
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == 'O':
            print('O won')
            self.numLosses += 1
            self.recordGamePlayed()
            self.resetGameBoard()

        elif self.isBoardFull():
            print('there is a tie')
            self.numTies +=1
            self.recordGamePlayed()
            self.resetGameBoard()
        
        else:
            print('nobody won yet')
    
    
if __name__ == '__main__':
    testGameboard = BoardClass()
