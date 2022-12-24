import tkinter as tk

from tkinter import messagebox as mb

def call():
    res=mb.askquestion('Exit Application', 'Cannot connect to server. \nDo you want to try again? ')
    if res == 'no' :
        print (res)
        root.destroy()
    else :
        print(res)
        mb.showinfo('Return', 'Lets try again')
        
root= tk.Tk()
canvas = tk.Canvas(root, width = 200, height = 200)
canvas.pack()

b = tk.Button(root,
           text ='Click this button',
           command = call)
  
canvas.create_window(100, 100, 
                     window = b)
root.mainloop()
