import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
import gameboard
import socket
import threading


class tiktactoeUI():
    num1 = 0
    hostname = ''
    port = ''
    playerOne = 0
    playerTwo = 0
    myBoardClassObject = gameboard.BoardClass()
    theGameBoard = myBoardClassObject.board
    numOfWins = 0
    numOfLosses = 0
    numOfTies = 0
    numOfGamesPlayed = 0
    theMessage = ''
    global server
    global player1Name
    player1Name = 'player1'
    conne = ''
    global addr
    FORMAT = "utf-8"
    turn = ''
    player2Name = ''
    
    def __init__(self):
        self.canvasSetup()
        self.initTKVariables()
        self.createLabels()
        self.createQuitButton()
        self.createHostInfo()
        self.createPortInfo()
        self.createPlayButton()
        self.createPlayerOneLabel()
        self.createPlayerTwoLabel()
        self.createTikTacToeButtons()
        self.createTurnLabel()
        self.runUI()
    
    def initTKVariables(self):
        self.num1 = tk.IntVar()
        self.hostname = tk.StringVar()
        self.port = tk.IntVar()
        self.name = tk.StringVar()
        self.playerOne = tk.StringVar()
        self.playerTwo = tk.StringVar()
        self.numOfWins = tk.IntVar()
        self.numOfLosses = tk.IntVar()
        self.numOfTies = tk.IntVar()
        self.numOfGamesPlayed = tk.IntVar()
        self.theMessage = tk.StringVar()
        self.turn = tk.StringVar()
        
    def receive(self):
        server.listen()
        conn, addr =  server.accept()
        self.conne = conn
        while True:
                stringdata = conn.recv(1024).decode(self.FORMAT)
                print('Server received: ', stringdata)
                
                if stringdata is None:
                    break
                    
                if len(stringdata) == 0:
                    break
        
                vals = stringdata.split(",")
                print ('Vals 0 :'+vals[0])
                
                if (vals[0] == 'move'):
                    print ('Player: '+vals[1])
                    print ('Row '+vals[2])
                    print ('Col '+vals[3])
                    print ('Mov: '+vals[4])

                    self.player2Name = vals[1]
                    self.playPlayer2sMove(vals[2])
                    self.turn.set('player1')
                
                if (vals[0] == 'stop'):
                    print('revised stop - will send stop to client')

                    msgAsBytes = str.encode('stop'+','+'player1'+","+","+","+"O", "UTF-8")
                    conn.sendall(msgAsBytes)
                    conn.shutdown(socket.SHUT_RDWR)
                    self.master.destroy()
                    break
                
                if (vals[0] == 'join'):
                    self.playerOne.set(vals[1])
                    self.turn.set(vals[1])
                    self.myBoardClassObject.playerOneUsername = 'player1'
                    self.myBoardClassObject.playerTwoUsername =  vals[1]
                    
                    print('server sending wookay')
                    msgAsBytes = str.encode('wookay'+','+'player1'+","+","+","+"O", "UTF-8")
                    conn.sendall(msgAsBytes)
                
                if vals[0] == 'playagain':
                    self.myBoardClassObject.board == [['','',''],['','',''],['','','']]
                    self.resetAllButtons()
    
    def playPlayer2sMove(self, player2BoxNum):
        print('before playing player 2s move:')
        print(self.myBoardClassObject.board)
        
        player2BoxNum = int(player2BoxNum)
        self.myBoardClassObject.playMoveOnBoard_X(player2BoxNum)
        
        if player2BoxNum == 1:
            buttonTitle = self.buttonOne
        if player2BoxNum == 2:
            buttonTitle = self.buttonTwo
        if player2BoxNum == 3:
            buttonTitle = self.buttonThree
        if player2BoxNum == 4:
            buttonTitle = self.buttonFour
        if player2BoxNum == 5:
            buttonTitle = self.buttonFive
        if player2BoxNum == 6:
            buttonTitle = self.buttonSix
        if player2BoxNum == 7:
            buttonTitle = self.buttonSeven
        if player2BoxNum == 8:
            buttonTitle = self.buttonEight
        if player2BoxNum == 9:
            buttonTitle = self.buttonNine
        
        buttonTitle['text'] = self.myBoardClassObject.board[self.myBoardClassObject.boxNumberToRowNumber(player2BoxNum)][self.myBoardClassObject.boxNumberToColumnNumber(player2BoxNum)]
        
        if self.myBoardClassObject.isBoardFull() == True:
            self.myBoardClassObject.board == [['','',''],['','',''],['','','']]
            self.resetAllButtons()
        
        print('after playing player 2s move:')
        print(self.myBoardClassObject.board)
        self.myBoardClassObject.isGameFinished()
        
        print(self.myBoardClassObject.board)
        self.myBoardClassObject.isGameFinished()
        print('\n')
        
        
        self.numOfWins.set(self.myBoardClassObject.numLosses)
        self.numOfLosses.set(self.myBoardClassObject.numWins)
        self.numOfTies.set(self.myBoardClassObject.numTies)
        self.numOfGamesPlayed.set(self.myBoardClassObject.numGamesPlayed)
        
    
    def startServerButtonPressed(self):
        print('start server button has been pressed')
        print(self.hostname.get())
        print(self.port.get())
        
        global server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.hostname.get(), self.port.get()))

        print('server has started')

        rcv = threading.Thread(target=self.receive)
        rcv.start()
         
        self.playerTwo.set('player1')
        self.playerOne.set('waiting for player 2...')
        
    
    def canvasSetup(self):
        self.master = tk.Tk()
        self.master.title('Server Tic Tac Toe')
        self.master.geometry('660x500')
        self.master.configure(background='lightblue')
        self.master.resizable(0,0)
        
    def runUI(self):
        self.master.mainloop()
    
    def createQuitButton(self):
        self.quitButton = tk.Button(self.master, text = 'quit', command = self.master.destroy)
        self.quitButton.place(x=620, y=450)
    
    def createLabels(self):
        tk.Label(self.master, text='Hostname: ').grid(row=0)
        tk.Label(self.master, text='Port: ').grid(row=1)
        tk.Label(self.master, text='Stats: ').place(x=0, y=300, width=300)
       
        tk.Label(self.master, text='games played: ').place(x=0, y=330, width=140)
        tk.Label(self.master, textvariable= self.numOfGamesPlayed).place(x=150, y=330, width=150)
        
        tk.Label(self.master, text='games won: ').place(x=0, y=360, width=140)
        tk.Label(self.master, textvariable= self.numOfWins).place(x=150, y=360, width=150)

        tk.Label(self.master, text='games lost: ').place(x=0, y=390, width=140)
        tk.Label(self.master, textvariable= self.numOfLosses).place(x=150, y=390, width=150)
        
        tk.Label(self.master, text='ties: ').place(x=0, y=420, width=140)
        tk.Label(self.master, textvariable= self.numOfTies).place(x=150, y=420, width=150)
        
        tk.Label(self.master, text='player 1: ').place(x=0, y=170)
        tk.Label(self.master, text='player 2: ').place(x=0, y=200)
        
        tk.Label(self.master, text='turn:').place(x=380,y=5)
    
        
    def createHostInfo(self):
        self.hostInfoEntry = tk.Entry(self.master, textvariable=self.hostname)
        self.hostInfoEntry.grid(row=0, column=1)
        
    def createPortInfo(self):
        self.portInfoEntry = tk.Entry(self.master, textvariable=self.port)
        self.portInfoEntry.grid(row=1, column=1)
    
    def createPlayButton(self):
        self.playButton = tk.Button(self.master, text='Start Server', command=self.startServerButtonPressed)
        self.playButton.place(x=125, y=65)
    
    def createPlayerOneLabel(self):
        self.playerOne.set('...')
        self.playerOneLabel = tk.Label(self.master, textvariable=self.playerOne)
        self.playerOneLabel.place(x=70,y=200)
        
    def createPlayerTwoLabel(self):
        self.playerTwo.set('...')
        self.playerTwoLabel = tk.Label(self.master, textvariable=self.playerTwo)
        self.playerTwoLabel.place(x=70,y=170)
    
    def createTurnLabel(self):
        self.turnLabel = tk.Label(self.master, textvariable=self.turn)
        self.turnLabel.place(x=430,y=5, width=150)
        
    
    def createTikTacToeButtons(self):
        self.buttonOne = tk.Button(self.master, text = '', command=lambda: self.ticTakToeButtonPressed(self.buttonOne))
        self.buttonOne.place(height=70, width=70,x=350,y=50)
        
        self.buttonTwo = tk.Button(self.master, text = '', command=lambda: self.ticTakToeButtonPressed(self.buttonTwo))
        self.buttonTwo.place(height=70, width=70,x=430,y=50)
        
        self.buttonThree = tk.Button(self.master, text = '', command=lambda: self.ticTakToeButtonPressed(self.buttonThree))
        self.buttonThree.place(height=70, width=70,x=510,y=50)
       
        self.buttonFour = tk.Button(self.master, text = '', command=lambda: self.ticTakToeButtonPressed(self.buttonFour))
        self.buttonFour.place(height=70, width=70,x=350,y=130)
        
        self.buttonFive = tk.Button(self.master, text = '', command=lambda: self.ticTakToeButtonPressed(self.buttonFive))
        self.buttonFive.place(height=70, width=70,x=430,y=130)
        
        self.buttonSix = tk.Button(self.master, text = '', command=lambda: self.ticTakToeButtonPressed(self.buttonSix))
        self.buttonSix.place(height=70, width=70,x=510,y=130)

        self.buttonSeven = tk.Button(self.master, text = '', command=lambda: self.ticTakToeButtonPressed(self.buttonSeven))
        self.buttonSeven.place(height=70, width=70,x=350,y=210)
        
        self.buttonEight = tk.Button(self.master, text = '', command=lambda: self.ticTakToeButtonPressed(self.buttonEight))
        self.buttonEight.place(height=70, width=70,x=430,y=210)
        
        self.buttonNine = tk.Button(self.master, text = '', command=lambda: self.ticTakToeButtonPressed(self.buttonNine))
        self.buttonNine.place(height=70, width=70,x=510,y=210)
        
    def ticTakToeButtonPressed(self, buttonNum):
        print(self.myBoardClassObject.board)
        
        if buttonNum == self.buttonOne:
            boxNum = 1
        if buttonNum == self.buttonTwo:
            boxNum = 2
        if buttonNum == self.buttonThree:
            boxNum = 3
        if buttonNum == self.buttonFour:
            boxNum = 4
        if buttonNum == self.buttonFive:
            boxNum = 5
        if buttonNum == self.buttonSix:
            boxNum = 6
        if buttonNum == self.buttonSeven:
            boxNum = 7
        if buttonNum == self.buttonEight:
            boxNum = 8
        if buttonNum == self.buttonNine:
            boxNum = 9
        
        self.myBoardClassObject.playMoveOnBoard_O(boxNum)

        buttonNum['text'] = self.myBoardClassObject.board[self.myBoardClassObject.boxNumberToRowNumber(boxNum)][self.myBoardClassObject.boxNumberToColumnNumber(boxNum)]
    
        print(self.myBoardClassObject.board)
        self.myBoardClassObject.isGameFinished()
        print('\n')

        self.numOfWins.set(self.myBoardClassObject.numLosses)
        self.numOfLosses.set(self.myBoardClassObject.numWins)
        self.numOfTies.set(self.myBoardClassObject.numTies)
        self.numOfGamesPlayed.set(self.myBoardClassObject.numGamesPlayed)
        
        msgAsBytes = str.encode('move'+','+player1Name+","+str(boxNum)+","+str(self.myBoardClassObject.boxNumberToColumnNumber(boxNum))+","+"X", "UTF-8")
        print('move'+','+self.name.get()+","+str(self.myBoardClassObject.boxNumberToRowNumber(boxNum))+","+str(self.myBoardClassObject.boxNumberToColumnNumber(boxNum))+","+"X")
        self.conne.sendall(msgAsBytes)
        
        self.turn.set(self.player2Name)
    
    def resetAllButtons(self):
        self.buttonOne['text'] = ''
        self.buttonTwo['text'] = ''
        self.buttonThree['text'] = ''
        self.buttonFour['text'] = ''
        self.buttonFive['text'] = ''
        self.buttonSix['text'] = ''
        self.buttonSeven['text'] = ''
        self.buttonEight['text'] = ''
        self.buttonNine['text'] = ''
        self.turn.set(self.player2Name)
        
        
        
if __name__ == '__main__':
    testing = tiktactoeUI()

    
