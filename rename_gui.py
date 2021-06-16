import os
import tkinter as tk
window = tk.Tk()

COUNT = 1


def increment():
    global COUNT
    COUNT = COUNT + 1


def start_rename(direc, name):
    os.chdir(direc)
    files = (file for file in os.listdir()
             if os.path.isfile(os.path.join(os.getcwd(), file)))

    for f in files:
        f_name, f_ext = os.path.splitext(f)
        f_name = name + \
            str(COUNT)
        increment()

        new_name = '{}{}'.format(f_name, f_ext)
        os.rename(f, new_name)


def rename_files():
    directory = ent_directory.get()
    name = ent_file_name.get()
    start_rename(direc=directory, name=name)
    global COUNT
    COUNT = 1


# Head
frm_head = tk.Frame(pady=4)
lbl_greeting = tk.Label(master=frm_head, text="Multiple File Renamer",
                        fg="#000000", bg="#eeeeee", width=60, height=1, font=("Arial", 20))
lbl_greeting.pack()

# Upper
frm_upper = tk.Frame(pady=2)
lbl_directory = tk.Label(master=frm_upper, width=60,
                         height=1, text="Enter the folder directory:")
ent_directory = tk.Entry(master=frm_upper, width=40)
lbl_directory.pack()
ent_directory.pack()

# Lower
frm_lower = tk.Frame(pady=2)
lbl_file_name = tk.Label(master=frm_lower, width=60,
                         height=1, text="Enter File Name")
ent_file_name = tk.Entry(master=frm_lower, width=40)
btn_rename = tk.Button(master=frm_lower, text="Rename",
                       width=20, height=2, command=rename_files)
lbl_eg = tk.Label(master=frm_lower, width=60,
                  height=1, text="For eg: If input Filename 'test' the files will be test1, test2 etc.")
lbl_file_name.pack()
ent_file_name.pack()
lbl_eg.pack()
btn_rename.pack()

# pack frames
frm_head.pack()
frm_upper.pack()
frm_lower.pack()

window.title("Multiple File Renamer - by Binong")
window.geometry('400x300+400+150')
window.minsize(400, 400)
window.maxsize(400, 400)
window.mainloop()
