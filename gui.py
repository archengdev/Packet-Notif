import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter as ctk
import os

# fix some pngs (3d)

# make dungeons grayscale?
# click and hold to choose?
# choose from recently popped?


root = ctk.CTk()
root.title("Packet Sniffer")
root.geometry("500x300")
root.iconbitmap('./logo.ico')


# frame =customtkinter.CTkScrollableFrame(root)
# # frame =customtkinter.CTkScrollableFrame(root, orientation="horizontal")
# frame.grid(row=0, column=0, sticky="nsew")

# for x in range(20):
#     customtkinter.CTkButton(frame, text="button").pack(pady=10)

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# root.rowconfigure(1,weight=0)
# frame.columnconfigure(0, weight=1)
# frame.rowconfigure(1, weight=1)


# file = './dungeons/3d.png'

# image = Image.open(file)


# img = ImageTk.PhotoImage(image.resize((50, 50))) 
# label = tk.Label(root, image=img)
# label.image = img
# label.pack()
# aby = ImageTk.PhotoImage(Image.open("./dungeons/3d.png"))
# abyl = tk.Label(root, image=aby)
# udl = ImageTk.PhotoImage(Image.open("./dungeons/udl.png"))
# udll = tk.Label(root,image=udl)

# abyl.grid(row=0,column=0)
# udll.grid(row=0,column=1)
# udll.pack(side = "top", fill = "none")
# abyl.pack(side = "bottom", fill = "both", expand="yes")

# forax = tk.PhotoImage(file=r"./dungeons/forax.png")
# threed = tk.PhotoImage(file=r"./dungeons/snake.png")
# test = forax.subsample(3,3)
# t2 = threed.subsample(3,3)
# tk.Button(root,image=t2).pack(side="top")
# tk.Button(root, image=test).pack(side="top")

#--------
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1,weight=2)
# root.rowconfigure(0, weight=1)


# def add_to_list(event=None):
#     text = entry.get()
#     if text:
#         text_list.insert(tk.END, text)
#         entry.delete(0, tk.END)


# frame = ttk.Frame(root)
# frame.grid(row=0,column=0, sticky="nsew", padx=5, pady=5)

# frame.columnconfigure(0, weight=1)
# frame.rowconfigure(1, weight=1)

# entry = ttk.Entry(frame)
# entry.grid(row=0, column=0, sticky="ew")

# entry.bind("<Return>", add_to_list)
# # will pass event object to the function, can use lambda function

# entry_btn = ttk.Button(frame, text="add", command = add_to_list)
# entry_btn.grid(row=0, column=1)

# text_list = tk.Listbox(frame)
# text_list.grid(row=1,column=0, columnspan=2, sticky="nsew")
#--------

root.columnconfigure(0, weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(1, weight=1)

# for the title
title = ctk.CTkLabel(root,
                     text="RotMG Packet Sniffer: Choose which dungeons you want to be notified for",
                     font=("helvetica",13))
title.grid(row=0,column=1,columnspan=2,pady=5)

# for the list of dungeons to select
frame = ctk.CTkScrollableFrame(root)
frame.grid(row=1,column=0,columnspan=4,sticky="nsew",pady=5,padx=5)

# start button
start = ctk.CTkButton(root)
start.grid(row=2,column=1)

# stop button
stop = ctk.CTkButton(root)
stop.grid(row=2,column=2)

# # dungeon history
hist = ctk.CTkScrollableFrame(root,orientation="horizontal",height=37,
                              label_text="hello")

# label_text_color
# label_fg_color
# label_font

hist._scrollbar.configure(height=12)
hist.grid(row=3,column=0,columnspan=4,sticky="nsew",pady=5,padx=5)

a = ttk.Label(hist,text="test")
a.grid(row=10,column=1)
b = ttk.Label(frame,text="test")
b.grid(row=10,column=0)



root.mainloop()