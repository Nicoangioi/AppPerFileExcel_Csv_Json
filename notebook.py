from tkinter import BOTH
from tkinter import ttk

from tab_excel_csv import ExcelCsvTab
from tab_csv_json import CsvJsonTab
from tab_excel_json import ExcelJsonTab

class MainNotebook:
    def __init__(self, root):
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=BOTH, expand=True, pady=15)

        # Creo e aggiungo le schede
        self.tab_excel_csv = ExcelCsvTab(self.notebook)
        self.tab_csv_json = CsvJsonTab(self.notebook)
        self.tab_excel_json = ExcelJsonTab(self.notebook)

        self.notebook.add(self.tab_excel_csv.frame, text="Excel/Csv")
        self.notebook.add(self.tab_csv_json.frame, text="Csv/Json")
        self.notebook.add(self.tab_excel_json.frame, text="Excel/Json")
