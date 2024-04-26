import requests
import json

import tkinter
import tkinter.filedialog
import tkinter.messagebox
import customtkinter

# https://fakestoreapi.com/


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Fenêtre mère
        self.title("Lecteur de CSV simple")
        self.geometry(f"{1100}x{580}")

        # Frame top
        self.top_frame = customtkinter.CTkFrame(self, width=1100, corner_radius=20)
        self.top_frame.grid(row=0, sticky="nsew")

        ## ctk entry
        self.entry = customtkinter.CTkEntry(self.top_frame, placeholder_text="chemin/vers/fichier",width=800)
        self.entry.grid(row=0, padx=(20, 20), pady=(20, 20), sticky="w")

        ## button load
        self.btn_charger = customtkinter.CTkButton(self.top_frame, command=self.selection_fichier,text="Sélectionner",height=30)
        self.btn_charger.grid(row=0, padx=(20,20), pady=10,sticky="e")
 

        # Frame tableau csv
        self.csv_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
        self.csv_frame.grid(row=1,padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        self.obtenir_produits()



    def obtenir_produits(self):
        res = requests.get('https://fakestoreapi.com/products')
        data = res.json()
        print(data)
        return data

    def enregistrer_csv(self):pass

    def selection_fichier(self):
        name = tkinter.filedialog.askopenfilename()
        self.entry.delete(0,'end')
        self.entry.insert(0,name)
        self.charger_csv(name)
        

    def selection_enregistrement(self):pass





if __name__ == "__main__":
    app = App()
    #print(app.selection_fichier())
    app.mainloop()