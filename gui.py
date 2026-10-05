from lz78 import compress_to_lz78
from lz78 import decompress_lz78
from lz77 import compress
import customtkinter as ctk
app = ctk.CTk()
app.title("Data Compression")
app.geometry("600x400")
#============================
def run_compression():
    selected = options.get()
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


entry.grid(row=1,column=0)
compress=ctk.CTkButton(app,text="Compress",command=run_compression)
compress.grid(row=0,column=1,padx=10, pady=10)
Decompress=ctk.CTkButton(app,text="Decompress",command=run_decompress)
Decompress.grid(row=0,column=2)
app.mainloop()