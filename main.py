#Names:Anton Voronov 33572006, Demetrius Brown 33814841


from tkinter import *
import time
import random

class Pixel:
    color = ['black', 'white', 'yellow', 'red', 'blue', 'green', 'orange', 'purple', 'brown', 'cyan']

    def __init__(self, canvas, i, j, nrow, ncol, scale, c, vector=None):
        self.canvas = canvas
        self.i = i
        self.j = j
        self.nrow = nrow
        self.ncol = ncol
        self.scale = scale
        self.color = Pixel.color[c]
        self.vector = vector

        self.x = (j % self.ncol) * scale
        self.y = (i % self.nrow) * scale

        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + scale, self.y + scale, fill=self.color, width=1, outline="black", tags="rectangle")

    def __str__(self):
        '''
        The String method for pixel. Prints out details of the pixel.
        '''
        return f"Pixel at ({self.i}, {self.j}) with color {self.color}"

    def delete(self):
        '''
        The delete method for pixel. Deletes the rectangle corresponding to the pixel object.
        '''
        self.canvas.delete(self.rect)

    def next(self):
        '''
        The Next method for pixel. It takes the pixel object, and depending on the vector of the pixel, plots it on the canvas accordingly.
        If there is no vector, then it is plotted to the xy coodrinates of the pixel. If there is, then the new location is updated and plotted.
        '''
        if self.vector is None:
            self.canvas.coords(self.rect, self.x, self.y, self.x + self.scale, self.y + self.scale)
        else:
            new_i = self.i + self.vector[0]
            new_j = self.j + self.vector[1]

            if new_i < 0:
                new_i += self.nrow
            elif new_i >= self.nrow:
                new_i -= self.nrow
            if new_j < 0:
                new_j += self.ncol
            elif new_j >= self.ncol:
                new_j -= self.ncol

            self.i = new_i
            self.j = new_j

            self.x = self.j * self.scale
            self.y = self.i * self.scale

            self.canvas.coords(self.rect, self.x, self.y, self.x + self.scale, self.y + self.scale)

    def left(self):
        '''
        Left method. Sets the vector of the pixel object to the left direction
        '''
        self.vector = [0, -1]

    def right(self):
        '''
        Right method. Sets the vector of the pixel object to the right direction
        '''
        self.vector = [0, 1]

    def up(self):
        '''
        Up method. Sets the vector of the pixel object to the upward direction
        '''
        self.vector = [-1, 0]

    def down(self):
        '''
        Down method. Sets the vector of the pixel object to the downward direction
        '''
        self.vector = [1, 0]

    def stop(self):
        '''
        Stop method. Sets the vector of the pixel object to None
        '''
        self.vector = None





        
#################################################################
########## TESTING FUNCTION
#################################################################
def delete_all(canvas):
    canvas.delete("all")
    print("Delete All")


def test1(canvas,nrow,ncol,scale):
    print("Generate 10 points at random")
    random.seed(4) # for reproducibility
    for k in range(10):
        i=random.randint(0,nrow-1) 
        j=random.randint(0,ncol-1)
        c=random.randint(1,9)    # color number
        pix=Pixel(canvas,i,j,nrow,ncol,scale,c)
        print(pix)

def test2(canvas,nrow,ncol,scale):
    print("Generate 10 points at random (using modulo)")
    random.seed(5) # for reproducibility
    for k in range(10):
        i=random.randint(0,nrow-1)*34
        j=random.randint(0,ncol-1)*13
        ij=str(i)+","+str(j)
        c=random.randint(1,9)    # color number
        pix=Pixel(canvas,i,j,nrow,ncol,scale,c)
        print(ij,"->",pix)

        
def test3(root,canvas,nrow,ncol,scale):
    print("Move one point along a square")

    pix=Pixel(canvas,35,35,nrow,ncol,scale,3)
    pix.vector=[-1,0] # set up direction (up)
    for i in range(30):
        pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)
        
    pix.vector=[0,-1] # set up new direction (left)
    for i in range(30):
        pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)
        
    pix.vector=[1,0]   # set up new direction (down)
    for i in range(30):
        pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)
        
    pix.vector=[0,1]    # set up new direction (right)
    for i in range(30):
        pix.next()       # next move in the simulation 
        root.update()    # update the graphic
        time.sleep(0.05) # wait in second (simulation)

    #delete point
    pix.delete()


  
def test4(root,canvas,nrow,ncol,scale):
    print("Move four point along a square")

    pixs=[]
    pixs.append(Pixel(canvas,35,35,nrow,ncol,scale,3,[-1,0]))
    pixs.append(Pixel(canvas,5,35,nrow,ncol,scale,4,[0,-1]))
    pixs.append(Pixel(canvas,5,5,nrow,ncol,scale,5,[1,0]))
    pixs.append(Pixel(canvas,35,5,nrow,ncol,scale,6,[0,1]))
    
    print("Starting coords")
    for p in pixs: print(p)

    for i in range(30):
        for p in pixs:
            p.next()       # next move in the simulation     
        root.update()      # update the graphic
        time.sleep(0.05)   # wait in second (simulation)

    print("Ending coords")
    for p in pixs:
        print(p)
        p.delete()


        
def test5(root,canvas,nrow,ncol,scale):
    print("Move one point any direction -use arrow commands")

    pix=Pixel(canvas,20,20,nrow,ncol,scale,2)

    ### binding used by test5
    root.bind("<Right>",lambda e:pix.right())
    root.bind("<Left>",lambda e:pix.left())
    root.bind("<Up>",lambda e:pix.up())
    root.bind("<Down>",lambda e:pix.down())

    ### simulation
    while True:
        pix.next()
        root.update()     # update the graphic
        time.sleep(0.05)  # wait in second (simulation)



        

###################################################
#################### Main method ##################
###################################################


def main():
       
        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        nrow=40
        ncol=40
        scale=15
        canvas = Canvas(root,width=ncol*scale,height=nrow*scale,bg="black") # create a canvas width*height
        canvas.pack()


        ### general binding events to choose a testing function
        root.bind("1",lambda e:test1(canvas,nrow,ncol,scale))
        root.bind("2",lambda e:test2(canvas,nrow,ncol,scale))
        root.bind("3",lambda e:test3(root,canvas,nrow,ncol,scale))
        root.bind("4",lambda e:test4(root,canvas,nrow,ncol,scale))
        root.bind("5",lambda e:test5(root,canvas,nrow,ncol,scale))
        root.bind("<d>",lambda e:delete_all(canvas))
        
       
        
        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()

