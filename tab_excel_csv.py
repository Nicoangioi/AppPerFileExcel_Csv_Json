from tkinter import *
from tkinter import ttk, filedialog, messagebox
import pandas as pd

class ExcelCsvTab:
    def __init__(self, notebook):
        self.frame = Frame(notebook)
        self.NomeFile_Excel = None
        self.NomeFile_Csv = None
        self.df_excel = None
        self.df_csv = None

        self._crea_ui()

    def _crea_ui(self):
        # Frame per Excel
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

        # Bottoni Excel
        self.ExcelBottoni_LabelFrame = LabelFrame(self.Excel_Frame, text="Apri e Converti")
        self.ExcelBottoni_LabelFrame.pack(fill=BOTH, pady=5)

        self.label_excel = ttk.Label(self.ExcelBottoni_LabelFrame, text="Nessun File Selezionato")
        self.label_excel.grid(row=0, column=0, padx=20)

        ttk.Button(self.ExcelBottoni_LabelFrame, text="Apri File", command=self.apri_excel).grid(row=1, column=0)
        ttk.Button(self.ExcelBottoni_LabelFrame, text="Converti in Csv", command=self.converti_in_csv).grid(row=1, column=1)
        ttk.Button(self.ExcelBottoni_LabelFrame, text="Reset", command=self.reset_excel).grid(row=1, column=2, padx=30)

        # Frame per CSV
        self.Csv_Frame = Frame(self.frame)
        self.Csv_Frame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.CsvTab_LabelFrame = LabelFrame(self.Csv_Frame, text="Csv File")
        self.CsvTab_LabelFrame.pack(fill=BOTH, expand=True, ipady=225)

        self.tree_csv = ttk.Treeview(self.CsvTab_LabelFrame)
        self.tree_csv.pack(fill=BOTH, expand=True)

        self.scroll_y_csv = ttk.Scrollbar(self.tree_csv, orient=VERTICAL, command=self.tree_csv.yview)
        self.scroll_x_csv = ttk.Scrollbar(self.tree_csv, orient=HORIZONTAL, command=self.tree_csv.xview)
        self.scroll_y_csv.pack(side=RIGHT, fill=Y)
        self.scroll_x_csv.pack(side=BOTTOM, fill=X)
        self.tree_csv.configure(yscrollcommand=self.scroll_y_csv.set, xscrollcommand=self.scroll_x_csv.set)

        # Bottoni CSV
        self.CsvBottoni_LabelFrame = LabelFrame(self.Csv_Frame, text="Apri e Converti")
        self.CsvBottoni_LabelFrame.pack(fill=BOTH, pady=5)

        self.label_csv = ttk.Label(self.CsvBottoni_LabelFrame, text="Nessun File Selezionato")
        self.label_csv.grid(row=0, column=0, padx=20)

        ttk.Button(self.CsvBottoni_LabelFrame, text="Apri File", command=self.apri_csv).grid(row=1, column=0)
        ttk.Button(self.CsvBottoni_LabelFrame, text="Converti in Excel", command=self.converti_in_excel).grid(row=1, column=1)
        ttk.Button(self.CsvBottoni_LabelFrame, text="Reset", command=self.reset_csv).grid(row=1, column=2, padx=30)

    # Metodi per Excel
    def apri_excel(self):
        if not self.NomeFile_Excel:
            self.NomeFile_Excel = filedialog.askopenfilename(title="Apri un file", filetypes=[("xlsx files", "*.xlsx")])
        if not self.NomeFile_Excel: return
        self.label_excel["text"] = self.NomeFile_Excel
        try:
            self.df_excel = pd.read_excel(self.NomeFile_Excel)
            self._popola_tree(self.tree_excel, self.df_excel)
        except Exception as e:
            self.NomeFile_Excel = None
            messagebox.showerror("Errore", f"{e}")

    def converti_in_csv(self):
        if self.df_excel is None:
            messagebox.showinfo("Info", "Apri prima un file Excel")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files","*.csv")])
        if not path: return
        try:
            self.df_excel.to_csv(path, index=False)
            self.NomeFile_Csv = path
            self.apri_csv()
        except Exception as e:
            messagebox.showerror("Errore", f"{e}")

    def reset_excel(self):
        self.label_excel["text"] = "Nessun File Selezionato"
        for r in self.tree_excel.get_children(): self.tree_excel.delete(r)
        self.tree_excel["columns"] = ()
        self.NomeFile_Excel = None

    # Metodi per CSV
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

    def converti_in_excel(self):
        if self.df_csv is None:
            messagebox.showinfo("Info", "Apri prima un file CSV")
            return
        path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files","*.xlsx")])
        if not path: return
        try:
            self.df_csv.to_excel(path, index=False)
            self.NomeFile_Excel = path
            self.apri_excel()
        except Exception as e:
            messagebox.showerror("Errore", f"{e}")

    def reset_csv(self):
        self.label_csv["text"] = "Nessun File Selezionato"
        for r in self.tree_csv.get_children(): self.tree_csv.delete(r)
        self.tree_csv["columns"] = ()
        self.NomeFile_Csv = None

    # Metodo comune per popolare treeview
    def _popola_tree(self, tree, df):
        tree.delete(*tree.get_children())
        tree["columns"] = list(df.columns)
        tree["show"] = "headings"
        for col in df.columns:
            tree.heading(col, text=col)
        for row in df.to_numpy().tolist():
            tree.insert("", "end", values=row)
