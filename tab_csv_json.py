from tkinter import *
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import json

class CsvJsonTab:
    def __init__(self, notebook):
        self.frame = Frame(notebook)
        self.NomeFile_Csv = None
        self.NomeFile_Json = None
        self.df_csv = None
        self.df_json = None

        self._crea_ui()

    def _crea_ui(self):
        # Frame CSV
        self.Csv_Frame = Frame(self.frame)
        self.Csv_Frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.CsvTab_LabelFrame = LabelFrame(self.Csv_Frame, text="Csv File")
        self.CsvTab_LabelFrame.pack(fill=BOTH, expand=True, ipady=225)

        self.tree_csv = ttk.Treeview(self.CsvTab_LabelFrame)
        self.tree_csv.pack(fill=BOTH, expand=True)

        self.scroll_y_csv = ttk.Scrollbar(self.tree_csv, orient=VERTICAL, command=self.tree_csv.yview)
        self.scroll_x_csv = ttk.Scrollbar(self.tree_csv, orient=HORIZONTAL, command=self.tree_csv.xview)
        self.scroll_y_csv.pack(side=RIGHT, fill=Y)
        self.scroll_x_csv.pack(side=BOTTOM, fill=X)
        self.tree_csv.configure(yscrollcommand=self.scroll_y_csv.set, xscrollcommand=self.scroll_x_csv.set)

        self.CsvBottoni_LabelFrame = LabelFrame(self.Csv_Frame, text="Apri e Converti")
        self.CsvBottoni_LabelFrame.pack(fill=BOTH, pady=5)

        self.label_csv = ttk.Label(self.CsvBottoni_LabelFrame, text="Nessun File Selezionato")
        self.label_csv.grid(row=0, column=0, padx=20)

        ttk.Button(self.CsvBottoni_LabelFrame, text="Apri File", command=self.apri_csv).grid(row=1, column=0)
        ttk.Button(self.CsvBottoni_LabelFrame, text="Converti in Json", command=self.converti_in_json).grid(row=1, column=1)
        ttk.Button(self.CsvBottoni_LabelFrame, text="Reset", command=self.reset_csv).grid(row=1, column=2, padx=30)

        # Frame JSON
        self.Json_Frame = Frame(self.frame)
        self.Json_Frame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.JsonTab_LabelFrame = LabelFrame(self.Json_Frame, text="Json File")
        self.JsonTab_LabelFrame.pack(fill=BOTH, expand=True, ipady=225)

        self.tree_json = ttk.Treeview(self.JsonTab_LabelFrame)
        self.tree_json.pack(fill=BOTH, expand=True)

        self.scroll_y_json = ttk.Scrollbar(self.tree_json, orient=VERTICAL, command=self.tree_json.yview)
        self.scroll_x_json = ttk.Scrollbar(self.tree_json, orient=HORIZONTAL, command=self.tree_json.xview)
        self.scroll_y_json.pack(side=RIGHT, fill=Y)
        self.scroll_x_json.pack(side=BOTTOM, fill=X)
        self.tree_json.configure(yscrollcommand=self.scroll_y_json.set, xscrollcommand=self.scroll_x_json.set)

        self.JsonBottoni_LabelFrame = LabelFrame(self.Json_Frame, text="Apri e Converti")
        self.JsonBottoni_LabelFrame.pack(fill=BOTH, pady=5)

        self.label_json = ttk.Label(self.JsonBottoni_LabelFrame, text="Nessun File Selezionato")
        self.label_json.grid(row=0, column=0, padx=20)

        ttk.Button(self.JsonBottoni_LabelFrame, text="Apri File", command=self.apri_json).grid(row=1, column=0)
        ttk.Button(self.JsonBottoni_LabelFrame, text="Converti in Csv", command=self.converti_in_csv).grid(row=1, column=1)
        ttk.Button(self.JsonBottoni_LabelFrame, text="Reset", command=self.reset_json).grid(row=1, column=2, padx=30)

    # Metodi CSV
    def apri_csv(self):
        if not self.NomeFile_Csv:
            self.NomeFile_Csv = filedialog.askopenfilename(title="Apri un file", filetypes=[("csv files","*.csv")])
        if not self.NomeFile_Csv: return
        self.label_csv["text"] = self.NomeFile_Csv
        try:
            self.df_csv = pd.read_csv(self.NomeFile_Csv)
            self._popola_tree(self.tree_csv, self.df_csv)
        except Exception as e:
            self.NomeFile_Csv = None
            messagebox.showerror("Errore", f"{e}")

    def converti_in_json(self):
        if self.df_csv is None:
            messagebox.showinfo("Info", "Apri prima un file CSV")
            return
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Json files","*.json")])
        if not path: return
        try:
            self.df_csv.to_json(path, orient="records", indent=4)
            self.NomeFile_Json = path
            self.apri_json()
        except Exception as e:
            messagebox.showerror("Errore", f"{e}")

    def reset_csv(self):
        self.label_csv["text"] = "Nessun File Selezionato"
        for r in self.tree_csv.get_children(): self.tree_csv.delete(r)
        self.tree_csv["columns"] = ()
        self.NomeFile_Csv = None

    # Metodi JSON
    def apri_json(self):
        if not self.NomeFile_Json:
            self.NomeFile_Json = filedialog.askopenfilename(title="Apri un file", filetypes=[("Json files","*.json")])
        if not self.NomeFile_Json: return
        self.label_json["text"] = self.NomeFile_Json
        try:
            with open(self.NomeFile_Json, "r") as f:
                data = json.load(f)
            self.df_json = pd.DataFrame(data)
            self._popola_tree(self.tree_json, self.df_json)
        except Exception as e:
            self.NomeFile_Json = None
            messagebox.showerror("Errore", f"{e}")

    def converti_in_csv(self):
        if self.df_json is None:
            messagebox.showinfo("Info", "Apri prima un file JSON")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Csv files","*.csv")])
        if not path: return
        try:
            self.df_json.to_csv(path, index=False)
            self.NomeFile_Csv = path
            self.apri_csv()
        except Exception as e:
            messagebox.showerror("Errore", f"{e}")

    def reset_json(self):
        self.label_json["text"] = "Nessun File Selezionato"
        for r in self.tree_json.get_children(): self.tree_json.delete(r)
        self.tree_json["columns"] = ()
        self.NomeFile_Json = None

    # Metodo comune
    def _popola_tree(self, tree, df):
        tree.delete(*tree.get_children())
        tree["columns"] = list(df.columns)
        tree["show"] = "headings"
        for col in df.columns:
            tree.heading(col, text=col)
        for row in df.to_numpy().tolist():
            tree.insert("", "end", values=row)
