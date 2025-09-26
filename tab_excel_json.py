from tkinter import *
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import json

class ExcelJsonTab:
    def __init__(self, notebook):
        self.frame = Frame(notebook)
        self.NomeFile_Excel = None
        self.NomeFile_Json = None
        self.df_excel = None
        self.df_json = None

        self._crea_ui()

    def _crea_ui(self):
        # Frame Excel
        self.Excel_Frame = Frame(self.frame)
        self.Excel_Frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.ExcelTab_LabelFrame = LabelFrame(self.Excel_Frame, text="Excel File")
        self.ExcelTab_LabelFrame.pack(fill=BOTH, expand=True, ipady=225)

        self.tree_excel = ttk.Treeview(self.ExcelTab_LabelFrame)
        self.tree_excel.pack(fill=BOTH, expand=True)

        self.scroll_y_excel = ttk.Scrollbar(self.tree_excel, orient=VERTICAL, command=self.tree_excel.yview)
        self.scroll_x_excel = ttk.Scrollbar(self.tree_excel, orient=HORIZONTAL, command=self.tree_excel.xview)
        self.scroll_y_excel.pack(side=RIGHT, fill=Y)
        self.scroll_x_excel.pack(side=BOTTOM, fill=X)
        self.tree_excel.configure(yscrollcommand=self.scroll_y_excel.set, xscrollcommand=self.scroll_x_excel.set)

        self.ExcelBottoni_LabelFrame = LabelFrame(self.Excel_Frame, text="Apri e Converti")
        self.ExcelBottoni_LabelFrame.pack(fill=BOTH, pady=5)

        self.label_excel = ttk.Label(self.ExcelBottoni_LabelFrame, text="Nessun File Selezionato")
        self.label_excel.grid(row=0, column=0, padx=20)

        ttk.Button(self.ExcelBottoni_LabelFrame, text="Apri File", command=self.apri_excel).grid(row=1, column=0)
        ttk.Button(self.ExcelBottoni_LabelFrame, text="Converti in Json", command=self.converti_in_json).grid(row=1, column=1)
        ttk.Button(self.ExcelBottoni_LabelFrame, text="Reset", command=self.reset_excel).grid(row=1, column=2, padx=30)

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
        ttk.Button(self.JsonBottoni_LabelFrame, text="Converti in Excel", command=self.converti_in_excel).grid(row=1, column=1)
        ttk.Button(self.JsonBottoni_LabelFrame, text="Reset", command=self.reset_json).grid(row=1, column=2, padx=30)

    # Metodi Excel
    def apri_excel(self):
        if not self.NomeFile_Excel:
            self.NomeFile_Excel = filedialog.askopenfilename(title="Apri un file", filetypes=[("xlsx files","*.xlsx")])
        if not self.NomeFile_Excel: return
        self.label_excel["text"] = self.NomeFile_Excel
        try:
            self.df_excel = pd.read_excel(self.NomeFile_Excel)
            self._popola_tree(self.tree_excel, self.df_excel)
        except Exception as e:
            self.NomeFile_Excel = None
            messagebox.showerror("Errore", f"{e}")

    def converti_in_json(self):
        if self.df_excel is None:
            messagebox.showinfo("Info", "Apri prima un file Excel")
            return
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Json files","*.json")])
        if not path: return
        try:
            self.df_excel.to_json(path, orient="records", indent=4)
            self.NomeFile_Json = path
            self.apri_json()
        except Exception as e:
            messagebox.showerror("Errore", f"{e}")

    def reset_excel(self):
        self.label_excel["text"] = "Nessun File Selezionato"
        for r in self.tree_excel.get_children(): self.tree_excel.delete(r)
        self.tree_excel["columns"] = ()
        self.NomeFile_Excel = None

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

    def converti_in_excel(self):
        if self.df_json is None:
            messagebox.showinfo("Info", "Apri prima un file JSON")
            return
        path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files","*.xlsx")])
        if not path: return
        try:
            self.df_json.to_excel(path, index=False)
            self.NomeFile_Excel = path
            self.apri_excel()
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
