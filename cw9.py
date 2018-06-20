//1
import Tkinter as tk 
import tkFont as tkF 
import tkMessageBox as tkMB 

root = tk.Tk() 

default_font = tkF.nametofont("TkDefaultFont") 
default_font.configure(size = 48) 
root.option_add("*Font", default_font) 

bt1 = tk.Button(root, text = "button", command = root.quit).grid(row = 1, column = 1) 
e1 = tk.Entry(root) 
e1.grid(row = 2, column = 1) 
e1.insert(tk.END, "Message") 




rb1 = tk.Radiobutton(root, text = "red", command = red) 
rb1.grid(column = 0, row = 0) 

rb2 = tk.Radiobutton(root, text = "green") 
rb2.grid(column = 1, row = 0) 

rb3 = tk.Radiobutton(root, text = "blue") 
rb3.grid(column = 2, row = 0) 



root.mainloop()
