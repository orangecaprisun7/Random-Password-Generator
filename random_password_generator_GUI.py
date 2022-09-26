# random password Generator
# written by Kurtis Norman 02/07/2021

# uses the tkinter module for the GUI and imports all aspects of this to the code
from tkinter import *
# uses the random function to make the passwords
import random
# naming the gui 'root' and setting the size and colour
root= Tk()
root.geometry("600x150")
root.title("Password Generator")
root.configure(bg= "cyan")
# making variables for the password and setting default length as 8
passstr= StringVar()
passlen= IntVar()
passlen.set(8)
# defining a function that allows the code to reset itself when generating a new password
def Setup():
    # makes these 2 variables able to be modified to change password outcome
    global length, passstr
    # defining a function to generate the password
    def generate():
        global length, passstr
        # making an array for all characters used in the passwords
        pass1= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                '9', '0', '`', '!', '@', '#', '$', '%', '^', '&',
                '*', '(', ')', '_', '-']
        # sets password variable to blank
        password = ""
        # takes what user enters for password length and randomly chooses x amount of characters from array
        for x in range(passlen.get()):
            password = password + random.choice(pass1)
        # this then sets that amount of random characters as the password
        passstr.set(password)
    # definfng a function that gets the generated password and saves it in a text document
    def save():
        random_password = passstr.get()
        f= open("pypassw.txt", "a")
        f.write(random_password)
        f.write("\n")
        f.close()
    # this is creating all the buttons, labels and entry boxes using the tkinter module
    pass_label= Label(root, text="Enter password length:", bg= "light gray", font= "courier 14 bold")
    pass_label.place(x= 10, y= 30)
    length=Entry(root, textvariable= passlen)
    length.place(x= 270, y= 30, height= 25, width= 150)
    gen_passbtn= Button(root, text="Generate Password", bg= "light gray", font= "courier 14", command=generate)
    gen_passbtn.place(x= 10, y= 65)
    gen_passentry= Entry(root, textvariable=passstr)
    gen_passentry.place(x= 270, y= 70, height= 25, width= 150)
    save_btn= Button(root, text="save", font= "courier", width= 12, bg= "light gray", fg= "green", command=save)
    save_btn.place(x= 450, y= 70)
# defining a function that allows the user to clear the generated passsword and make another
def reset():
    global length, passstr
    length.delete(0, END)
    passstr.set("")
# creates a button for resetting password
reset_btn= Button(root, text= "reset", width= 12, bg= "light gray", fg= "red", font= "courier", command= reset)
reset_btn.place(x= 450, y= 25)
# this allows the code to loop by recalling its function
Setup()
# this allows the tkinter gui to loop by recalling its function
mainloop()
