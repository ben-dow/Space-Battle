from tkinter import *
import random

class Bullet:
    def __init__(self,canvas,spaceship,shipobject):
        self.canvas = canvas
        self.spaceship = spaceship
        self.shipobject = shipobject
        x0,y0,x1,y1 = self.canvas.bbox(self.spaceship)
        xavg= (x0 + x1) /2
        yavg = (y0+y1) /2
        tags = ('bullet', random.random())
        self.tagid = tags[1]
        self.bullet = self.canvas.create_rectangle(xavg-3,yavg-3,xavg+3,yavg+3,fill='black',tag=tags)
        self.move()


    def move(self):
        self.canvas.move(self.tagid,0,-5)
        x0,y0,x1,y1 = self.canvas.bbox(self.tagid)
        midx = (x0 + x1) / 2
        midy = (y0 + y1) / 2
        for item in self.canvas.find_withtag('enemy'):
            w0,z0,w1,z1 = self.canvas.bbox(item)
            if midx >= w0 and midx <= w1:
                if midy >= z0 and midy <= z1:
                    self.shipobject.updatescore(1)
                    self.canvas.delete(item)
                    self.canvas.delete(self.tagid)
                    return
        if y1 < 0:
            self.canvas.delete(self.tagid)
            return
        self.canvas.after(20,self.move)

class Enemy:
    def __init__(self,canvas,xval):
        self.canvas = canvas
        self.enemy = self.canvas.create_polygon(0,0,20,20,25,30,30,20,50,0,30,10,20,10,fill= 'black', tag ='enemy')
        self.canvas.move(self.enemy,xval,0)
        self.movement()

    def movement(self):
        self.canvas.move(self.enemy, 0,1)
        self.canvas.after(100,self.movement)


class Ship:
    def __init__(self,canvas):
        self.score = 0
        self.canvas = canvas
        self.spaceship = self.canvas.create_polygon(10,10,30,10,30,5,40,5,40,10,60,10,60,30,10,30,10,10,fill='black', tag='ship')
        self.canvas.move(self.spaceship,0,450)

    def key(self,event=None):
        if event.keysym == 'Right':
            self.canvas.move(self.spaceship,4,0)
        elif event.keysym == 'Left':
            self.canvas.move(self.spaceship,-4,0)
    def shoot(self,event=None):
        Bullet(self.canvas,self.spaceship,self)
    def updatescore(self,newscore):
        self.score += newscore
        self.canvas.itemconfigure('score', text="Score: " + str(self.score))



class App:
    def __init__(self,master):
        self.canvas = Canvas(master,width=500, height = 500)
        self.canvas.pack()
        self.spaceship = Ship(self.canvas)
        master.bind_all("<Key>",self.spaceship.key)
        master.bind("<space>",self.spaceship.shoot)
        self.spawn_enemy()
        self.canvas.create_text(30,490,text="Score: 0", tag = "score")



    def spawn_enemy(self):
        position = random.randint(10,470)
        Enemy(self.canvas,position)
        time = random.randint(1000,5000)
        self.canvas.after(time,self.spawn_enemy)


root = Tk()
app = App(root)
root.title('SpaceBattle')
root.mainloop()
