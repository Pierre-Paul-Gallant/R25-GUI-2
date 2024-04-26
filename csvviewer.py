import tkinter
import tkinter.filedialog
import tkinter.messagebox
import customtkinter
import csv

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
        



        # Frame bottom

    def charger_csv(self, path):
        with open(path,'r',encoding='utf-8') as f_lu :
            csv_reader = csv.reader(f_lu,delimiter=',')
            for num,line in enumerate(csv_reader):
                print(num,line)
                line_frame = customtkinter.CTkFrame(self.csv_frame, corner_radius=10)
                line_frame.grid(row=num)
                no_ligne = customtkinter.CTkLabel(line_frame,text=num)
                no_ligne.grid(row=0,column=0)
                for num2,element in enumerate(line) :
                    tiny_frame = customtkinter.CTkFrame(line_frame, corner_radius=10).grid(row=0,column=num2+1)
                    customtkinter.CTkLabel(line_frame,text=element,padx=10,anchor='w').grid(row=0,column=0)

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