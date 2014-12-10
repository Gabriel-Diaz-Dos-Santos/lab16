# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.delete(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
rocket1 = drawpad.create_rectangle(400,585,405,590)
player = drawpad.create_oval(390,580,410,600, fill="blue")
enemy = drawpad.create_rectangle(50,50,100,60, fill="red")
rocket1Fired = False

direction = 5


class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        # Enter my text
        self.prompt = "Rockets left :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

        self.rockets = 3
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rocketsTxt.pack()
        
        self.rocketFired = False
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
        global drawpad
        global enemy
        global direction
        global rocket
        global rocket1Fired
        x1,y1,x2,y2 = drawpad.coords(enemy)
        px1,py1,px2,py2 = drawpad.coords(player)
        #rocketsx1, rocketsy1, rocketsx2, rocketsy2 = drawpad.coords(rockets)
        if rocket1Fired == True:
            drawpad.move(rocket1,0,-5)
        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        drawpad.after(5,self.animate)
        
        global direction
    # Get the x and y co-ordinates of the circle
        x1, y1, x2, y2 = drawpad.coords(player)
        if x2 > drawpad.winfo_width(): 
                direction = - 4
        elif x1 < 3:
            direction = 4
    #Move our oval object by the value of direction
            drawpad.move(player,direction,0)

    def key(self,event):
        global player
        global rocket1Fired
        x1,y1,x2,y2 = drawpad.coords(player)
        if event.char == "w":
            if y1 > 0:
                drawpad.move(player,0,-4)
                drawpad.move(rocket1,0,-4)
        if event.char == "a":
            if x1 > 0:
                drawpad.move(player,-4,0)
                drawpad.move(rocket1,0,-4) 
        if event.char == "s": 
            if y2 < 600:
                drawpad.move(player,0,4)
                drawpad.move(rocket1,0,-4)  
        if event.char == "d": 
            if x2 <800:
                drawpad.move(player,4,0)
                drawpad.move(rocket1,0,-4)          
        if event.char == " ":
            self.rockets = self.rockets -1
            self.rocketsTxt.configure(text=self.rockets)
            rocket1Fired = True
           
    def collisionDetect(self, rocket):
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket)
app = myApp(root)
root.mainloop()