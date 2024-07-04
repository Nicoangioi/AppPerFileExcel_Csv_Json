def Apri_File_Excel(self):
        if self.NomeFile_Excel is None:
            self.NomeFile_Excel = filedialog.askopenfilename(title="Apri un file", initialdir="/",filetypes=(("xlsx files","*.xlsx"),("All Files","*.*")))
        
        self.label_NomeFile_Excel["text"] = self.NomeFile_Excel

        try:
            self.df_excel = pd.read_excel(self.NomeFile_Excel)
        except ValueError:
            messagebox.showerror(title="Info",message="il file scelto non è valido")
        except FileNotFoundError:
            messagebox.showerror(title="Info",message="File non trovato")
        


        self.tree_excel["column"] = list(self.df_excel.columns)
        self.tree_excel["show"] = "headings"

        for colonna in self.tree_excel["columns"]:
            self.tree_excel.heading(colonna, text=colonna)

        #Cambiare le righe del dataframe in righe di numpy che trasformeremo in list
        self.righe_df_excel = self.df_excel.to_numpy().tolist()

        #Adesso possiamo inserire i dati nella tabella
        for riga in self.righe_df_excel:
            self.tree_excel.insert("","end",values=riga)

        

        
    def Converti_In_Csv(self):
        if self.NomeFile_Excel is None:
            messagebox.showinfo(title="info",message="Inserisci prima un file")

        if self.NomeFile_Excel:
            
            path = filedialog.asksaveasfilename(defaultextension=".csv",filetypes=[("CSV files", "*.csv")],title="Salva il file CSV")
            self.df_excel.to_csv(path, index=False)
            messagebox.showinfo(title="info",message="Conversione avvenuta con successo")
            self.NomeFile_Csv = path
            self.ApriCsvFile()

    def ApriCsvFile(self):
        if self.NomeFile_Csv is None:
            self.NomeFile_Csv = filedialog.askopenfilename(title="Apri un file", initialdir="/",filetypes=(("csv files","*.csv"),("All Files","*.*")))

        self.label_NomeFile_Csv["text"] = self.NomeFile_Csv

        try:
            self.df_csv = pd.read_csv(self.NomeFile_Csv)
        except ValueError:
            messagebox.showerror(title="Info",message="il file scelto non è valido")
        except FileNotFoundError:
            messagebox.showerror(title="Info",message="File non trovato")
            


        self.tree_csv["column"] = list(self.df_csv.columns)
        self.tree_csv["show"] = "headings"

        for colonna in self.tree_csv["columns"]:
            self.tree_csv.heading(colonna,text=colonna)

        self.righe_df_csv = self.df_csv.to_numpy().tolist()

        for riga in self.righe_df_csv:
            self.tree_csv.insert("","end",values=riga)

    def Converti_In_Excel(self):
        if self.NomeFile_Csv is None:
            messagebox.showinfo(title="info",message="Inserisci prima un file")
        
        if self.NomeFile_Csv:
            path = filedialog.asksaveasfilename(defaultextension=".csv",filetypes=[("xlsx", "*.xlsx")],title="Salva il file Excel")
            self.df_csv.to_excel(path, index=False)
            messagebox.showinfo(title="info",message="Conversione avvenuta con successo")
            self.NomeFile_Excel = path
            self.Apri_File_Excel()
    
    def Reset_Dati_Excel(self):

        self.label_NomeFile_Excel["text"] = "Nessun File Selezionato"

        for righe in self.tree_excel.get_children():
            self.tree_excel.delete(righe)

        for colonna in self.tree_excel["columns"]:
            self.tree_excel.heading(colonna,text="")
            # self.tree_excel.column(colonna,width=0)
        
        self.tree_excel["columns"] = ()

        

    def Reset_Dati_Csv(self):
        for righe in self.tree_csv.get_children():
            self.tree_csv.delete(righe)
        
        for colonna in self.tree_csv["columns"]:
            self.tree_csv.heading(colonna,text=colonna)

        self.tree_csv["columns"] = ()