import tkinter
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Fenêtre mère
        self.title("Lecteur de CSV simple")
        self.geometry(f"{480}x{520}")
        # Frame top
        self.top_frame = customtkinter.CTkFrame(self,height=160, corner_radius=20)
        self.top_frame.grid(row=0,column=0,columnspan=4,padx=30, sticky="nsew")
        ## Écran Formule
        self.ecran = customtkinter.CTkEntry(self.top_frame,placeholder_text="Formule",height=100,width=400).grid()

        # Frame Buttons
        self.btn_frame = customtkinter.CTkFrame(self, corner_radius=20,fg_color='white')
        self.btn_frame.grid(row=1,column=0,columnspan=4,rowspan=4,padx=30, sticky="nsew")

        ##Numberbuttons
        self.btn0 = customtkinter.CTkButton(self.btn_frame,text=0,height=100,width=100,command=lambda : self.ajout_formule(0)).grid(row=3,column=0)
        self.btn1 = customtkinter.CTkButton(self.btn_frame,text=1,height=100,width=100,command=lambda : self.ajout_formule(1)).grid(row=2,column=0)
        self.btn2 = customtkinter.CTkButton(self.btn_frame,text=2,height=100,width=100,command=lambda : self.ajout_formule(2)).grid(row=2,column=1)
        self.btn3 = customtkinter.CTkButton(self.btn_frame,text=3,height=100,width=100,command=lambda : self.ajout_formule(3)).grid(row=2,column=2)
        self.btn4 = customtkinter.CTkButton(self.btn_frame,text=4,height=100,width=100,command=lambda : self.ajout_formule(4)).grid(row=1,column=0)
        self.btn5 = customtkinter.CTkButton(self.btn_frame,text=5,height=100,width=100,command=lambda : self.ajout_formule(5)).grid(row=1,column=1)
        self.btn6 = customtkinter.CTkButton(self.btn_frame,text=6,height=100,width=100,command=lambda : self.ajout_formule(6)).grid(row=1,column=2)
        self.btn7 = customtkinter.CTkButton(self.btn_frame,text=7,height=100,width=100,command=lambda : self.ajout_formule(7)).grid(row=0,column=0)
        self.btn8 = customtkinter.CTkButton(self.btn_frame,text=8,height=100,width=100,command=lambda : self.ajout_formule(8)).grid(row=0,column=1)
        self.btn9 = customtkinter.CTkButton(self.btn_frame,text=9,height=100,width=100,command=lambda : self.ajout_formule(9)).grid(row=0,column=2)

        ## Autres btn
        self.plus = customtkinter.CTkButton(self.btn_frame,text='+',height=100,width=100,fg_color='grey',command=lambda : self.ajout_formule(0)).grid(row=0,column=3)
        self.moins = customtkinter.CTkButton(self.btn_frame,text='-',height=100,width=100,fg_color='grey',command=lambda : self.ajout_formule(0)).grid(row=1,column=3)
        self.multiple = customtkinter.CTkButton(self.btn_frame,text='x',height=100,width=100,fg_color='grey',command=lambda : self.ajout_formule(0)).grid(row=2,column=3)
        self.egal = customtkinter.CTkButton(self.btn_frame,text='=',height=100,width=100,fg_color='green',command=lambda : self.resoudre_equation).grid(row=3,column=3)
        self.delete = customtkinter.CTkButton(self.btn_frame,text='del',height=100,width=100,fg_color='red',command=lambda : self.resoudre_equation).grid(row=3,column=2)



    def ajout_formule(self,caractere):
        # ajouter caractère à la fin de l'objet <CTkEntry> self.ecran (Voir la documentation)
        pass

    def resoudre_equation(self):pass

    def lire_equation(self):pass

    def delete(self):pass

if __name__ == "__main__":
    app = App()
    app.mainloop()