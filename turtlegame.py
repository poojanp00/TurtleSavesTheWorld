# Poojan Patel patel709

# I understand this is a graded, individual examination that may not be
# discussed with anyone.  I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work and that none of
# it was obtained from any source other than material presented as part of the
# course.


# Completed Task 1 through 8, as well as extra credit task 10. Attempted and partially completed task 9.

from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
import datetime

screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500

class LaserBeam(RawTurtle):
    def __init__(self,canvas,x,y,direction,dx,dy):
        super().__init__(canvas)
        self.penup()
        self.goto(x,y)
        self.setheading(direction)
        self.color("Green")
        self.__lifespan = 200
        # self.__dx and self.__dy equations given to us by our wonderful professor :)
        self.__dx = math.cos(math.radians(direction)) * 2 + dx
        self.__dy = math.sin(math.radians(direction)) * 2 + dy
        #Task 9: if the direction is straight up or straight down the laser will not move diagonally, but vertically up or down.
        if direction == 90:
            self.__dx = 0
            self.__dy = 2
        if direction == 270:
            self.__dx = 0
            self.__dy = -2
        self.shape("laser")

    # The following move function is neraly identical to the move functions of the ghost and tiny the turtle. This function additionally decreases the laser lifespan by 1.
    def moveLaser(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        x = (self.__dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.__dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY

        self.goto(x,y)
        self.__lifespan -= 1

    # The following functions create accessor functions to get the lifespan, dy, dx, and Radius values
    def get_lifespan(self):
        return self.__lifespan
    def get_dx(self):
        return self.__dx
    def get_dy(self):
        return self.__dy
    def getRadius(self):
        return 4




class Ghost(RawTurtle):
    def __init__(self,canvasobj,dx,dy,x,y,size):
        # Within this constructor, I have added .__ to the attributes to make them private
        RawTurtle.__init__(self,canvasobj)
        self.penup()
        self.goto(x,y)
        self.__dx = dx
        self.__dy = dy
        self.__size = size
        if self.__size==3:
            self.shape("blueghost.gif")
        elif self.__size==2:
            self.shape("pinkghost.gif")

    #Moves the ghost from its current position to a new position
    def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        x = (self.__dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.__dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY

        self.goto(x,y)

    #returns the apprximate "radius" of the Ghost object
    def getRadius(self):
        return self.__size * 10 - 5

    # The following four functions create 2 accessor and 2 mutator functions to
    # get the dy,dx values and set the dy,dx values to new values, respectively.
    def get_dx(self):
        return self.__dx
    def get_dy(self):
        return self.__dy
    def set_dx(self):
        self.__dx = dx
    def set_dy(self):
        self.__dy = dy

class FlyingTurtle(RawTurtle):
    def __init__(self,canvasobj,dx,dy,x,y, size):
        # Within this constructor, I have added .__ to the attributes to make them private
        RawTurtle.__init__(self,canvasobj)
        self.penup()
        self.color("purple")
        self.goto(x,y)
        self.__dx = dx
        self.__dy = dy
        self.__size = size
        self.shape("turtle")

    def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        x = (self.__dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.__dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY

        self.goto(x,y)

    def turboBoost(self):
        angle = self.heading()
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))
        self.__dx = self.__dx + x
        self.__dy = self.__dy + y

    def stopTurtle(self):
        angle = self.heading()
        self.__dx = 0
        self.__dy = 0


    def getRadius(self):
        return 2

    # The following four functions create 2 accessor and 2 mutator functions to
    # get the dy,dx values and set the dy,dx values to new values, respectively.
    def get_dx(self):
        return self.__dx
    def get_dy(self):
        return self.__dy
    def set_dx(self):
        self.__dx = dx
    def set_dy(self):
        self.__dy = dy

# intersect function uses the current positioning of both objects and checks to see if the distance is less that the sum of the radii, returns bool value
def intersect(obj1, obj2):
    x1 = obj1.xcor()
    y1 = obj1.ycor()
    x2 = obj2.xcor()
    y2 = obj2.ycor()
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    sum_of_radii = obj1.getRadius() + obj2.getRadius()
    if distance <= sum_of_radii:
        return True


def main():

    # Start by creating a RawTurtle object for the window.
    firstwindow = tkinter.Tk()
    firstwindow.title("Turtle Saves the World!")
    canvas = ScrolledCanvas(firstwindow,600,600,600,600)
    canvas.pack(side = tkinter.LEFT)
    t = RawTurtle(canvas)

    screen = t.getscreen()
    screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
    screen.register_shape("blueghost.gif")
    screen.register_shape("pinkghost.gif")
    screen.register_shape("laser",((-2,-4),(-2,4),(2,4),(2,-4)))
    frame = tkinter.Frame(firstwindow)
    frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
    scoreVal = tkinter.StringVar()
    scoreVal.set("0")
    scoreTitle = tkinter.Label(frame,text="Score")
    scoreTitle.pack()
    scoreFrame = tkinter.Frame(frame,height=2,bd=1,relief=tkinter.SUNKEN)
    scoreFrame.pack()
    score = tkinter.Label(scoreFrame,height=2, width=20,textvariable=scoreVal,fg="yellow",bg="black")
    score.pack()

    livesTitle = tkinter.Label(frame, text="Extra Lives Remaining")
    livesTitle.pack()
    livesFrame = tkinter.Frame(frame,height=30,width=60,relief=tkinter.SUNKEN)
    livesFrame.pack()
    livesCanvas = ScrolledCanvas(livesFrame,150,40,150,40)
    livesCanvas.pack()
    livesTurtle = RawTurtle(livesCanvas)
    livesTurtle.ht()
    livesScreen = livesTurtle.getscreen()
    life1 = FlyingTurtle(livesCanvas,0,0,-35,0,0)
    life2 = FlyingTurtle(livesCanvas,0,0,0,0,0)
    life3 = FlyingTurtle(livesCanvas,0,0,35,0,0)
    lives = [life1, life2, life3]
    t.ht()

    screen.tracer(10)

    #Tiny Turtle!
    flyingturtle = FlyingTurtle(canvas,0,0,(screenMaxX-screenMinX)/2+screenMinX,(screenMaxY-screenMinY)/2 + screenMinY,3)

    #A list to keep track of all the ghosts
    ghosts = []

    #Lists to keep track of all the active & dead lasers
    lasers = []

    #Create some ghosts and randomly place them around the screen
    for numofghosts in range(6):
        dx = random.random()*6 - 4
        dy = random.random()*6 - 4
        x = random.random() * (screenMaxX - screenMinX) + screenMinX
        y = random.random() * (screenMaxY - screenMinY) + screenMinY
        ghost = Ghost(canvas,dx,dy,x,y,3)
        ghosts.append(ghost)

    def play():
        #start counting time for the play function
        ##LEAVE THIS AT BEGINNING OF play()
        hitghosts = []

        start = datetime.datetime.now()

        # The following if statement checks to see if there are no more active ghosts in the list. If the length of the list of active ghosts is 0, the user wins and a congratulatory msg is displayed.
        if len(ghosts) == 0:
            tkinter.messagebox.showinfo("You Win!!", "You saved the world!")
            return

        # Move the turtle
        flyingturtle.move()

        deadlasers = []
        for laser in lasers:
            # This for loop will move the laser using the method created in the LaserBeam class. Once the lifespan reaches 0, the laser is removed from the list of active lasers and removed.
            laser.moveLaser()
            if laser.get_lifespan() == 0:
                deadlasers.append(laser)
                lasers.remove(laser)
                for deadlaser in deadlasers:
                    deadlaser.goto(-screenMinX*2, -screenMinY*2)
                    deadlaser.ht()
                    deadlasers.remove(deadlaser)

        #Move the ghosts
        for each_ghost in ghosts:
            each_ghost.move()

        # Checks if a laser intersects with a ghost
        for each_ghost in ghosts:
            for laser in lasers:
                if intersect(laser, each_ghost) ==  True:
                    each_ghost.ht()
                    hitghosts.append(each_ghost)
                    lasers.remove(laser)
                    laser.ht()
                    deadlasers.append(laser)
                    if each_ghost.getRadius() == 25:
                        # The following lines add 20 points to the total score if they hit a blue ghost
                        temp = int(scoreVal.get())
                        temp+=20
                        scoreVal.set(str(temp))
                        count = 0
                        dx = random.random()*6 - 4
                        dy = random.random()*6  - 4
                        for numofghosts in range(2):
                            if count == 0:
                                x = each_ghost.xcor()
                                y = each_ghost.ycor()
                                ghost = Ghost(canvas,dx,dy,x,y,2)
                            else:
                                x = each_ghost.xcor()
                                y = each_ghost.ycor()
                                ghost = Ghost(canvas,-dx,-dy,x,y,2)
                            count += 1
                            ghosts.append(ghost)
                    else:
                        # The following lines add 20 points to the total score if they hit a pink ghost
                        temp = int(scoreVal.get())
                        temp+=30
                        scoreVal.set(str(temp))
                    ghosts.remove(each_ghost)

        # Checks if tiny intersects with a ghost
        for each_ghost in ghosts:
            # Checks to see if intersect function returns True, if it does, the ghost is removed from list of active ghosts and hidden. The laser that hits it is also removed.
            if intersect(each_ghost,flyingturtle) ==  True:
                # The following if statements hide the respective life that tiny loses, based on the number of lives tiny has left. If the length of the list of lives is zero, the game is terminated and the user loses.
                if len(lives) == 3:
                    life3.ht()
                if len(lives) == 2:
                    life2.ht()
                if len(lives) == 1:
                    life1.ht()
                ghosts.remove(each_ghost)
                hitghosts.append(each_ghost)
                each_ghost.ht()
                if each_ghost.getRadius() == 25:
                    count = 0
                    dx = random.random()*6 - 4
                    dy = random.random()*6  - 4
                    for numofghosts in range(2):
                        if count == 0:
                            x = each_ghost.xcor()+40
                            y = each_ghost.ycor()
                            ghost = Ghost(canvas,dx,dy,x,y,2)
                        else:
                            x = each_ghost.xcor()-40
                            y = each_ghost.ycor()
                            ghost = Ghost(canvas,-dx,-dy,x,y,2)
                        count += 1
                        ghosts.append(ghost)
                lives.pop()
                tkinter.messagebox.showwarning( "Uh-Oh","You Lost a Life!")
                if len(lives) == 0:
                    tkinter.messagebox.showinfo("Uh-Oh!!", "You lost all your lives!")
                    return

        #stop counting time for the play function
        ##LEAVE THIS AT END OF ALL CODE IN play()
        end = datetime.datetime.now()
        duration = end - start

        millis = duration.microseconds / 1000.0

        # Set the timer to go off again
        screen.ontimer(play,int(10-millis))


    # Set the timer to go off the first time in 5 milliseconds
    screen.ontimer(play, 5)

    #Turn turtle 7 degrees to the left
    def turnLeft():
        flyingturtle.setheading(flyingturtle.heading()+7)

    #Turn turtle 7 degrees to the right, opposite or turnLeft function
    def turnRight():
        flyingturtle.setheading(flyingturtle.heading()-7)

    #turboBoost turtle
    def forward():
        flyingturtle.turboBoost()

    #stop Turtle
    def stop():
        flyingturtle.stopTurtle()

    # Fire laser
    def fireLaser():
        laserbeam = LaserBeam(canvas,flyingturtle.xcor(),flyingturtle.ycor(), flyingturtle.heading(),flyingturtle.get_dx(), flyingturtle.get_dy())
        lasers.append(laserbeam)


    #Call functions above when pressing relevant keys
    screen.onkeypress(turnLeft,"Left")
    screen.onkeypress(forward,"Up")
    screen.onkeypress(stop, "Down")
    screen.onkeypress(turnRight,"Right")
    screen.onkeypress(fireLaser,"")

    screen.listen()
    tkinter.mainloop()

if __name__ == "__main__":
    main()
