# #the following three lines show a blank window
# import tkinter as tk
# window = tk.Tk()
# window.mainloop()

import tkinter as tk
from compressmodule_02 import compress,decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir='/',title="Select a file")
    return filename

def compression(i,o):
    compress(i,o)

window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")

# input_entry = tk.Entry(window)
# output_entry = tk.Entry(window)
#
# input_label = tk.Label(window,text="File to be compressed")#
# output_label = tk.Label(window,text="File compressed")#
#updated. lambda:fetch the real time values from the input field
compress_button = tk.Button(window,text="Compress",command=lambda:compression(open_file(),"compressOutput_05.txt"))


# input_label.grid(row=0,column=0)
# input_entry.grid(row=0,column=1)
# output_label.grid(row=1,column=0)
# output_entry.grid(row=1,column=1)
compress_button.grid(row=2,column=1)

window.mainloop()