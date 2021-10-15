from tkinter import *
import random
root= Tk()
root.geometry("600x150")
root.title("Password Generator")
root.configure(bg= "cyan")
passstr= StringVar()
passlen= IntVar()
passlen.set(8)
def Setup():
    global length, passstr
    def generate():
        global length, passstr
        pass1= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                '9', '0', '`', '!', '@', '#', '$', '%', '^', '&',
                '*', '(', ')']
        password = ""
        for x in range(passlen.get()):
            password = password + random.choice(pass1)
        passstr.set(password)
    def save():
        random_password = passstr.get()
        f= open("pypassw.txt", "a")
        f.write(random_password)
        f.write("\n")
        f.close()
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
def reset():
    global length, passstr
    length.delete(0, END)
    passstr.set("")
reset_btn= Button(root, text= "reset", width= 12, bg= "light gray", fg= "red", font= "courier", command= reset)
reset_btn.place(x= 450, y= 25)
Setup()
mainloop()


















"""
import random
import time
import sys

#def setup():
names= str(input("Please enter your full name: ")).split(" ")
if not(len(names)> 1):
    print("Sorry, please input your full name.\n")
else:
    first_letter= names[0][0]
    three_letters_surname= names[-1][-1]
    number= '{:03d}'.format(random.randrange(1, 999))
    username= (first_letter+ three_letters_surname+ number)
    time.sleep(1)
    print("\nYour username is: \n            "+ username)
"""
