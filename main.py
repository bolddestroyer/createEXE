import os
import py_compile
import re
import shutil
import subprocess
import time
import tkinter
from tkinter import messagebox
from modules import *



#Create an EXE for a python file
def createEXEfile(file_path):
    regexp_pyfile = re.compile('.*.py$')        #Regexp for a python file

    #If a python file is selected
    if regexp_pyfile.search(file_path):
        try:
            py_compile.compile(file_path, doraise=True)     #Check if selected python file has got no syntax errors
        except py_compile.PyCompileError as error:
            messagebox.showerror('Syntax Error', f'{error}.')
            return      #In case of errors, show message box and return nothing (stop the process)

        cmd_new_wrk_dir = r'C:\Users\doria\Documents\Virtual Studio Code\_exe\\' + os.path.splitext(os.path.basename(file_path))[0]      #New working directory
        cmd_input_command = fr'C:\Users\doria\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe --onefile "{file_path}"'        #CMD input command
        exe_file_path = cmd_new_wrk_dir + '/dist/' + os.path.splitext(os.path.basename(file_path))[0] + '.exe'    #Path containing the exe file

        #If the new working directory exists, remove it with all its content (all old files are removed)
        if os.path.exists(cmd_new_wrk_dir):
            shutil.rmtree(cmd_new_wrk_dir)

        time.sleep(1)

        os.makedirs(cmd_new_wrk_dir)        #Create a new working directory
        os.chdir(cmd_new_wrk_dir)       #Change the working directory
        subprocess.run(cmd_input_command, shell=True)       #Run the command in CMD
        custom_messagebox(exe_file_path)        # Show the custom message box upon successful completion

    #If no file is selected
    elif file_path == 'No file selected':
        messagebox.showerror('Error', 'Select a file first.')

    #If selected file is not a python file
    elif not regexp_pyfile.search(file_path):
        messagebox.showerror('Error', 'Only python files can be processed (extension \'.py\').')


#Main method
def createEXE_exec():
    #Main window
    window = tkinter.Tk()       
    window.title('Create an EXE file')

    #Label with the file path
    lbl_dir = tkinter.Label(window, text='No file selected')
    lbl_dir.grid(row=0, column=0, padx=10, pady=10)

    #Button - execute open_file_explorer; search for a file 
    btn_brow_file = tkinter.Button(window, text='Browse', command=lambda: open_file_explorer(lbl_dir))      #lambda - command is executed on click
    btn_brow_file.grid(row=0, column=1, padx=10, pady=10)

    #Button - execute createEXEfile; create the EXE file; value in the label (file path) as an input
    btn_execute = tkinter.Button(window, text="Create the EXE file", command=lambda: createEXEfile(lbl_dir.cget("text")))
    btn_execute.grid(row=1, column=0, padx=10, pady=10)

    #Loop the window, refresh after each change (e.g. change of value in label)
    window.mainloop()