from tkinter import Tk, StringVar, Checkbutton, BOTH
from tkinter import ttk, messagebox
from connessione import Connessione


class Login:
    def __init__(self):
        self.utenti = []

        # finestra principale
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("600x400")

        self._crea_ui()

    def run(self):
        self.root.mainloop()

    def _crea_ui(self):
        # frame generale
        self.frame3 = ttk.Frame(self.root)
        self.frame3.pack(pady=120)

        self.frame1 = ttk.Frame(self.frame3)
        self.frame1.grid(row=0, column=0, sticky="nsew")

        self.frame2 = ttk.Frame(self.frame3)
        self.frame2.grid(row=1, column=0, sticky="nsew")

        # email
        self.email_label = ttk.Label(self.frame1, text="Email: ")
        self.email_label.pack()

        self.email = StringVar()
        self.email_entry = ttk.Entry(self.frame1, textvariable=self.email, width=35)
        self.email_entry.pack()

        # password
        self.password_label = ttk.Label(self.frame1, text="Password: ")
        self.password_label.pack()

        self.password = StringVar()
        self.password_entry = ttk.Entry(self.frame1, textvariable=self.password, width=35, show="*")
        self.password_entry.pack()

        # checkbutton nascondi
        self.nascondi_pass_checkbtn = Checkbutton(
            self.frame1, text="Mostra/Nascondi", command=self._toggle_password
        )
        self.nascondi_pass_checkbtn.pack()

        # bottoni login/registrati
        self.accedi_btn = ttk.Button(self.frame2, text="Accedi", command=self._accedi, width=12)
        self.accedi_btn.grid(row=1, column=0, padx=10, pady=10)

        self.oppure_label = ttk.Label(self.frame2, text="o")
        self.oppure_label.grid(row=1, column=1, padx=5)

        self.registrati_btn = ttk.Button(self.frame2, text="Registrati", command=self._registrati, width=15)
        self.registrati_btn.grid(row=1, column=2, padx=10)

    # metodo per nascondere/mostrare password
    def _toggle_password(self):
        if self.password_entry.cget("show") == "":
            self.password_entry.config(show="*")
        else:
            self.password_entry.config(show="")

    # metodo per aprire la finestra registrazione
    def _registrati(self):
        self.root.destroy()
        from registrati import Registrati
        Registrati()

    # metodo login
    def _accedi(self):
        try:
            con = Connessione()
            risultato = con.CollezioneUtenti.find()
            self.utenti = list(risultato)

            for utente in self.utenti:
                if self.email.get() == utente["email"] and self.password.get() == utente["password"]:
                    self.root.destroy()  # chiudo la finestra di login
                    from notebook import MainNotebook
                    root = Tk()  # creo la finestra principale
                    root.title("Applicazione")
                    root.geometry("1280x720")
                    notebook = MainNotebook(root)
                    return

            messagebox.showerror(title="Errore", message="I dati inseriti non sono corretti")

        except Exception as e:
            messagebox.showerror(title="Errore", message=f"Errore di connessione: {e}")