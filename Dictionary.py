from tkinter import *

root = Tk()
root.title("Dictionary")
root.geometry("600x400")
root.configure(bg = "turquoise1")

label_of_mutable = Label(root, bg = "SpringGreen2" )
label_of_immutable = Label(root , bg = "yellow")
label_of_tkinter = Label(root, bg = "maroon1")

dictionary = {'Mutable' : 'Values Can Be Changed Just LIke A List',
              'Immutable' : 'Values Can Not Be Changed Like A Tuple',
              'Tkinter' : 'It Is The GUI Library Of Python'}

def mutable():
    label_of_mutable ["text"] = dictionary['Mutable']
    
def immutable():
    label_of_immutable ["text"] = dictionary['Immutable']

def tkinter():
    label_of_tkinter ["text"] = dictionary['Tkinter']
    
button_mutable = Button(root, text =" Meaning Of Mutable", command = mutable)
button_mutable.place(relx = 0.5, rely = 0.2, anchor = CENTER)

label_of_mutable.place(relx = 0.5, rely = 0.3, anchor = CENTER)

button_immutable = Button(root, text = "Meaning Of Immutable", command = immutable)
button_immutable.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label_of_immutable.place(relx = 0.5, rely = 0.5, anchor = CENTER)

button_tkinter = Button(root, text = "Meaning Of Tkinter", command = tkinter)
button_tkinter.place(relx = 0.5, rely = 0.6, anchor = CENTER)

label_of_tkinter.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()