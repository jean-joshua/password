from tkinter import *
import random

root = Tk()
root.title("Password Generator")
root.geometry("400x400")

e = Entry(root)
e.place(relx=0.5, rely=0.3, anchor=CENTER)

label = Label(root)
label.place(relx=0.5, rely=0.4, anchor=CENTER)
lebel1 = Label(root)

#label2 = Label(root) # experiment

array_3d = [[['I','J','K','L','M','N','O','P'],['King','Queen'],['!','@','#','$','%','^','&','*',]]]

def new_password():
    random_no_1 = random.randint(0,5)
    random_no_2 = random.randint(0,1)
    random_no_3 = random.randint(0,7)

    letter1 = str(array_3d[0][0][random_no_1])
    letter2 = (array_3d[0][1][random_no_2])
    letter3 = (array_3d[0][2][random_no_3])
    #letter_all = str(letter1) + str(letter2) + str(letter3) #experiment
    label['text'] = "Guessed Password : " + letter1 + "" + letter2 + "" + letter3

    #if e.get() == letter_all: #experiment
        #label2['text'] = "You Won!"
    #else:
        #label2['text'] = "Get Good!"


btn = Button(root, text="new password", command=new_password)
btn.place(relx=0.5, rely=0.6, anchor=CENTER)

label1.place(relx=0.5, rely=0.6, anchor=CENTER)
#label2.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()