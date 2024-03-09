#Initialize Tkinter
from tkinter import *

#Create new root instance
root = Tk()

root.title("Tony's Pizzeria")

root.geometry("300x300")
root.resizable(False, False)

#Initialize value for global use
itemCost= 0

def openMenu():
     
    #Creates and displays new window
    newWindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    newWindow.geometry("200x200")

    #Creates and displays buttons and labels for second window
    spec = Label(newWindow,text="Choose an option:")
    spec.pack()
    
    pepp = Button(newWindow, text="Large Pepperoni: $13.00",command=addOption1)
    pepp.pack()

    saug = Button(newWindow, text="Large Sausage: $12.00",command=addOption2)
    saug.pack()

    bread = Button(newWindow, text="12 pack breadsticks: $6.00",command=addOption3)
    bread.pack()

    exitBt = Button(newWindow, text="Previous screen", command=newWindow.destroy).pack()

#Takes global itemCost, adds a value to it, and displays a popup with a running total
def addOption1():
    global itemCost
    itemCost += 13
    new = "Your new total is: ",str(itemCost)
    popup=Toplevel(root)
    msg = Label(popup, text=new).pack()
    
#Takes global itemCost, adds a value to it, and displays a popup with a running total    
def addOption2():
    global itemCost
    itemCost += 12
    new = "Your new total is: ",str(itemCost)
    popup=Toplevel(root)
    msg = Label(popup, text=new).pack()
    
#Takes global itemCost, adds a value to it, and displays a popup with a running total
def addOption3():
    global itemCost
    itemCost += 6
    new = "Your new total is: ",str(itemCost)
    popup=Toplevel(root)
    msg = Label(popup, text=new).pack() 

#Opens a popup with a message and resets itemCost to zero
def finishOrder():
    
    # Toplevel object which will 
    # be treated as a new window
    newWindow2 = Toplevel(root)
    #Call global variable, as well as set an intermediate for display
    global itemCost
    totalCost=itemCost

#Test for no Menu input
    if itemCost == 0:
        msg= Label(newWindow2, text="Please select at least one item.").pack()

#Displays final message with total, reset global itemCost
    finish = "Thanks for ordering! Your final total is: ",str(totalCost)
    msg= Label(newWindow2, text=finish).pack()
    itemCost=0


 
#Creates and displays GUI for first window
welcome = Label(root, text="Welcome to Tony's Pizzeria!")
welcome.grid(row=0, columnspan=2)

img = PhotoImage(file=r"C:\Users\Ethan\Downloads\output-onlinepngtools.png")
bg= Label(root,image=img).grid(row=1,column=0)

menu = Button(root, text="Menu", command=openMenu)
menu.grid(row=2, column=0)

order = Button(root, text="Order", command=finishOrder)
order.grid(row=2,column=1)

#Sets infinte loop
root.mainloop()

