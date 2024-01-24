import PIL
from tkinter import *
from tkinter.filedialog import *
import customtkinter
import speedtestpy
import threading

def do_speedtest():
    button.configure(state = "disabled")
    download_label.configure(text = f"{int(speedtestpy.st.download()/1024/1024)} Mbps: download speed ")
    upload_label.configure(text = f"{int(speedtestpy.st.upload()/1024/1024)} Mbps: upload speed ")
    button.configure(state = "normal")

def speedtest():
    t = threading.Thread(target=do_speedtest,daemon=True)
    t.start()
    

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

dex = customtkinter.CTk()
dex.geometry("650x600")
dex.iconbitmap("C:\\Users\\Kmuwl\\Downloads\\Flameia-Machemicals-Control-panels.128.ico")
dex.title("Blake's SpeedTest")

entry1 = customtkinter.CTkEntry(master=dex, placeholder_text="speedtest")

img = customtkinter.CTkCanvas(dex,borderwidth = 0)
img.pack(fill = "both",expand = True)
photo = PhotoImage(file = "C:\\Users\\Kmuwl\Downloads\\4fb0aff2644234b0585ad2fbc7c522a3.png")

img.create_image(0,0,anchor = "nw",image = photo)

button = customtkinter.CTkButton(master=dex, text="Check Speed", command=speedtest)
button.pack(pady=12, padx=10)
button.place(relx = 0.5, rely = 0.5, anchor = customtkinter.CENTER)

download_label = customtkinter.CTkLabel(master = dex,text="500 Mbps:download speed ")
download_label.pack()

upload_label = customtkinter.CTkLabel(master = dex,text="200 Mbps: upload speed")
upload_label.pack()

dex.mainloop()