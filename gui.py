import customtkinter as ctk
from tkinter import filedialog
from BinaryHandling import from_tag__to_Binary
from lz77 import *
from lz78 import *
from lzw import *

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
    size=0
    stat=0
    selected = options.get()
    if selected=="Lz78":
        result = compress_to_lz78(data)
        compression_ratio(data,result)
    elif selected=="Lz77":
        result = compress_lz77(data)
        compression_ratio_lz77(data, result)
    elif selected=="Lzw":
        result=lzw_compress_fuc(data)
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
    elif selected=="Lz77":
        tags = read_tags(data)
        result = decompress_lz77(tags)
    elif selected=="Lzw":
        clean_data = lzw_clean_fuc(data)
        result = lzw_decompress_fuc(clean_data)
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
    selected = options.get()
    if(stat):
      content=result
    else:
        if selected=="Lz78":
            content=parse_string(result)
        elif selected=="Lz77":
            content=lz77_to_text(result)
        elif selected== "Lzw":
            content=lzw_to_text(result)
    file_path = filedialog.asksaveasfilename(title="Save File", defaultextension=".txt",filetypes=[
    ("Text Files", "*.txt"),
    ("All Files", "*.*")
])
    if(content):
        if(file_path):
            with open(file_path, "w") as file:
                file.write(content)
def save_file_bin():
    file_path = filedialog.asksaveasfilename(title="Save File", defaultextension=".bin")
    global result
    global stat
    selected=options.get()
    if (not stat):
        from_tag__to_Binary(result,selected,file_path)
#=================== GUI
app.columnconfigure((0, 1), weight=1)
options = ctk.CTkComboBox(
    app,
    values=["Lz77", "Lz78", "Lzw"],
    height=38,
    font=("Segoe UI", 13),
    dropdown_font=("Segoe UI", 13)
)
options.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")

entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter your data...",
    height=38,
    font=("Segoe UI", 13)
)
entry.bind("<KeyRelease>", change_data)
entry.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

entry_file = ctk.CTkButton(
    app,
    text="📁 Upload File",
    command=upload_file,
    height=38,
    font=("Segoe UI", 13, "bold"),
    fg_color="#1F6AA5",
    hover_color="#144870"
)
entry_file.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

compress_button = ctk.CTkButton(
    app,
    text="⚡ Compress",
    command=run_compression,
    height=40,
    font=("Segoe UI", 13, "bold"),
    fg_color="#2FA572",
    hover_color="#1E6B49"
)
compress_button.grid(row=3, column=0, padx=(20, 5), pady=15, sticky="ew")

Decompress_button = ctk.CTkButton(
    app,
    text="🔓 Decompress",
    command=run_decompress,
    height=40,
    font=("Segoe UI", 13, "bold"),
    fg_color="#2FA572",
    hover_color="#1E6B49"
)
Decompress_button.grid(row=3, column=1, padx=(5, 20), pady=15, sticky="ew")

label = ctk.CTkLabel(
    app,
    text="the result",
    height=50,
    corner_radius=8,
    fg_color=("gray85", "#2B2B2B"),
    font=("Segoe UI", 14)
)
label.grid(row=4, column=0, columnspan=2, padx=20, pady=15, sticky="ew")

Save_txt = ctk.CTkButton(
    app,
    text="💾 Save file.txt",
    command=save_file_txt,
    height=38,
    font=("Segoe UI", 12, "bold"),
    fg_color="#3B3B3B",
    hover_color="#2B2B2B",
    border_width=1,
    border_color="#555555"
)
Save_txt.grid(row=5, column=0, padx=(20, 5), pady=(5, 20), sticky="ew")

Save_binary = ctk.CTkButton(
    app,
    text="💾 Save file.bin",
    command=save_file_bin,
    height=38,
    font=("Segoe UI", 12, "bold"),
    fg_color="#3B3B3B",
    hover_color="#2B2B2B",
    border_width=1,
    border_color="#555555"
)
Save_binary.grid(row=5, column=1, padx=(5, 20), pady=(5, 20), sticky="ew")


app.mainloop()