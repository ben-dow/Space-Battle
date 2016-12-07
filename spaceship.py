from tkinter import *

class Ship:
    def __init__(self,canvas):
        self.canvas = canvas
        self.spaceship = self.canvas.create_rectangle(10,10,50,50,fill='black')

    def key(self,event):
        if event.keysym == 'Right':
            self.canvas.move(self.spaceship,3,0)
        elif event.keysym == 'Left':
            self.canvas.move(self.spaceship,-3,0)
        elif event.keysym == 'Down':
            self.canvas.move(self.spaceship,0,3)
        elif event.keysym == 'Up':
            self.canvas.move(self.spaceship,0,-3)



class App:
    def __init__(self,master):
        self.canvas = Canvas(master,width=500, height = 500)
        self.canvas.pack()
        self.spaceship = Ship(self.canvas)
        master.bind_all("<Key>",self.spaceship.key)



root = Tk()
app = App(root)
root.title('SpaceBattle')
root.mainloop()
