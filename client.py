import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import Pyro4

# Connect to the P2P server
p2p_server = Pyro4.Proxy("PYRONAME:p2p_server")

#function to add a file.
def add_file():
    filename = filedialog.askopenfilename()
    if filename:
        with open(filename, 'rb') as file:
            content = file.read()
            result = p2p_server.add_file(os.path.basename(filename), content)
            status_label.config(text=result)
            update_file_list()

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

def update_file_list():
    file_list.delete(*file_list.get_children())
    for filename in p2p_server.file_storage.keys():
        file_list.insert('', 'end', text=filename)

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
