from lz78 import compress_to_lz78
from lz78 import decompress_lz78
from lz78 import parse_string
from BinaryHandling import from_tag__to_Binary
import lz77
import customtkinter as ctk
from tkinter import filedialog
app = ctk.CTk()
app.title("Data Compression")
app.geometry("600x400")
data=""
result=""
#0 for compress 1 for decompress
stat=0

#==========================
def run_compression():
    global data
    global result
    global stat
    stat=0
    selected = options.get()
    if selected=="Lz78":
        result = compress_to_lz78(data)
        from_tag__to_Binary(result)
        label.configure(text=result)
    elif selected=="Lz77":
        result = lz77.compress(data)
        label.configure(text=result)
#========================================  
def run_decompress():
    global data
    global result
    global stat
    stat=1
    selected = options.get()
    if selected=="Lz78":
        result = decompress_lz78(data)
        label.configure(text=result)
    elif selected=="Lz77":
        tags = lz77.read_tags(data)
        result = lz77.decompress(tags)
        label.configure(text=result)
#===================
def upload_file():
           global data
           file_path = filedialog.askopenfilename()
           file=open(file_path)
           data=file.read()
def change_data(event):
    global data
    data = entry.get()
#=====================save compressed file
def save_file_txt():
    global result
    global stat
    if(stat):
      content=result
    else:
     content=parse_string(result)
    file_path = filedialog.asksaveasfilename(title="Save File", defaultextension=".txt",filetypes=[
    ("Text Files", "*.txt"),
    ("All Files", "*.*")
])
    if(content):
        if(file_path):
            with open(file_path, "w") as file:
                file.write(content)
def save_file_bin():
    pass
#=================== GUI
label = ctk.CTkLabel(app, text="the result")
label.grid(row=1,column=1,padx=10, pady=10)

options = ctk.CTkComboBox(app,values=["Lz77","Lz78","Lzw"])
options.grid(row=0,column=0,padx=10, pady=10)

entry = ctk.CTkEntry(app,placeholder_text="Enter your data...")
entry.bind("<KeyRelease>", change_data)
entry.grid(row=3,column=0)

entry_file=ctk.CTkButton(app,text="Upload file",command=upload_file,fg_color="#1976D2",
    hover_color="#1565C0")
entry_file.grid(row=4,column=0,)

Save_txt=ctk.CTkButton(app,text="Save file.txt",command=save_file_txt,fg_color="#EF6C00",
    hover_color="#E65100")
Save_txt.grid(row=5,column=0,padx=10, pady=10)

Save_binary=ctk.CTkButton(app,text="Save file.bin",command=save_file_bin,fg_color="#E96005",
    hover_color="#E96004")
Save_binary.grid(row=5,column=1)

compress_button =ctk.CTkButton(app,text="Compress",command=run_compression,
    fg_color="#2E7D32",
    hover_color="#1B5E20")
compress_button .grid(row=0,column=1,padx=10, pady=10)

Decompress_button =ctk.CTkButton(app,text="Decompress",command=run_decompress,
    fg_color="#7B1FA2",
    hover_color="#6A1B9A")
Decompress_button.grid(row=0,column=2)



"""def segment_click(value):
    if value == "Input Text":
        entry.configure(state="normal")
    else:
           global data
           entry.configure(state="disabled")
           file_path = filedialog.askopenfilename()
           file=open(file_path)
           data=file.read()"""

        

"""segemented_button = ctk.CTkSegmentedButton(app, values=["Input Text", "Upload File"], command=segment_click)
segemented_button.set("Input Text")
segemented_button.grid(row=1,column=0)"""
app.mainloop()