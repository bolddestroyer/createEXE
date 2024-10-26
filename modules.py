import os
import sys
import tkinter
from tkinter import filedialog



#Open the file explorer
def open_file_explorer(label):
    file_path = filedialog.askopenfilename()        #Open the file explorer, save file path as a variable
    if file_path:
        label.config(text=file_path)        #Set the file path as new text for the label


#Open the file explorer with the directory of the generated EXE file 
def open_exe_file_loc(exe_file_path):
    os.startfile(os.path.dirname(exe_file_path))
    sys.exit()


#Custom message box with buttons to close and open the file explorer
def custom_messagebox(exe_file_path):
    #Top-level pop-up window
    msg_box = tkinter.Tk()
    msg_box.title('Info')
    
    #Label
    lbl_message = tkinter.Label(msg_box, text='The EXE file was created successfully.')
    lbl_message.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    #Button - close the message box
    btn_ok = tkinter.Button(msg_box, text="OK", command=lambda: sys.exit())
    btn_ok.grid(row=1, column=0, padx=10, pady=10)
    
    #Button - open directory in the file explorer with the generated EXE file
    btn_open_explorer = tkinter.Button(msg_box, text="Open EXE file location", command=lambda: open_exe_file_loc(exe_file_path))
    btn_open_explorer.grid(row=1, column=1, padx=10, pady=10)