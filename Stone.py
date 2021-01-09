from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from datetime import date
import login


# LOGIN
# login.mainlogin()


# ROOT
root = Tk()
root.title("STone")
root.geometry("480x270")
root.eval('tk::PlaceWindow . center')


# FUNCTIONS
saved_text = ''
todays_date = date.today()


def new_entry():
    if str(textbox.get(1.0, END)) != saved_text and str(textbox.get(1.0, END)) != "\n":
        # save_yesno = messagebox.askquestion(
        #     'New Entry', 'Would you like to save before creating a new entry?', icon='warning')
        # if save_yesno == 'yes':
        save_entry()
        textbox.delete(1.0, END)
    else:
        messagebox.showinfo("New Entry", "Your entry has been updated")
        textbox.delete(1.0, END)


def save_entry():
    save_yesno = messagebox.askquestion(
        'Save Entry', 'Would you like to save the entry?', icon='warning')
    if save_yesno == 'yes':
        f = open('C:/Users/Mesrop Simonyan/Desktop/test.txt', "a")
        date = new_day()
        text2save = str(textbox.get(1.0, END))
        global saved_text
        saved_text = text2save
        f.write(date + 61 * "-" + '\n\n' + text2save + '\n\n')
        f.close()


def save_entry_as_file():

    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    text2save = str(textbox.get(1.0, END))
    global saved_text
    saved_text = text2save
    f.write(str(todays_date) + ' ' + 50*"_" +
            '\n\n' + text2save + '\n\n')
    f.close()


# def open_file():
#     f = filedialog.askopenfile()


# def comment():
    # ...


def exit_journal():
    exit_yesno = messagebox.askquestion(
        'Exit', 'Are you sure you want to exit STone?', icon='warning')
    if exit_yesno == 'yes':
        save_entry()
    root.destroy()


def new_day():
    f = open('C:/Users/Mesrop Simonyan/Desktop/test.txt', "r")
    if str(todays_date) not in f.read():
        date = str(todays_date) + " " + 50*"_" + '\n'
    else:
        date = ""
    f.close()
    return date
    # if todays_date not in the file
    # add date

# WIDGETS


# Main Frame
master_frame = Frame(root)
master_frame.pack(padx=5, pady=5)

# MENU
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New Entry", command=new_entry)
file_menu.add_command(label="Save Entry", command=save_entry)
file_menu.add_command(label="Save Entry As File", command=save_entry_as_file)
#file_menu.add_command(label="Open", command=open_file)
# file_menu.add_command(label="Add Comment", command=comment)
file_menu.add_command(label="Exit", command=exit_journal)

# Initial Entry
textbox = Text(root, width=1920, height=1080)
textbox.pack(padx=5, pady=5)


### MAIN LOOP ###
root.mainloop()


# TODO
# AUTO SAVE
# SAVE AS TXT FILE
# SEPARATE COMMENT SECTION
# FILE LOAD
# ASK IF COMMENT NEEDS TO BE ADDED BEFORE CLOSING (CHECK TO NOT SEE THIS AGAIN)
# ONLY PASSWORD ACCESS
