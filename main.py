from unicodedata import name
import letters
import tkinter as tk

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b" , "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

root=tk.Tk()
root.geometry("400x200")
name_var=tk.StringVar()
passw_var=tk.StringVar()

def submit():
	name = name_var.get()
	
	print("Calculating " + name + "for you...")

	name_var.set("")


# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Enter Spanish Word:', font=('calibre',10, 'bold'))
answer = tk.Label(root, text = 'Answer', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method

name_label.grid(row=0,column=0)
answer.grid(row=4,column=0)
name_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)

# performing an infinite loop
# for the window to display
root.mainloop()

