import os
import tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import Pyro4
import pymysql
from tkinter import Label, Entry, Button
import hashlib

# Connect to the P2P server
p2p_server = Pyro4.Proxy("PYRONAME:p2p_server")

main = tkinter.Tk()
main.title("Distributed File System") 
main.maxsize(width=500 ,  height=300)
main.minsize(width=500 ,  height=300)

#Below are the functions for performing CRUD operations(Create, Read, Update, Delete)
#function to add a file.
def add_file():
    filename = filedialog.askopenfilename()
    if filename:
        with open(filename, 'rb') as file:
            content = file.read()
            result = p2p_server.add_file(os.path.basename(filename), content)
            status_label.config(text=result)
            update_file_list()

#Function to Delete a File from the server
def delete_file():
    
    selected_item = file_list.selection()
    if selected_item:
        filename = file_list.item(selected_item, 'text')
        result = p2p_server.delete_file(filename)
        status_label.config(text=result)
        update_file_list()

def write_file():
    selected_item = file_list.selection()
    if selected_item:
        filename = file_list.item(selected_item, 'text')
        content = p2p_server.restore_file(filename)
        if content:
            with open(filename, 'wb') as file:
                file.write(content)
            status_label.config(text=f"File '{filename}' written to disk.")
        else:
            status_label.config(text=f"File '{filename}' not found on the server.")
    else:
        status_label.config(text="Select a file to write.")

# To Create a new Directory
def create_directory():
    pass

# To Create a new File
def create_file():
    pass

# To Restore File
def recycle():
    pass
# TO Read the File.
def read_files():
    pass

def rename_file():
    pass

def share_access():
    pass

def update_file_list():
    file_list.delete(*file_list.get_children())
    for filename in p2p_server.file_storage.keys():
        file_list.insert('', 'end', text=filename)

def validate_login():
    global login_user, login_pass, username, available_files

    user = login_user.get()
    password = login_pass.get()

    if not user or not password:
        messagebox.showinfo("Input Error", "Please enter both username and password")
        return
    hashed_password = hash_password(password)

    try:
        con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='Sathvik@007', database='distributed', charset='utf8')
    except pymysql.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return

    try:
        with con:
            cur = con.cursor()
            cur.execute("SELECT username, password FROM register")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == user and row[1] == hashed_password:
                    login_success()
                    break
            else:
                login_failure()
    except pymysql.Error as e:
        messagebox.showerror("Database Error", f"Error querying the database: {e}")
    finally:
        if con:
            con.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_success():
    global username
    username = login_user.get()
    read_files()
    winlogin.destroy()
    file_system()

def login_failure():
    messagebox.showerror("Login Failed", "Invalid username or password. Please retry.")


def file_system():
    # Implement your logic for the file system window here
    global username, text, available_files, filecombo, accessList

    filesystem = tk.Tk()
    filesystem.title("Distributed File System Client Screen")
    filesystem.geometry("1300x900")
    font1 = ('times', 13, 'bold')

    cd_button = tk.Button(filesystem, text="Create Directory", command=create_directory)
    cd_button.place(x=50, y=100)
    cd_button.config(font=font1)

    cf_button = tk.Button(filesystem, text="Create File", command=create_file)
    cf_button.place(x=300, y=100)
    cf_button.config(font=font1)

    filecombo = ttk.Combobox(filesystem, values=available_files)
    filecombo.place(x=50, y=150)
    filecombo.set(available_files[0] if available_files else "")
    filecombo.config(font=font1)

    df_button = tk.Button(filesystem, text="Delete File", command=delete_file)
    df_button.place(x=300, y=150)
    df_button.config(font=font1)

    restore_button = tk.Button(filesystem, text="Restore File", command=recycle)
    restore_button.place(x=500, y=150)
    restore_button.config(font=font1)

    rf_button = tk.Button(filesystem, text="Read File", command=read_files)
    rf_button.place(x=50, y=200)
    rf_button.config(font=font1)

    wf_button = tk.Button(filesystem, text="Write File", command=write_file)
    wf_button.place(x=300, y=200)
    wf_button.config(font=font1)

    ren_button = tk.Button(filesystem, text="Rename File", command=rename_file)
    ren_button.place(x=50, y=250)
    ren_button.config(font=font1)

    sa_button = tk.Button(filesystem, text="Share Access", command=share_access)
    sa_button.place(x=300, y=250)
    sa_button.config(font=font1)

    access_list = ttk.Combobox(filesystem, values=['Read', 'Write'])
    access_list.place(x=450, y=250)
    access_list.set('Read')
    access_list.config(font=font1)

    text = tk.Text(filesystem, height=15, width=120)
    scroll = tk.Scrollbar(text)
    text.configure(yscrollcommand=scroll.set)
    text.place(x=10, y=300)
    text.config(font=font1)

    filesystem.config(bg='chocolate1')
    filesystem.mainloop()


# Global variables
global login_user, login_pass, username, available_files
available_files = []

# Your existing code for creating the login window
# ...

# Example of creating a login button
login_button = Button(winlogin, text="Submit", command=validate_login)
login_button.place(x=100, y=180)
login_button.config(font=font1)

# Your existing code for running the Tkinter main loop
winlogin.mainloop()

def signup_Action():
    global sign_user, sign_password, contact, username, count, winsignup
    user = sign_user.get()
    password = sign_password.get()
    contact_number = contact.get()

    output = "none"
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'Sathvik@007', database = 'distributed',charset='utf8')
    try:
        con = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Sathvik@007',
            database='distributed',
            charset='utf8'
        )
        with con:
            cur = con.cursor()
            cur.execute("SELECT username FROM register")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == user:
                    output = user + " Username already exists"
                    break
            if output == "none":
                # No need to create a separate connection and cursor again
                student_sql_query = f"INSERT INTO register(username, password, contact) VALUES('{usr}', '{password}', '{contactno}')"
                cur.execute(student_sql_query)
                con.commit()

                if cur.rowcount == 1:
                    output = "Signup process completed. You can log in now"
                    count = 2
                    messagebox.showinfo("Success", output)
                    winsignup.destroy()
                    login_Function()
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Database error: {e}")
    finally:
        # Close the connection outside the try-except block
        if con:
            con.close()

    # Move the messagebox.showinfo outside the with block
    if output != "none":
        messagebox.showinfo("Info", output)

def login_Function():
    global login_user, login_pass, count, winlogin
    if count == 0:
        main.destroy()
        count = 1
    winlogin = tkinter.Tk()
    winlogin.title("User Login Screen")
    winlogin.maxsize(width=500, height=300)
    winlogin.minsize(width=500, height=300)

    l1 = Label(winlogin, text='Login Screen')
    l1.config(font=font1)
    l1.place(x=140,y=30)

    l2 = Label(winlogin, text='Username')
    l2.config(font=font1)
    l2.place(x=50,y=80)

    login_user = Entry(winlogin,width=35)
    login_user.config(font=font1)
    login_user.place(x=150,y=80)

    l3 = Label(winlogin, text='Password')
    l3.config(font=font1)
    l3.place(x=50,y=130)

    login_pass = Entry(winlogin,width=35, show="*")
    login_pass.config(font=font1)
    login_pass.place(x=150,y=130)

    login1Button = Button(winlogin, text="Submit", command=validate_login)
    login1Button.place(x=100,y=180)
    login1Button.config(font=font1)

    winlogin.mainloop()

def validate_login():


font1 = ('times', 12, 'bold')


root = tk.Tk()
root.title("P2P File System")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Add File Button
add_button = ttk.Button(main_frame, text="Add File", command=add_file)
add_button.grid(column=1, row=1, sticky=tk.W)

# Delete File Button
delete_button = ttk.Button(main_frame, text="Delete File", command=delete_file)
delete_button.grid(column=2, row=1, sticky=tk.W)

# Write File Button
write_button = ttk.Button(main_frame, text="Write File", command=write_file)
write_button.grid(column=3, row=1, sticky=tk.W)

# Status Label
status_label = ttk.Label(main_frame, text="")
status_label.grid(column=1, row=2, columnspan=3, sticky=(tk.W, tk.E))

# File List
file_list = ttk.Treeview(main_frame, columns=("Filename"))
file_list.heading("#1", text="Filename")
file_list.grid(column=1, row=3, columnspan=3, sticky=(tk.W, tk.E))
file_list.column("#1", width=200)

update_file_list()

root.mainloop()
