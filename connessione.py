import pymongo
from pymongo import MongoClient
from tkinter import messagebox


# Classe che gestisce la connessione a MongoDB Cloud
class Connessione:
    def __init__(self):
        try:
            # Connessione al cluster
            self.client = MongoClient("mongodb://localhost:27017/")
            # Selezione del database
            self.db = self.client["pymongo"]

            # Selezione della collezione utenti
            self.CollezioneUtenti = self.db["utenti"]

        except Exception as e:
            messagebox.showerror("Errore connessione", f"Impossibile connettersi a MongoDB.\n{e}")
            self.client = None
            self.db = None
            self.CollezioneUtenti = None
