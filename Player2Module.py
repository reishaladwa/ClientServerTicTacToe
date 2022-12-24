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
    name = ''
    playerOne = 0
    playerTwo = 0
    myBoardClassObject = gameboard.BoardClass()
    theGameBoard = myBoardClassObject.board
    numOfWins = 0
    numOfLosses = 0
    numOfTies = 0
    numOfGamesPlayed = 0
    theMessage = ''
    global client
    FORMAT = "utf-8"
    rcv1 = ''
    turn = ''
    global stop_threads
    
    def __init__(self):
        self.canvasSetup()
        self.initTKVariables()
        self.createLabels()
        self.createQuitButton()
        self.createHostInfo()
        self.createPortInfo()
        self.createNameInfo()
        self.createPlayButton()
        self.createPlayerOneLabel()
        self.createPlayerTwoLabel()
        self.createTikTacToeButtons()
        self.createTurnLabel()
        self.runUI()
        #self.createPopUp()
    
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
        while True:
                stringdata = client.recv(1024).decode(self.FORMAT)
                print('Client received: ', stringdata)
                
                if stringdata is None:
                    break
                    
                if len(stringdata) == 0:
                    break
                
                vals = stringdata.split(",")
                print ('Vals 0 :'+vals[0])
                print ('Row '+vals[2])
                print ('Col '+vals[3])

                self.playerTwo.set(vals[1])
                
                if (vals[0] == 'stop'):
                    print('Stopping client')
                    client.close()
                    self.master.destroy()
                    break
            
                if (vals[0] == 'wookay'):
                    print('we are okay to play')
                
                if (vals[0] == 'move'):
                    self.playPlayer1sMove(vals[2])
                    self.turn.set(self.name.get())
                    
                if self.stop_threads:
                    print('closing thread now')
                    break
    
    def playPlayer1sMove(self, player1BoxNum):
        print('before playing player 1s move:')
        print(self.myBoardClassObject.board)
        
        player1BoxNum = int(player1BoxNum)
        self.myBoardClassObject.playMoveOnBoard_O(player1BoxNum)
        
        if player1BoxNum == 1:
            buttonTitle = self.buttonOne
        if player1BoxNum == 2:
            buttonTitle = self.buttonTwo
        if player1BoxNum == 3:
            buttonTitle = self.buttonThree
        if player1BoxNum == 4:
            buttonTitle = self.buttonFour
        if player1BoxNum == 5:
            buttonTitle = self.buttonFive
        if player1BoxNum == 6:
            buttonTitle = self.buttonSix
        if player1BoxNum == 7:
            buttonTitle = self.buttonSeven
        if player1BoxNum == 8:
            buttonTitle = self.buttonEight
        if player1BoxNum == 9:
            buttonTitle = self.buttonNine
        
        buttonTitle['text'] = self.myBoardClassObject.board[self.myBoardClassObject.boxNumberToRowNumber(player1BoxNum)][self.myBoardClassObject.boxNumberToColumnNumber(player1BoxNum)]
        
        if self.myBoardClassObject.isBoardFull() == True:
            self.myBoardClassObject.board == [['','',''],['','',''],['','','']]
            self.resetAllButtons()
        
        print('after playing player 1s move:')
        print(self.myBoardClassObject.board)
        self.myBoardClassObject.isGameFinished()
        
        print(self.myBoardClassObject.board)
        self.myBoardClassObject.isGameFinished()
        print('\n')
        
        self.numOfWins.set(self.myBoardClassObject.numWins)
        self.numOfLosses.set(self.myBoardClassObject.numLosses)
        self.numOfTies.set(self.myBoardClassObject.numTies)
        self.numOfGamesPlayed.set(self.myBoardClassObject.numGamesPlayed)
        
        if self.myBoardClassObject.board == [['','',''],['','',''],['','','']] or self.myBoardClassObject.isBoardFull():
            print('POP UP NOOOWWW')
            self.createPopUp()
            self.resetAllButtons()
    
    
    def playButtonPressed(self):
        print('play button has been pressed')
        
        global client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.hostname.get(), self.port.get()))
        
        # the thread to receive messages
        self.stop_threads = False
        global rcv
        rcv = threading.Thread(target=self.receive)
        rcv.start()
        
        msgAsBytes = str.encode('join'+','+self.name.get()+","+","+','+',' "UTF-8")
        client.sendall(msgAsBytes)    
            
        print(self.hostname.get())
        self.playerOne.set(self.name.get())
        self.turn.set(self.name.get())
    
    def canvasSetup(self):
        self.master = tk.Tk()
        self.master.title('Let\'s Play Tic Tac Toe!')
        self.master.geometry('660x500')
        self.master.configure(background='pink')
        self.master.resizable(0,0)
        
    def runUI(self):
        self.master.mainloop()
    
    def createQuitButton(self):
        self.quitButton = tk.Button(self.master, text = 'quit', command = self.closingSocket)
        self.quitButton.place(x=620, y=450)
    
    def closingSocket(self):
        print('requested to close from quit button')
        try:
            client
        except NameError:
            print("well, it WASN'T defined after all!")
            self.master.destroy()
        else:
            print("sure, it was defined.")
            msgAsBytes = str.encode('stop'+','+self.name.get()+","+","+","+"X", "UTF-8")
            client.sendall(msgAsBytes)

    
    def createLabels(self):
        tk.Label(self.master, text='Hostname: ').grid(row=0)
        tk.Label(self.master, text='Port: ').grid(row=1)
        tk.Label(self.master, text='Name: ').grid(row=2)
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
    
    def createNameInfo(self):
        self.nameInfoEntry = tk.Entry(self.master, textvariable=self.name)
        self.nameInfoEntry.grid(row=2, column=1)
    
    def createPlayButton(self):
        self.playButton = tk.Button(self.master, text='Play!', command=self.playButtonPressed)
        self.playButton.place(x=150, y=90)
    
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
        
        self.myBoardClassObject.playMoveOnBoard_X(boxNum)

        buttonNum['text'] = self.myBoardClassObject.board[self.myBoardClassObject.boxNumberToRowNumber(boxNum)][self.myBoardClassObject.boxNumberToColumnNumber(boxNum)]
    
        print(self.myBoardClassObject.board)
        self.myBoardClassObject.isGameFinished()
        print('\n')

        self.numOfWins.set(self.myBoardClassObject.numWins)
        self.numOfLosses.set(self.myBoardClassObject.numLosses)
        self.numOfTies.set(self.myBoardClassObject.numTies)
        self.numOfGamesPlayed.set(self.myBoardClassObject.numGamesPlayed)
        
        msgAsBytes = str.encode('move'+','+self.name.get()+","+str(boxNum)+","+str(self.myBoardClassObject.boxNumberToColumnNumber(boxNum))+","+"X", "UTF-8")
        print('move'+','+self.name.get()+","+str(self.myBoardClassObject.boxNumberToRowNumber(boxNum))+","+str(self.myBoardClassObject.boxNumberToColumnNumber(boxNum))+","+"X")
        client.sendall(msgAsBytes)
        
        self.turn.set('player1')
        
        if self.myBoardClassObject.board == [['','',''],['','',''],['','','']] or self.myBoardClassObject.isBoardFull():
            print('POP UP NOOOWWW')
            self.createPopUp()
            self.resetAllButtons()
            
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
        
    def createPopUp(self):
        self.theMessage = messagebox.askquestion('Play Again Message', 'Would you like to play again?')
        if self.theMessage == 'yes':
            print('yes')
            msgAsBytes = str.encode('playagain', "UTF-8")
            client.sendall(msgAsBytes)
            self.turn.set(self.name.get())
        else:
            print('requesting to close from yes/no')
            msgAsBytes = str.encode('stop'+','+self.name.get()+","+","+","+"X", "UTF-8")
            client.sendall(msgAsBytes)
        
if __name__ == '__main__':
    testing = tiktactoeUI()

    
