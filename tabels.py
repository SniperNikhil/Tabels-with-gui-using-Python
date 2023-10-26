#We are Importing tkinter module for gui
from tkinter import*

#we have created a class tables in which our main code will be written
class tables:
    #this is the code for creting the window up till line no 12
    def __init__(self,root):
        self.root=root
        self.root.geometry("850x500+0+0") #this will set the window geometry
        self.root.title("Tabels Calulator") #Title of a window
        self.root.config(bg="WHITE") 
        self.root.resizable(0,0) #This will disable the resizing of window
        
        #We are creating a frame now
        TabelsFrame1=Frame(self.root,bd=8,relief=RIDGE,bg="blue")
        TabelsFrame1.place(x=6,y=6,width=410,height=470) #We have set the position of frame in widow

        #we have created a variable to store the number 
        self.var_num=IntVar()

        #This is a label
        label1=Label(TabelsFrame1,text="Enter a Number",font=("goudy old style",25,"bold"),bg="blue",fg="White")
        label1.place(x=55,y=60,width=280,height=60) #setting position of label in TabelsFrame1

        #Here we have our entry field 
        #Note that we have assigned variable to this entry field
        #using keyword textvariable
        text1=Entry(TabelsFrame1,textvariable=self.var_num,font=("goudy old style",25,"bold"),bd=4,bg="White",fg="Black",justify=CENTER)
        text1.place(x=105,y=160,width=180,height=60)

        #we have a button here
        #Note that onclick of a button We are calling a function calculate
        #This is possible using keyword command
        btn1=Button(TabelsFrame1,text="Print",command=self.calculate,font=("goudy old style",25,"bold"),bg="red")
        btn1.place(x=55,y=260,width=280,height=60) #we are setting the postion of button

        #We have created another frame where we will be displaying the table
        TabelsFrame2=Frame(self.root,bd=8,relief=RIDGE,bg="blue")
        TabelsFrame2.place(x=410,y=6,width=410,height=470)

    #on click of Print button this function will be called
    def calculate(self):
        #Here we are over riding our empty frame and adding a new frame above our TabelsFrame2
        TabelsFrame2=Frame(self.root,bd=8,relief=RIDGE,bg="blue")
        TabelsFrame2.place(x=410,y=6,width=410,height=470)

        #now we have assigned variable b with a number which we are going to use it
        #setting the position of y axis 
        #you can check on line no 53 i have assigned y=b
        b=15

        #Now we have a loop to Print tables of a number 
        for i in range(0,10): 
            #each time in loop a new label will be created and dislayed at different 
            #position
            # Now comes to login which is very easy
            # we are getting the variable from interface using the self.var_num.get()
            # And after = we are just multipling  the variable with number from 1 to 10        
            label1=Label(TabelsFrame2,text=f"{self.var_num.get()} X {i+1} = {self.var_num.get()*(i+1)}",font=("goudy old style",25,"bold"),bg="blue",fg="White")
            label1.place(x=55,y=b,width=280,height=30)

            #now each time the value of b should increase in loop
            b=b+45

#this will help us to create our window
root=Tk()
c=tables(root) #we are calling our tables class here
root.mainloop() #here the complete pgm is running continuosly so the user can intertract
                #with gui if you dont write this the pgm will run and get close immediately

#Thank You