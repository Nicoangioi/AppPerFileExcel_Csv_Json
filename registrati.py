from tkinter import *
from tkinter import ttk
from tkinter import messagebox




from connessione import connessione








class registrati():
    def __init__(self):
        self.root = Tk()
        self.root.title("Registrati")
        self.root.geometry("600x400")
        
        self.display()

        

        self.root.mainloop()

    def display(self):


        self.frame3 = ttk.Frame(self.root)
        self.frame3.pack(pady=85)

        self.frame1 = ttk.Frame(self.frame3)
        self.frame1.grid(row=0,column=0,sticky="nsew")
        
        self.frame2 = ttk.Frame(self.frame3)
        self.frame2.grid(row=1,column=0,sticky="nsew")

        



        self.email_label = ttk.Label(self.frame1,text="Email: ")
        self.email_label.pack()

        self.email = StringVar()
        self.email_entry = ttk.Entry(self.frame1,textvariable=self.email,width=30)
        self.email_entry.pack()


        self.password_label = Label(self.frame1,text="Password: ")
        self.password_label.pack()


        self.password = StringVar()
        self.password_entry = ttk.Entry(self.frame1,textvariable=self.password,width=30)
        self.password_entry.pack()


        self.conferma_password_label = Label(self.frame1,text="Conferma Password: ")
        self.conferma_password_label.pack()


        self.conferma_password = StringVar()
        self.conferma_password_entry = ttk.Entry(self.frame1,textvariable=self.conferma_password,width=30)
        self.conferma_password_entry.pack()


        self.nascondi_pass_checkbtn = Checkbutton(self.frame1,text="Nascondi",command=self.NascondiPassword)
        self.nascondi_pass_checkbtn.pack()

        self.registrati_btn = ttk.Button(self.frame2, text="Registrati", command=self.Registrati)
        self.registrati_btn.grid(row=0,column=0)

        self.oppure_label = ttk.Label(self.frame2,text="o")
        self.oppure_label.grid(row=0,column=1,padx=10)

        self.torna_al_login = ttk.Button(self.frame2,text="Torna al login",command=self.TornaAlLogin)
        self.torna_al_login.grid(row=0,column=2)



    def NascondiPassword(self):
        if self.password_entry.cget("show") == "":
            self.password_entry.config(show='*')
        else:
            self.password_entry.config(show='')

        if self.conferma_password_entry.cget("show") =="":
            self.conferma_password_entry.config(show='*')
        else:
            self.conferma_password_entry.config(show='')

    
    def Registrati(self):



        if self.email == "" and self.password == "" and self.conferma_password == "":
            messagebox.showwarning(title="warning", message="Inserisci prima i dati nei campi vuoti")
        else:
            self.con = connessione()
            self.utente = {"email":self.email.get(),"password":self.password.get()}

            self.risultato = self.con.CollezioneUtenti.insert_one(self.utente)

            messagebox.showinfo(title="info", message="Utente Registrato in modo corretto!")
            



      

    def TornaAlLogin(self):
        self.root.destroy()
        from Login import Login
        self.login = Login()




        