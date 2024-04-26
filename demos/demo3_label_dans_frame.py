# https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/simple_example.py
import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# fenêtre de l'application.
app = customtkinter.CTk()
app.geometry("250x150")
app.title(__name__)
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

# Une frame qui contiendra d'autres widgets
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

# premier widget, un label
label_1 = customtkinter.CTkLabel(master=frame_1,text="Voici une fenêtre avec deux label", justify=customtkinter.LEFT)
label_1.grid(column=0,row=0,padx=10,pady=20,sticky="wn")

# un autre label
label_2 = customtkinter.CTkLabel(master=frame_1,text="Dans une frame.", justify=customtkinter.LEFT)
label_2.grid(column=0,row=1,padx=10,pady=20,sticky="wn")


app.mainloop()