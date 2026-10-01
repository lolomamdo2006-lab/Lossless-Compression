from lz77 import compress as lz77_compress
import customtkinter as ctk
app = ctk.CTk()
app.title("Data Compression")
app.geometry("600x400")
#============================
def run_compression():
    result = lz77_compress();
    result_label.configure(text=result)
    

#===================
label = ctk.CTkLabel(app, text="===== Lossless Compression =====")
label.pack()
result_label = ctk.CTkLabel(app, text="Result")
result_label.pack()
button77 = ctk.CTkButton(app, text="Lz77",command=run_compression)
button77.pack()




'''button78 = ctk.CTkButton(app, text="Lz78")
button78.pack()
buttonZW = ctk.CTkButton(app, text="LzZw")
buttonZW.pack()'''
app.mainloop()