from tkinter import *
import bcrypt

def validate(password):
    #the following doesn't work, try to fix it later
    # password = b"thisispassword"
    # hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    hashed = b'$2b$12$HWvuYn.zqi/YAxHgR1mVxe9ULOUjuOa9HZxrilYXrCR2dPYkCaa8m'
    password = bytes(password,encoding='utf-8')
    if bcrypt.checkpw(password,hashed):
        print('Login successful')
    else:
        print('Invalid password')

root = Tk()
root.title("Password Validator")
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()
password_entry.get()
button = Button(text="validate",command=lambda:validate(password_entry.get()))
button.pack()

root.mainloop()

# #the window
# from tkinter import *
# root = Tk()
# root.title("Password Validator")
# root.geometry("300x300")
# root.mainloop()