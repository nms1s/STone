from tkinter import *


allow_entry = False


def mainlogin():
    # ROOT
    global root
    root = Tk()
    root.title("Login")
    root.geometry("240x110")
    root.protocol("WM_DELETE_WINDOW", disable_event)
    root.resizable(width=False, height=False)

    # login creditentials
    my_username = 'm'
    my_password = 'm'

    # FUNCTIONS

    def login(event=None):
        global allow_entry
        if my_username == username.get() and my_password == pswd.get():
            allow_entry = True
            root.destroy()
        else:
            allow_entry = False
            wrong_input = Label(root, text="Wrong username or password!")
            wrong_input.pack(padx=5, pady=5)

    root.bind("<Return>", login)
    # WIDGETS

    # Login entry widgets
    username = Entry(root)
    username.pack(padx=5, pady=5)
    username.focus_set()
    pswd = Entry(root, show="*")
    pswd.pack(padx=5, pady=5)

    # BUTTONS

    login_button = Button(root, text="Login", command=login)
    login_button.pack()

    ### MAIN LOOP ###
    root.mainloop()


# def quit_login():
#     global allow_entry
#     allow_entry = False
#     root.destroy()


def disable_event():
    pass


### NAME == MAIN ###

if __name__ == "__main__":
    mainlogin()
