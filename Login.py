from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from connessione import connessione




class Login():
    def __init__(self):

        self.utenti = []


        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("600x400")

        self.display()

        self.root.mainloop()


    #Metodo per mostrare i widget
    def display(self):


        self.frame3 = ttk.Frame(self.root)
        self.frame3.pack(pady=120)

        self.frame1 = ttk.Frame(self.frame3)
        self.frame1.grid(row=0,column=0,sticky="nsew")
        
        self.frame2 = ttk.Frame(self.frame3)
        self.frame2.grid(row=1,column=0,sticky="nsew")

        



        self.email_label = ttk.Label(self.frame1,text="Email: ")
        self.email_label.pack()

        self.email = StringVar()
        self.email_entry = ttk.Entry(self.frame1,textvariable=self.email,width=35)
        self.email_entry.pack()


        self.password_label = Label(self.frame1,text="Password: ")
        self.password_label.pack()


        self.password = StringVar()
        self.password_entry = ttk.Entry(self.frame1,textvariable=self.password,width=35)
        self.password_entry.pack()


        self.nascondi_pass_checkbtn = Checkbutton(self.frame1,text="Nascondi",command=self.NascondiPassword)
        self.nascondi_pass_checkbtn.pack()

        self.accedi_btn = ttk.Button(self.frame2, text="Accedi",command=self.Accedi,width=12)
        self.accedi_btn.grid(row=1,column=0,padx=10,pady=10)

        self.oppure_label = ttk.Label(self.frame2,text="o")
        self.oppure_label.grid(row=1,column=1,padx=5)

        self.registrati_btn = ttk.Button(self.frame2, text="Registrati",command=self.Registrati,width=15)
        self.registrati_btn.grid(row = 1, column=2,padx=10)

        


    
        

    #Metodo che ci consente di nascondere la password quando la checkbutton viene flaggata
    def NascondiPassword(self):
        if self.password_entry.cget("show") == "":
            self.password_entry.config(show='*')
        else:
            self.password_entry.config(show='')


    #Metodo che ci consente di passare al form per la creazione di un utente tramite un bottone
    def Registrati(self):
        self.root.destroy()
        from registrati import registrati
        self.Reg = registrati()



    #Metodo che verifica se i dati inseriti corrispondono ad un utente nel db mongo, se corrispondono entriamo nell'applicazione vera e propria e questa pagina verrà chiusa
    def Accedi(self):
        self.con = connessione()
        self.risultato = self.con.CollezioneUtenti.find()
        for i in self.risultato:
            self.utenti.append(i)
        
        for utente in self.utenti:
            if self.email.get() == utente["email"] and self.password.get() == utente["password"]:
                self.root.destroy()
                from main import main
                m = main()
            else:
                messagebox.showerror(title="Errore",message="I dati inseriti non sono corretti")

        
            
            
        


        





        


if __name__ == "__main__":
    login = Login()