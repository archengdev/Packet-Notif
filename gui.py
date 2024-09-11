from PIL import Image
import customtkinter as ctk
from os import listdir


dung_dir = './dungeons/'
dung_files = listdir(dung_dir)

root = ctk.CTk()
root.title("Packet Sniffer")
root.geometry("700x500")
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
frame = ctk.CTkFrame(root)
frame.grid(row=1,column=0,columnspan=4,sticky="nsew",pady=5,padx=5)
for i in range(10):
    frame.columnconfigure(i, weight=1)
for i in range(6):
    frame.rowconfigure(i, weight=1)


# start button
start = ctk.CTkButton(root)
start.grid(row=2,column=1)

# stop button
stop = ctk.CTkButton(root)
stop.grid(row=2,column=2)

# # dungeon history
hist = ctk.CTkScrollableFrame(root,orientation="horizontal",height=37,
                              label_text="Recently popped dungeons")

hist._scrollbar.configure(height=12)
hist.grid(row=3,column=0,columnspan=4,sticky="nsew",pady=5,padx=5)


def tester(dung_idx):
    if want_notif[dung_idx]:
        # is already gray, change back
        buttons[dung_idx].configure(fg_color='blue', hover_color = 'blue')
        want_notif[dung_idx] = 0
    else:
        # change color to gray
        buttons[dung_idx].configure(fg_color='gray', hover_color = 'gray')
        want_notif[dung_idx] = 1
    # print(dung_idx)

def func(val):
    return lambda: tester(val)

idx_to_file = {}
want_notif = [0] * 60

class DungeonButton(ctk.CTkButton):
    def __init__(self, img, command):
        super(DungeonButton, self).__init__(frame, image=img, command=command,text="",width=60,hover_color='#32a852')


imgs =[]
buttons=[]
for i, file in enumerate(dung_files):
    img = ctk.CTkImage(Image.open(dung_dir + file))
    idx_to_file[i] = file
    
    imgs.append(img)
    button = DungeonButton(imgs[i], func(i))
    buttons.append(button)

row = 0
col = 0
for button in buttons:
    button.grid(row=row, column = col,sticky="nsew")
    col += 1
    if col > 9:
        row += 1
        col = 0

root.mainloop()