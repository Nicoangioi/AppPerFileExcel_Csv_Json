from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from connessione import Connessione


class Registrati:
    def __init__(self):
        self.root = Tk()
        self.root.title("Registrati")
        self.root.geometry("600x400")

        self.display()

        self.root.mainloop()

    def display(self):
        # Frame principale
        self.frame3 = ttk.Frame(self.root)
        self.frame3.pack(pady=85)

        # Sottosezioni
        self.frame1 = ttk.Frame(self.frame3)
        self.frame1.grid(row=0, column=0, sticky="nsew")

        self.frame2 = ttk.Frame(self.frame3)
        self.frame2.grid(row=1, column=0, sticky="nsew")

        # Campi Email
        self.email_label = ttk.Label(self.frame1, text="Email: ")
        self.email_label.pack()

        self.email = StringVar()
        self.email_entry = ttk.Entry(self.frame1, textvariable=self.email, width=30)
        self.email_entry.pack()

        # Campi Password
        self.password_label = Label(self.frame1, text="Password: ")
        self.password_label.pack()

        self.password = StringVar()
        self.password_entry = ttk.Entry(self.frame1, textvariable=self.password, width=30)
        self.password_entry.pack()

        # Conferma Password
        self.conferma_password_label = Label(self.frame1, text="Conferma Password: ")
        self.conferma_password_label.pack()

        self.conferma_password = StringVar()
        self.conferma_password_entry = ttk.Entry(
            self.frame1, textvariable=self.conferma_password, width=30
        )
        self.conferma_password_entry.pack()

        # Nascondi Password
        self.nascondi_pass_checkbtn = Checkbutton(
            self.frame1, text="Nascondi", command=self.NascondiPassword
        )
        self.nascondi_pass_checkbtn.pack()

        # Bottoni
        self.registrati_btn = ttk.Button(
            self.frame2, text="Registrati", command=self.Registrati
        )
        self.registrati_btn.grid(row=0, column=0)

        self.oppure_label = ttk.Label(self.frame2, text="o")
        self.oppure_label.grid(row=0, column=1, padx=10)

        self.torna_al_login = ttk.Button(
            self.frame2, text="Torna al login", command=self.TornaAlLogin
        )
        self.torna_al_login.grid(row=0, column=2)

    # Metodo per nascondere le password
    def NascondiPassword(self):
        if self.password_entry.cget("show") == "":
            self.password_entry.config(show="*")
        else:
            self.password_entry.config(show="")

        if self.conferma_password_entry.cget("show") == "":
            self.conferma_password_entry.config(show="*")
        else:
            self.conferma_password_entry.config(show="")

    # Metodo per registrare l'utente
    def Registrati(self):
        email_val = self.email.get().strip()
        pass_val = self.password.get().strip()
        conferma_val = self.conferma_password.get().strip()

        if email_val == "" or pass_val == "" or conferma_val == "":
            messagebox.showwarning(
                title="Attenzione", message="Inserisci tutti i campi richiesti"
            )
            return

        if pass_val != conferma_val:
            messagebox.showerror(
                title="Errore", message="Le password non corrispondono"
            )
            return

        self.con = Connessione()
        self.utente = {"email": email_val, "password": pass_val}

        try:
            self.con.CollezioneUtenti.insert_one(self.utente)
            messagebox.showinfo(
                title="Successo", message="Utente registrato correttamente!"
            )
            self.TornaAlLogin()
        except Exception as e:
            messagebox.showerror(title="Errore", message=f"Errore DB: {e}")

    # Metodo per tornare al login
    def TornaAlLogin(self):
        self.root.destroy()
        from Login import Login

        self.login = Login()


if __name__ == "__main__":
    Registrati()
