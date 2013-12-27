# Graphics play sample app number 2
# (C) 2013 by Richard Sprague

# No, I am not going to do this:
# from tkinter import *
# because while I'm learning, I want to be very explicit
# about where the objects and methods come from.
import tkinter
import time
import pickle
from tkinter import Image

class Map():

    # the __init__ method is called when we create an instance of this class, so I want to set up everything here
    def __init__(self):

        # 'root' is the name I give to the main window.
        self.root = tkinter.Tk()
        self.time_label = tkinter.Label(self.root,text="time")
 
        self.update_clock()
        self.labelName = "Nathan"
        self.canvas = tkinter.Canvas(self.root,bg="blue", height=500,width=300)
        self.canvas.pack()
 
        self.nathan_label = tkinter.Label(self.root,text=self.labelName)
        self.root.bind("<KeyPress>", self.process_key)
        # lambda is a way to create a single expression so that it can appear as an argument.
        #self.root.bind("<Escape>", lambda e: self.root.destroy())
        # but I've got more to do when the user hits escape
        self.root.bind("<Escape>",self.leave)
        self.nathan_label.bind('<Double-1>',  self.ask_something) 

    def draw(self):
         self.time_label.pack()
         # pack() means just draw canvas whereever it is now, wherever it makes sense.
         self.canvas.pack()
         # place() will draw at a specific (x,y) location.
         self.nathan_label.place(x=self.x,y=self.y)
         # if you double-click the mouse when hovered over the nathan_label, it will do ask_something
         self.leprechaun_file = tkinter.PhotoImage(file="Leprechaun.gif")
         self.leprechaun = self.canvas.create_image(100,400,image=self.leprechaun_file)
         self.canvas.pack()

    def process_key(self,event):
        if event.keysym == "Up":
            self.move_up(10)
        elif event.keysym == "Down":
            self.move_down(10)
        elif event.keysym == "Left":
            self.move_left(10)
        elif event.keysym == "Right":
            self.move_right(10)
        elif event.keysym =="f":
            self.show_dialog()
        elif event.keysym =="b":
            self.go_boom()
        elif event.keysym == "r":
            self.make_rect()
        elif event.keysym == "s":
            self.save_state()
            
        self.nathan_label.place(x=self.x,y=self.y)


    def leave(self,event):
        r = tkinter.messagebox.askyesno("Ask Yes or No","Are you sure you want to quit?")
        if r:
            self.root.quit()
        

    def save_state(self):
        pass

        
    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.time_label.configure(text=now)
        self.root.after(1000,self.update_clock)

    def go_boom(self):
        self.nathan_label.config(text="Boom!",fg="blue",bg="red")
        
    def show_dialog(self):
        coord_string = "X="+str(self.x)+", Y=" +str(self.y)
        tkinter.messagebox.showinfo(title="X and Y",message=coord_string)

    def ask_something(self,event):
        r = tkinter.messagebox.askyesno("Ask Yes or No","Are you crazy?")
        print("You answered:", r)
 

    def make_arc(self):
        coord = (10,50,240,210)
        arc = self.canvas.create_arc(coord, start=0, extent=150, fill="red")


    def make_rect(self):
        rect = self.canvas.create_polygon(0,0,100,200, fill = "yellow")

    def move_down(self,increment):
        self.y = self.y+increment

    def move_up (self, increment):
        self.y = self.y-increment

    def move_left (self, increment):
        self.x=self.x-increment

    def move_right (self,increment):
        self.x = self.x+increment
        

def game_play():

    s= input("Resume (y/n)?")
    
    if s=="y":
        file = open("Nathansettings",'rb')
        x = pickle.load(file)
        y = pickle.load(file)
        file.close()
    else: x=y=100
    
    game_map = Map()
    game_map.x = x
    game_map.y = y

    game_map.make_arc()
    game_map.draw()

    
    # this tells the graphics system to go into an infinite loop and just follow whatever events come along.
    tkinter.mainloop()
    s= tkinter.messagebox.askyesno("Save state","Save?")
    if s:
        file = open("Nathansettings",'wb')
        pickle.dump(game_map.x,file)
        pickle.dump(game_map.y,file)
        file.close()

    print("Thanks for playing")
    game_map.root.destroy()



g = Map()








