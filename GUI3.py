import tkinter as tk

master = tk.Tk()
master.title("Welcome to TicTacToe -a game by Reisha Ladwa")
master.geometry('800x400')

playerOne = tk.StringVar()
playerOne.set("-")
playerTwo = tk.StringVar() 
playerTwo.set("-")

my_string_var = tk.StringVar()

def userMove(btn1, r, c):
    my_text = btn1['text']
    btn1['text'] = "X"
    print (my_text)
    print("User Move ",r, " ",c)

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    my_string_var.set("What should learn")
    playerOne.set(e3.get())
    playerTwo.set("Server - 01")

tk.Label(master, text="Hostname: ").grid(row=0)
tk.Label(master, text="Port: ").grid(row=1)
tk.Label(master, text="Name: ").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

p1Label=tk.Label(master, text = "Player 1:").grid(row=4)
p2Label=tk.Label(master, text = "Player 2:").grid(row=5)

p1Name=tk.Label(master,textvariable = playerOne).grid(row=4, column=1, sticky=tk.W,pady=4)
p2Name=tk.Label(master,textvariable = playerTwo).grid(row=5, column=1, sticky=tk.W,pady=4)
                         
# set the text
#my_string_var.set("What should I learn")
  
# create a label widget
#my_label = tk.Label(master, 
#                 textvariable = my_string_var).grid(row=6)   
      
#player1Name = tk.Label(master, 
#                 textvariable = playerOne).grid(row=7)   


# tk.Button(master, 
#           text='Quit', 
#           command=master.quit).grid(row=3, 
#                                     column=0, 
#                                     sticky=tk.W, 
#                                     pady=4)

tk.Button(master, 
          text='Connect', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)
          

#tk.Button(master, 
#          text='0,0', command=show_entry_fields).grid(row=7, 
#                                                       column=1, 
#                                                       sticky=tk.W, 
#                                                       pady=4)


BtnA = tk.Button(master, text='0,0', command= lambda: userMove(BtnA, 0, 0))
BtnA.place(width=50, height=50, x = 200, y = 200)
          
BtnB = tk.Button(master, text='0,1', command= lambda: userMove(BtnB, 0, 1))
BtnB.place(width=50, height=50, x = 260, y = 200)

BtnC = tk.Button(master, text='0,2', command= lambda: userMove(BtnC, 0, 2))
BtnC.place(width=50, height=50, x = 320, y = 200)
                                                       
BtnD = tk.Button(master, text='1,0', command= lambda: userMove(BtnD, 1, 0))
BtnD.place(width=50, height=50, x = 200, y = 260)
          
BtnE = tk.Button(master, text='1,1', command= lambda: userMove(BtnE, 1, 1))
BtnE.place(width=50, height=50, x = 260, y = 260)

BtnF = tk.Button(master, text='1,2', command= lambda: userMove(BtnF, 1, 2))
BtnF.place(width=50, height=50, x = 320, y = 260)

BtnG = tk.Button(master, text='2,0', command= lambda: userMove(BtnG, 2, 0))
BtnG.place(width=50, height=50, x = 200, y = 320)
          
BtnH = tk.Button(master, text='2,1', command= lambda: userMove(BtnH, 2, 1))
BtnH.place(width=50, height=50, x = 260, y = 320)

BtnI = tk.Button(master, text='2,2', command= lambda: userMove(BtnI, 2, 2))
BtnI.place(width=50, height=50, x = 320, y = 320)


tk.mainloop()