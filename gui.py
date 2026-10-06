from lz78 import compress_to_lz78
from lz78 import decompress_lz78
from lz77 import compress
import customtkinter as ctk
from tkinter import filedialog
app = ctk.CTk()
app.title("Data Compression")
app.geometry("600x400")
#============================
data=""
#==========================
def run_compression():
    global data
    current_value = segemented_button.get()
    selected = options.get()
    
    if current_value=="Input Text": #"Upload File"
        data=entry.get()

    if selected=="Lz78":
        result = compress_to_lz78(data)
        label.configure(text=result)
    elif selected=="Lz77":
        result=compress(data)
        label.configure(text=result)
    
def run_decompress():
    
    selected = options.get()
    data=entry.get()
    if selected=="Lz78":
        result = decompress_lz78(data)
        label.configure(text=result)
    elif selected=="Lz77":
        #call your function (mariam)
        label.configure(text=result)


    
#===================
label = ctk.CTkLabel(app, text="the result")
label.grid(row=1,column=1,padx=10, pady=10)
options = ctk.CTkComboBox(
    app,
    values=[
        "Lz77",
        "Lz78",
        "Lzw"
    ]
)


options.grid(row=0,column=0,padx=10, pady=10)

entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter your data..."
)


entry.grid(row=3,column=0)
compress_button =ctk.CTkButton(app,text="Compress",command=run_compression)
compress_button .grid(row=0,column=1,padx=10, pady=10)
Decompress_button =ctk.CTkButton(app,text="Decompress",command=run_decompress)
Decompress_button.grid(row=0,column=2)



def segment_click(value):
    if value == "Input Text":
        entry.configure(state="normal")
    else:
           global data
           entry.configure(state="disabled")
           file_path = filedialog.askopenfilename()
           file=open(file_path)
           data=file.read()

        

segemented_button = ctk.CTkSegmentedButton(app, values=["Input Text", "Upload File"], command=segment_click)
segemented_button.set("Input Text")
segemented_button.grid(row=1,column=0)
app.mainloop()