import tkinter as tk #importing modules
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import*#tk is user interface
from tkinter import Toplevel, Button, Tk, Menu

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title("THE BIKER YASHAS REDDY")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title("THE BIKER YASHAS REDDY")
window = tk.Tk()
window.title("YASHAS REDDY'S WINDOW")
window.rowconfigure(0)
window.columnconfigure(1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0,   padx=5, pady=5)
btn_save.grid(row=1, column=0,   padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


   

menubar = Menu(window)  
file = Menu(menubar, tearoff=0)  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close")  
  
file.add_separator()  
  
file.add_command(label="Exit", command=window.quit)  
  
menubar.add_cascade(label="File", menu=file)  
edit = Menu(menubar)  
edit.add_command(label="Undo")  
  
edit.add_separator()  
  
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")  
  
menubar.add_cascade(label="Edit", menu=edit)  
help = Menu(menubar)  
help.add_command(label="About")  
menubar.add_cascade(label="Help", menu=help)  
  
window.config(menu=menubar)  
  
   

window.mainloop()#to display the window until the applicatio is closed manually
