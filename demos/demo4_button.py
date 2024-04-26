from tkinter import LEFT
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# fenêtre de l'application.
app = customtkinter.CTk()
app.geometry("450x180")
app.title(__name__)
app.grid_columnconfigure((0,1), weight=1)
app.grid_rowconfigure((0,1), weight=1)

# Une frame qui contiendra d'autres widgets
frame_1 = customtkinter.CTkFrame(master=app,width=400)
frame_1.grid(column=0,row=0,padx=10,pady=20,sticky="e")
frame_1.grid_columnconfigure(0, weight=3,uniform="column")
frame_1.grid_columnconfigure(1, weight=2,uniform="column")
frame_1.grid_rowconfigure((0,1), weight=1)

# premier widget, un label
label_1 = customtkinter.CTkLabel(master=frame_1,text="Voici une fenêtre avec deux label",anchor="w",width=180)
label_1.grid(column=0,row=0,padx=30,pady=20,sticky="w")

def appuyer_sur_button():
    label_1.configure(text ="Yay un bouton !")

button_1 = customtkinter.CTkButton(master=frame_1, command=appuyer_sur_button,width=200)
button_1.grid(column=1,row=1,padx=10,pady=20,sticky="e")

app.mainloop()