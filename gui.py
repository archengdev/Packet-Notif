import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter as ctk
import os

dung_dir = './dungeons/'
dung_files = os.listdir(dung_dir)
print(len(dung_files))

root = ctk.CTk()
root.title("Packet Sniffer")
root.geometry("550x500")
root.iconbitmap('./logo.ico')

root.columnconfigure(0, weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(1, weight=1)

# for the title
title = ctk.CTkLabel(root,
                     text="RotMG Packet Sniffer",
                     font=("helvetica",13))
title.grid(row=0,column=1,columnspan=2,pady=5)

# , label_text="Select which dungeons you want to be notified for"
# for the list of dungeons to select
frame = ctk.CTkScrollableFrame(root, label_text="Select which dungeons you want to be notified for")
frame.grid(row=1,column=0,columnspan=4,sticky="nsew",pady=5,padx=5)


# start button
start = ctk.CTkButton(root)
start.grid(row=2,column=1)

# stop button
stop = ctk.CTkButton(root)
stop.grid(row=2,column=2)

# # dungeon history
hist = ctk.CTkScrollableFrame(root,orientation="horizontal",height=37,
                              label_text="Recently popped dungeons")

# label_text_color
# label_fg_color
# label_font

hist._scrollbar.configure(height=12)
hist.grid(row=3,column=0,columnspan=4,sticky="nsew",pady=5,padx=5)


# for x in range(20):
#     customtkinter.CTkButton(frame, text="button").pack(pady=10)

# file = './dungeons/3d.png'

# image = Image.open(file)


# img = ImageTk.PhotoImage(image.resize((50, 50))) 
# label = tk.Label(root, image=img)
# label.image = img
# label.pack()
# aby = ImageTk.PhotoImage(Image.open("./dungeons/3d.png"))
# abyl = tk.Label(frame, image=aby)
# abyl.pack(side='left')
# udl = ImageTk.PhotoImage(Image.open("./dungeons/udl.png"))
# udll = tk.Label(root,image=udl)


# forax = tk.PhotoImage(file=r"./dungeons/forax.png")
# threed = tk.PhotoImage(file=r"./dungeons/snake.png")
# test = forax.subsample(3,3)
# t2 = threed.subsample(3,3)
# tk.Button(root,image=t2).pack(side="top")
# tk.Button(root, image=test).pack(side="top")

def tester(dung_idx):
    print(dung_idx)

def func(val):
    return lambda: tester(val)



imgs =[]
buttons=[]
for i, file in enumerate(dung_files):
    # img = Image.open(dung_dir + file).resize((30, 30))
    # print(img.mode)
    img = ctk.CTkImage(Image.open(dung_dir + file).resize((30, 30)))
    
    imgs.append(img)
    # img.configure()
    button = ctk.CTkButton(frame, image=imgs[i],text="",width=35, command=func(i))
    buttons.append(button)


for button in buttons:
    button.pack(side='left', anchor='nw')



# i2 = ImageTk.PhotoImage(Image.open(dung_dir + 'aby.png').resize((30, 30)))
# # img.configure()
# l2 = tk.Label(frame, image=i2)
# l2.pack(side='left', anchor='nw')


root.mainloop()


# def add_to_list(event=None):
#     text = entry.get()
#     if text:
#         text_list.insert(tk.END, text)
#         entry.delete(0, tk.END)


# entry_btn = ttk.Button(frame, text="add", command = add_to_list)