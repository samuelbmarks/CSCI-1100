from tkinter import *
import random

class Ball(object):
    def __init__ (self,x,y,dx,dy,radius,color):
        self.x,self.y = x,y
        self.radius = radius
        self.dx,self.dy = dx,dy
        self.color = color
        self.isstopped = False 
        
    def position(self):
        return self.x,self.y

    def move(self):
        self.x += self.dx
        self.y += self.dy
        
    def bounding_box(self):
        bounding_box = (self.x-self.radius, \
                        self.y-self.radius,\
                        self.x+self.radius, \
                        self.y+self.radius)         
        return bounding_box
        
    def get_color(self):
        return self.color
        
    def some_inside(self,maxx,maxy):
        if 0 < self.x + self.radius and \
              self.x - self.radius < maxx and \
              0 < self.y + self.radius and \
              self.y - self.radius < maxy:     
            return True
        return False
    
    def check_and_reverse(self, maxx, maxy):
        if self.x - self.radius <= 0 or self.x + self.radius >= maxx:
            self.dx = -self.dx
        elif self.y - self.radius <=0 or self.y + self.radius >= maxy:
            self.dy = -self.dy      
    
class BallDraw(object):
    def __init__ (self, parent):
        ##=====DATA RELEVANT TO BALL===============
        ##  We are going to repeatedly draw a ball object on the canvas,
        ##  "moving" it across the canvas.  The ball object is specified
        ## by (a) its x and y center coordinates (a tuple), (b) its radius,
        ##  (c) the delta x and delta y to move the ball in each time
        ## increment, and (d)  its color.
        self.balls_list = []
        for i in range(10):
            x = random.randint(10,390)
            y = random.randint(10,390)
            dx = random.randint(-8,8)
            dy = random.randint(-8,8)
            radius = random.randint(5,10)
            colorList = ["blue", "red", "green", "yellow", "magenta", "orange"]
            color = random.choice(colorList) 
            b = Ball(x,y,dx,dy,radius,color)
            self.balls_list.append(b)
        
        #========DATA NEEDED FOR ANIMATION=========
        #  Here is the time in milliseconds between consecutive instances
        #  of drawing the ball.  If this time is too small the ball will
        #  zip across the canvas in a blur.
        self.wait_time = 100 

        #this will allow us to stop moving the ball when the program quits
        self.isstopped = False 

        self.maxx = 400 # canvas width, in pixels
        self.maxy = 400 # canvas height, in pixels

        #=============CREATE THE NEEDED GUI ELEMENTS===========
        ##  Create a frame, attach a canvas and 4 buttons to this frame
        ##  Buttons are used to cleanly exit the program;
        ##  to speed up or slow down the animation, and to restart 
        ##  the animation.
        ##  Canvas, like an image, is an object that we can draw objects on.
        ##  This canvas is called chart_1.  
        ##  Parent = root window, contains a frame
        ##  The frame contains the canvas and the 4 buttons.
        ##  We only care about the canvas in our animation
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.top_frame = Frame(self.frame)
        self.top_frame.pack(side=TOP)
        self.canvas = Canvas(self.top_frame, background="white", \
                             width=self.maxx, height=self.maxy )
        self.canvas.pack()
        self.bottom_frame = Frame(self.frame)
        self.bottom_frame.pack(side=BOTTOM)
        self.restart = Button(self.bottom_frame, text="Restart", command=self.restart)
        self.restart.pack(side=LEFT)
        self.slow = Button(self.bottom_frame, text="Slower", command=self.slower)
        self.slow.pack(side=LEFT)
        self.fast = Button(self.bottom_frame, text="Faster", command=self.faster)
        self.fast.pack(side=LEFT)
        self.quit = Button(self.bottom_frame, text="Quit", command=self.quit)
        self.quit.pack(side=RIGHT)

    def faster(self):
        if self.wait_time > 2:
            self.wait_time //= 2

    def slower(self):
        self.wait_time *= 2
            
    def restart(self):
        self.isstopped = False
        self.b.x,self.b.y = 80,200
        self.animate()
        
    def quit(self):
        self.isstopped = True
        self.parent.destroy()
        
    def draw_ball(self):
        self.canvas.delete("all")
        for ball in self.balls_list:
            
            # Draw an oval on the canvas within the bounding box
            self.canvas.create_oval(ball.bounding_box(), fill=ball.color)
            self.canvas.update()   # Actually refresh the drawing on the canvas.
        
            # Pause execution.  This allows the eye to catch up
            self.canvas.after(self.wait_time)

    def animate(self):
        while not self.isstopped:
            for ball in self.balls_list:
                self.draw_ball()
                ball.x += ball.dx
                ball.y += ball.dy
                ball.check_and_reverse(self.maxx,self.maxy)


if __name__ == "__main__":
    ##  We will create a root object, which will contain all 
    ##  our user interface elements
    ##
    root = Tk()
    root.title("Tkinter: Lab 11")

    ## Create a class to handle all our animation
    bd = BallDraw(root)

    ## Run the animation by continuously drawing the ball and then moving it
    bd.animate()

    ## This is an infinite loop that allows the window to listen to
    ## "events", which are user inputs.  The only user event here is
    ## closing the window, which ends the program. 
    root.mainloop()