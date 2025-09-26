import pandas as pd
from tkinter import filedialog, messagebox

def apri_file_dialog(tipo):
    estensioni = {
        "excel": [("Excel files", "*.xlsx")],
        "csv": [("CSV files", "*.csv")],
        "json": [("JSON files", "*.json")]
    }
    return filedialog.askopenfilename(
        title="Apri un file",
        initialdir="/",
        filetypes=estensioni.get(tipo, [("All files", "*.*")])
    )

def salva_file_dialog(tipo):
    estensioni = {
        "excel": [("Excel files", "*.xlsx")],
        "csv": [("CSV files", "*.csv")],
        "json": [("JSON files", "*.json")]
    }
    return filedialog.asksaveasfilename(
        defaultextension=f".{tipo}",
        filetypes=estensioni.get(tipo, [("All files", "*.*")]),
        title=f"Salva il file {tipo.upper()}"
    )

def mostra_errore(e):
    messagebox.showerror("Errore", f"Errore: {e}")
