from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import pandas as pd



class main():
    def __init__(self):
        self.root = Tk()
        self.root.title("Applicazione")
        self.root.geometry("1920x1080")

        #inizializziamo la variabile utile per contenere il percorso del file da aprire  (se il file non è stato ancora importato chiedere il nome del file da convertire)
        self.NomeFile_Excel_Tab1 = None
        self.NomeFile_Csv_Tab1 = None

        



        self.NomeFile_Csv_Tab2 = None
        self.NomeFile_Json_Tab2 = None

        self.NomeFile_Excel_Tab3 = None
        self.NomeFile_Json_Tab3 = None

        self.display()


        self.root.mainloop()

    def display(self):
        


        #Creazione del notebook con le tab e i relativi frame iniziali


        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=BOTH, expand=True, pady= 15)

        self.Excel_Csv_frame = Frame(self.notebook)
        self.Excel_Csv_frame.pack()

        self.Csv_Json_frame = Frame(self.notebook)
        self.Csv_Json_frame.pack()

        self.Excel_Json_frame = Frame(self.notebook)
        self.Excel_Csv_frame.pack()

        self.notebook.add(self.Excel_Csv_frame,text="Excel/Csv")
        self.notebook.add(self.Csv_Json_frame,text="Csv/Json")
        self.notebook.add(self.Excel_Json_frame,text="Excel/Json")





        #---------------------------------------------------------------Creazione widget per la tab Excel_Csv--------------------------------------------------------------------------------




        #Creazione di frame separati per predisporli meglio all'imterno delle tab

        self.Excel_FrameTab1 = Frame(self.Excel_Csv_frame)
        self.Excel_FrameTab1.pack(side=LEFT,fill=BOTH,expand=True)

        self.Csv_FrameTab1 = Frame(self.Excel_Csv_frame)
        self.Csv_FrameTab1.pack(side=RIGHT,fill=BOTH,expand=True)
        
        #Creazione di label frame appositi per le tabella (treeview)

        #Creazione di label frame per la tabella excel
        self.ExcelTab_LabelFrame_Tab1 = LabelFrame(self.Excel_FrameTab1, text="Excel File")
        self.ExcelTab_LabelFrame_Tab1.pack(side = TOP,fill=BOTH,expand=True, ipady=225)

        #Creazione tabella/treeview per i file excel + scrollbar
        self.tree_excel_Tab1 = ttk.Treeview(self.ExcelTab_LabelFrame_Tab1)
        self.tree_excel_Tab1.pack(fill=BOTH,expand=True)

        self.treescrolly_excel_Tab1 = ttk.Scrollbar(self.tree_excel_Tab1, orient="vertical",command=self.tree_excel_Tab1.yview)
        self.treescrollx_excel_Tab1 = ttk.Scrollbar(self.tree_excel_Tab1, orient="horizontal",command=self.tree_excel_Tab1.xview)
        self.treescrollx_excel_Tab1.pack(side=BOTTOM,fill=X)
        self.treescrolly_excel_Tab1.pack(side=RIGHT,fill=Y)
        
        self.tree_excel_Tab1.configure(xscrollcommand=self.treescrollx_excel_Tab1.set,yscrollcommand=self.treescrolly_excel_Tab1.set)



        #Creazione di label frame per la tabella csv
        self.CsvTab_LabelFrame_Tab1 = LabelFrame(self.Csv_FrameTab1,text="Csv File")
        self.CsvTab_LabelFrame_Tab1.pack(side=TOP,fill=BOTH,expand=True, ipady=225)

        #Creazione tabella/treeview per i file csv + scrollbar
        self.tree_csv_Tab1 = ttk.Treeview(self.CsvTab_LabelFrame_Tab1)
        self.tree_csv_Tab1.pack(fill=BOTH,expand=True)

        self.treescrolly_csv_Tab1 = ttk.Scrollbar(self.tree_csv_Tab1, orient="vertical",command=self.tree_csv_Tab1.yview)
        self.treescrollx_csv_Tab1 = ttk.Scrollbar(self.tree_csv_Tab1, orient="horizontal",command=self.tree_csv_Tab1.xview)
        self.treescrollx_csv_Tab1.pack(side=BOTTOM,fill=X)
        self.treescrolly_csv_Tab1.pack(side=RIGHT,fill=Y)
        self.tree_csv_Tab1.configure(xscrollcommand=self.treescrollx_csv_Tab1.set,yscrollcommand=self.treescrolly_csv_Tab1.set)

        

        #Creazione di labelFrame appositi per i bottoni
        self.ExcelBottoniTab1_LabelFrame = LabelFrame(self.Excel_FrameTab1,text="Apri e Converti")
        self.ExcelBottoniTab1_LabelFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        self.label_NomeFile_Excel_Tab1 = ttk.Label(self.ExcelBottoniTab1_LabelFrame, text="Nessun File Selezionato")
        self.label_NomeFile_Excel_Tab1.grid(row=0,column=0, padx=20)

        self.ApriFileExcelTab1 = ttk.Button(self.ExcelBottoniTab1_LabelFrame,text="Apri File", command=self.Apri_File_Excel_Tab1)
        self.ApriFileExcelTab1.grid(row= 1,column=0 )

        self.Converti_in_CsvTab1 = ttk.Button(self.ExcelBottoniTab1_LabelFrame,text="Converti in Csv", command=self.Converti_In_Csv_Tab1)
        self.Converti_in_CsvTab1.grid(row= 1,column=1 )

        self.Reset_Excel_Tab1 = ttk.Button(self.ExcelBottoniTab1_LabelFrame,text="Reset", command=self.Reset_Dati_Excel_Tab1)
        self.Reset_Excel_Tab1.grid(row=1,column=2, padx=30)

        self.CsvBottoni_LabelFrame_Tab1 = LabelFrame(self.Csv_FrameTab1,text="Apri e Converti")
        self.CsvBottoni_LabelFrame_Tab1.pack(side = BOTTOM,fill=BOTH,expand=True)

        self.label_NomeFile_Csv_Tab1 = ttk.Label(self.CsvBottoni_LabelFrame_Tab1, text="Nessun File Selezionato")
        self.label_NomeFile_Csv_Tab1.grid(row=0,column=0, padx=20)

        self.ApriFileCsvTab1 = ttk.Button(self.CsvBottoni_LabelFrame_Tab1, text="Apri File", command=self.ApriCsvFile_Tab1)
        self.ApriFileCsvTab1.grid(row=1,column=0)

        self.Converti_in_ExcelTab1 = ttk.Button(self.CsvBottoni_LabelFrame_Tab1, text="Converti in Excel", command=self.Converti_In_Excel_Tab1)
        self.Converti_in_ExcelTab1.grid(row=1,column=1)

        self.Reset_Csv_Tab1 = ttk.Button(self.CsvBottoni_LabelFrame_Tab1,text="Reset", command=self.Reset_Dati_Csv_Tab1)
        self.Reset_Csv_Tab1.grid(row=1,column=2, padx=30)



        #------------------------------------------------------------------Creazione widget per la tab Csv_Json---------------------------------------------------------------------------------

        #Creazione di due frame iniziali per separare i due tipi di file
        self.Csv_FrameTab2 = Frame(self.Csv_Json_frame)
        self.Csv_FrameTab2.pack(side=LEFT,fill=BOTH,expand=True)

        self.Json_FrameTab2 = Frame(self.Csv_Json_frame)
        self.Json_FrameTab2.pack(side=RIGHT,fill=BOTH,expand=True)

        #Creazione di Label frame per i file csv
        self.CsvTab_LabelFrame_Tab2 = ttk.LabelFrame(self.Csv_FrameTab2, text="Csv File")
        self.CsvTab_LabelFrame_Tab2.pack(side=TOP,fill=BOTH,expand=True, ipady=225)

        #Creazione della tabella treeview collegata al labelframe csv + scrollbar
        self.tree_csv_Tab2 = ttk.Treeview(self.CsvTab_LabelFrame_Tab2)
        self.tree_csv_Tab2.pack(fill=BOTH,expand=True)

        self.treescrolly_csv_Tab2 = ttk.Scrollbar(self.tree_csv_Tab2, orient="vertical",command=self.tree_csv_Tab2.yview)
        self.treescrollx_csv_Tab2 = ttk.Scrollbar(self.tree_csv_Tab2, orient="horizontal",command=self.tree_csv_Tab2.xview)
        self.treescrollx_csv_Tab2.pack(side=BOTTOM,fill=X)
        self.treescrolly_csv_Tab2.pack(side=RIGHT,fill=Y)

        self.tree_csv_Tab2.configure(xscrollcommand=self.treescrollx_csv_Tab2.set,yscrollcommand=self.treescrolly_csv_Tab2.set)
        

        #Creazione di Label frame per i file json
        self.JsonTab_LabelFrame_Tab2 = ttk.LabelFrame(self.Json_FrameTab2, text="Json File")
        self.JsonTab_LabelFrame_Tab2.pack(side=TOP,fill=BOTH,expand=True, ipady=225)

        #Creazione della tabella treeview collegata al labelframe json + scrollbar
        self.tree_json_Tab2 = ttk.Treeview(self.JsonTab_LabelFrame_Tab2)
        self.tree_json_Tab2.pack(fill=BOTH,expand=True)

        self.treescrolly_json_Tab2 = ttk.Scrollbar(self.tree_json_Tab2, orient="vertical",command=self.tree_json_Tab2.yview)
        self.treescrollx_json_Tab2 = ttk.Scrollbar(self.tree_json_Tab2, orient="horizontal",command=self.tree_json_Tab2.xview)
        self.treescrollx_json_Tab2.pack(side=BOTTOM,fill=X)
        self.treescrolly_json_Tab2.pack(side=RIGHT,fill=Y)

        self.tree_json_Tab2.configure(xscrollcommand=self.treescrollx_json_Tab2.set,yscrollcommand=self.treescrolly_json_Tab2.set)


        #Creazione dei label frame per appositi bottoni

        self.CsvBottoni_LabelFrame_Tab2 = ttk.LabelFrame(self.Csv_FrameTab2,text="Apri e Converti")
        self.CsvBottoni_LabelFrame_Tab2.pack(side=BOTTOM,fill=BOTH,expand=True)

        self.label_NomeFile_Csv_Tab2 = ttk.Label(self.CsvBottoni_LabelFrame_Tab2, text="Nessun File Selezionato")
        self.label_NomeFile_Csv_Tab2.grid(row=0,column=0,padx=20)

        self.ApriFileCsvTab2 = ttk.Button(self.CsvBottoni_LabelFrame_Tab2, text="Apri File", command=self.ApriCsvFile_Tab2)
        self.ApriFileCsvTab2.grid(row=1,column=0)

        self.Converti_in_Json_Tab2 = ttk.Button(self.CsvBottoni_LabelFrame_Tab2, text="Converti In Json",command=self.Converti_In_Json_Tab2)
        self.Converti_in_Json_Tab2.grid(row=1,column=1)

        self.Reset_Csv_Tab2 = ttk.Button(self.CsvBottoni_LabelFrame_Tab2, text="Reset", command=self.Reset_Dati_Csv_Tab2)
        self.Reset_Csv_Tab2.grid(row=1,column=2,padx=30)




        self.JsonBottoni_LabelFrame_Tab2 = ttk.LabelFrame(self.Json_FrameTab2,text="Apri e Converti")
        self.JsonBottoni_LabelFrame_Tab2.pack(side=BOTTOM, fill=BOTH,expand=True)

        self.label_NomeFile_Json_Tab2 = ttk.Label(self.JsonBottoni_LabelFrame_Tab2, text="Nessun File Selezionato")
        self.label_NomeFile_Json_Tab2.grid(row=0,column=0,padx=20)

        self.ApriFileJsonTab2 = ttk.Button(self.JsonBottoni_LabelFrame_Tab2, text="Apri File", command=self.ApriJsonFile_Tab2)
        self.ApriFileJsonTab2.grid(row=1,column=0)

        self.Converti_in_CsvTab2 = ttk.Button(self.JsonBottoni_LabelFrame_Tab2, text="Converti In Csv", command=self.Converti_In_Csv_Tab2)
        self.Converti_in_CsvTab2.grid(row=1,column=1)

        self.Reset_Json_Tab2 = ttk.Button(self.JsonBottoni_LabelFrame_Tab2, text="Reset", command=self.Reset_Dati_Json_Tab2)
        self.Reset_Json_Tab2.grid(row=1,column=2,padx=30)

        

        #--------------------------------------------Creazione Widget per la terza tab---------------------------------------------------------------


        #Creazione di due frame iniziali per separare i due tipi di file
        self.Excel_FrameTab3 = Frame(self.Excel_Json_frame)
        self.Excel_FrameTab3.pack(side=LEFT,fill=BOTH,expand=True)

        self.Json_FrameTab3 = Frame(self.Excel_Json_frame)
        self.Json_FrameTab3.pack(side=RIGHT,fill=BOTH,expand=True)

        #Creazione di Label frame per i file excel
        self.ExcelTab_LabelFrame_Tab3 = ttk.LabelFrame(self.Excel_FrameTab3, text="Excel File")
        self.ExcelTab_LabelFrame_Tab3.pack(side=TOP,fill=BOTH,expand=True, ipady=225)

        #Creazione della tabella treeview collegata al labelframe csv + scrollbar
        self.tree_excel_Tab3 = ttk.Treeview(self.ExcelTab_LabelFrame_Tab3)
        self.tree_excel_Tab3.pack(fill=BOTH,expand=True)

        self.treescrolly_excel_Tab3 = ttk.Scrollbar(self.tree_excel_Tab3, orient="vertical",command=self.tree_excel_Tab3.yview)
        self.treescrollx_excel_Tab3 = ttk.Scrollbar(self.tree_excel_Tab3, orient="horizontal",command=self.tree_excel_Tab3.xview)
        self.treescrollx_excel_Tab3.pack(side=BOTTOM,fill=X)
        self.treescrolly_excel_Tab3.pack(side=RIGHT,fill=Y)

        self.tree_excel_Tab3.configure(xscrollcommand=self.treescrollx_excel_Tab3.set,yscrollcommand=self.treescrolly_excel_Tab3.set)
        

        #Creazione di Label frame per i file json
        self.JsonTab_LabelFrame_Tab3 = ttk.LabelFrame(self.Json_FrameTab3, text="Json File")
        self.JsonTab_LabelFrame_Tab3.pack(side=TOP,fill=BOTH,expand=True, ipady=225)

        #Creazione della tabella treeview collegata al labelframe json + scrollbar
        self.tree_json_Tab3 = ttk.Treeview(self.JsonTab_LabelFrame_Tab3)
        self.tree_json_Tab3.pack(fill=BOTH,expand=True)

        self.treescrolly_json_Tab3 = ttk.Scrollbar(self.tree_json_Tab3, orient="vertical",command=self.tree_json_Tab3.yview)
        self.treescrollx_json_Tab3 = ttk.Scrollbar(self.tree_json_Tab3, orient="horizontal",command=self.tree_json_Tab3.xview)
        self.treescrollx_json_Tab3.pack(side=BOTTOM,fill=X)
        self.treescrolly_json_Tab3.pack(side=RIGHT,fill=Y)

        self.tree_json_Tab3.configure(xscrollcommand=self.treescrollx_json_Tab3.set,yscrollcommand=self.treescrolly_json_Tab3.set)


        #Creazione dei label frame per appositi bottoni

        self.ExcelBottoni_LabelFrame_Tab3 = ttk.LabelFrame(self.Excel_FrameTab3,text="Apri e Converti")
        self.ExcelBottoni_LabelFrame_Tab3.pack(side=BOTTOM,fill=BOTH,expand=True)

        self.label_NomeFile_Excel_Tab3 = ttk.Label(self.ExcelBottoni_LabelFrame_Tab3, text="Nessun File Selezionato")
        self.label_NomeFile_Excel_Tab3.grid(row=0,column=0,padx=20)

        self.ApriFileExcelTab3 = ttk.Button(self.ExcelBottoni_LabelFrame_Tab3, text="Apri File", command=self.ApriExcelFile_Tab3)
        self.ApriFileExcelTab3.grid(row=1,column=0)

        self.Converti_in_Json_Tab3 = ttk.Button(self.ExcelBottoni_LabelFrame_Tab3, text="Converti In Json",command=self.Converti_In_Json_Tab3)
        self.Converti_in_Json_Tab3.grid(row=1,column=1)

        self.Reset_Excel_Tab3 = ttk.Button(self.ExcelBottoni_LabelFrame_Tab3, text="Reset", command=self.Reset_Dati_Excel_Tab3)
        self.Reset_Excel_Tab3.grid(row=1,column=2,padx=30)




        self.JsonBottoni_LabelFrame_Tab3 = ttk.LabelFrame(self.Json_FrameTab3,text="Apri e Converti")
        self.JsonBottoni_LabelFrame_Tab3.pack(side=BOTTOM, fill=BOTH,expand=True)

        self.label_NomeFile_Json_Tab3 = ttk.Label(self.JsonBottoni_LabelFrame_Tab3, text="Nessun File Selezionato")
        self.label_NomeFile_Json_Tab3.grid(row=0,column=0,padx=20)

        self.ApriFileJsonTab3 = ttk.Button(self.JsonBottoni_LabelFrame_Tab3, text="Apri File", command=self.ApriJsonFile_Tab3)
        self.ApriFileJsonTab3.grid(row=1,column=0)

        self.Converti_in_ExcelTab3 = ttk.Button(self.JsonBottoni_LabelFrame_Tab3, text="Converti In Excel", command=self.Converti_In_Excel_Tab3)
        self.Converti_in_ExcelTab3.grid(row=1,column=1)

        self.Reset_Json_Tab3 = ttk.Button(self.JsonBottoni_LabelFrame_Tab3, text="Reset", command=self.Reset_Dati_Json_Tab3)
        self.Reset_Json_Tab3.grid(row=1,column=2,padx=30)











    #-----------------------------------------------------------------------------Metodi per la prima Tab-----------------------------------------------------------------------------------------






    #Metodo che ci consente di aprire un file excel e mostrarlo nella tabella con un bottone
    def Apri_File_Excel_Tab1(self):
        #se non è stato specificato ancora il nome del percorso di un file excel, lo chiediamo all'utente
        if self.NomeFile_Excel_Tab1 is None:
            self.NomeFile_Excel_Tab1 = filedialog.askopenfilename(title="Apri un file", initialdir="/",filetypes=(("xlsx files","*.xlsx"),))
        
        #settiamo la label con il percorso del file che dobbiamo aprire
        self.label_NomeFile_Excel_Tab1["text"] = self.NomeFile_Excel_Tab1

        
        try:
            #Leggiamo il file con pandas
            self.df_excel_Tab1 = pd.read_excel(self.NomeFile_Excel_Tab1)
    


            #mettiamo nella tabella le colonne del dataframe
            self.tree_excel_Tab1["column"] = list(self.df_excel_Tab1.columns)
            self.tree_excel_Tab1["show"] = "headings"

            #inseriamo gli headings della tabella con i nomi delle colonne del dataframe
            for colonna in self.tree_excel_Tab1["columns"]:
                self.tree_excel_Tab1.heading(colonna, text=colonna)

            #Cambiare le righe del dataframe in righe di numpy che trasformeremo in list
            self.righe_df_excel_Tab1 = self.df_excel_Tab1.to_numpy().tolist()

            #Adesso possiamo inserire le righe nella tabella
            for riga in self.righe_df_excel_Tab1:
                self.tree_excel_Tab1.insert("","end",values=riga)
        except Exception as e:
            #inizializziamo con None la variabile che contiene il percorso del file in memoria in modo che una volta Chiuso il file si potrà procedere con l'inserimento di un nuovo file
            self.NomeFile_Excel_Tab1 = None
            messagebox.showerror(title="Error",message=f"Errore{e}")


        



    

    #metodo che ci consente di convertire il dataframe di un file excel in un file csv
    def Converti_In_Csv_Tab1(self):

        #se non è stato specificato ancora il nome del percorso di un file excel ricordiamo all'utente di inserirne uno prima di effettuare quest'operazione
        if self.NomeFile_Excel_Tab1 is None:
            messagebox.showinfo(title="info",message="Inserisci prima un file")
        
        #Altrimenti
        else:
        
            
            try:

                #chiediamo all'utente dove desidera salvare il file csv
                path = filedialog.asksaveasfilename(defaultextension=".csv",filetypes=[("CSV files", "*.csv")],title="Salva il file CSV")
                #convertiamo il dataframe excel in un file csv
                self.df_excel_Tab1.to_csv(path, index=False)
                #Messaggio di successo
                messagebox.showinfo(title="info",message="Conversione avvenuta con successo")
                #Inizializziamo il percorso del file csv con il percorso dato dall'utente precedentemente 
                self.NomeFile_Csv_Tab1 = path
                #Chiamiamo il metodo per aprire il file csv appena creato
                self.ApriCsvFile_Tab1()
            except Exception as e:
                messagebox.showerror(title="Errore", message=f"Errore:{e}")

    #Metodo che ci consente di aprire un file csv e mostrarlo nella tabella con un bottone
    def ApriCsvFile_Tab1(self):
        
        #se non è stato specificato ancora il nome del percorso di un file csv, lo chiediamo all'utente
        if self.NomeFile_Csv_Tab1 is None:
            self.NomeFile_Csv_Tab1 = filedialog.askopenfilename(title="Apri un file", initialdir="/",filetypes=(("csv files","*.csv"),))

        #settiamo la label con il percorso del file che dobbiamo aprire
        self.label_NomeFile_Csv_Tab1["text"] = self.NomeFile_Csv_Tab1

        
        try:
            #Leggiamo il file con pandas
            self.df_csv_Tab1 = pd.read_csv(self.NomeFile_Csv_Tab1)
        
    
            #mettiamo nella tabella le colonne del dataframe
            self.tree_csv_Tab1["column"] = list(self.df_csv_Tab1.columns)
            self.tree_csv_Tab1["show"] = "headings"

            #inseriamo gli headings della tabella con i nomi delle colonne del dataframe
            for colonna in self.tree_csv_Tab1["columns"]:
                self.tree_csv_Tab1.heading(colonna,text=colonna)

            #Cambiare le righe del dataframe in righe di numpy che trasformeremo in list
            self.righe_df_csv_Tab1 = self.df_csv_Tab1.to_numpy().tolist()

            #Adesso possiamo inserire le righe nella tabella
            for riga in self.righe_df_csv_Tab1:
                self.tree_csv_Tab1.insert("","end",values=riga)
        except Exception as e:
            #inizializziamo con None la variabile che contiene il percorso del file in memoria in modo che una volta Chiuso il file si potrà procedere con l'inserimento di un nuovo file
            self.NomeFile_Csv_Tab1 = None
            messagebox.showerror(title="Errore", message=f"Errore: {e}")

        
        


    
    #metodo che ci consente di convertire il dataframe di un file csv in un file excel
    def Converti_In_Excel_Tab1(self):
        #se non è stato specificato ancora il nome del percorso di un file csv, lo chiediamo all'utente
        if self.NomeFile_Csv_Tab1 is None:
            messagebox.showinfo(title="info",message="Inserisci prima un file")

        #Altrimenti
        else:
            try:
                
                #chiediamo all'utente dove desidera salvare il file excel
                path = filedialog.asksaveasfilename(defaultextension=".xlsx",filetypes=[("xlsx", "*.xlsx")],title="Salva il file Excel")
                #convertiamo il dataframe csv in un file excel
                self.df_csv_Tab1.to_excel(path, index=False)
                #Messaggio di successo
                messagebox.showinfo(title="info",message="Conversione avvenuta con successo")
                #Inizializziamo il percorso del file csv con il percorso dato dall'utente precedentemente 
                self.NomeFile_Excel_Tab1 = path
                #Chiamiamo il metodo per aprire il file csv appena creato
                self.Apri_File_Excel_Tab1()
            except Exception as e:
                messagebox.showerror(title="Errore", message=f"Errore: {e}")
            
    
    #metodo che ci consente di chiudere il file che abbiamo aperto e visualizzato/resettare i dati dalla tabella
    def Reset_Dati_Excel_Tab1(self):

        #Rinominiamo la label che indica il percorso del file
        self.label_NomeFile_Excel_Tab1["text"] = "Nessun File Selezionato"

        #Eliminiamo ogni riga nella tabella
        for righe in self.tree_excel_Tab1.get_children():
            self.tree_excel_Tab1.delete(righe)

        #Rinominimao le colonne della tabella
        for colonna in self.tree_excel_Tab1["columns"]:
            self.tree_excel_Tab1.heading(colonna,text="")
        
        #Impostiamo le colonne della tabella come vuote
        self.tree_excel_Tab1["columns"] = ()

        #inizializziamo con None la variabile che contiene il percorso del file in memoria in modo che una volta Chiuso il file si potrà procedere con l'inserimento di un nuovo file
        self.NomeFile_Excel_Tab1 = None

        



    #metodo che ci consente di chiudere il file che abbiamo aperto e visualizzato/resettare i dati dalla tabella
    def Reset_Dati_Csv_Tab1(self):

        #Rinominiamo la label che indica il percorso del file
        self.label_NomeFile_Csv_Tab1["text"] = "Nessun File Selezionato"

        #Eliminiamo ogni riga nella tabella
        for righe in self.tree_csv_Tab1.get_children():
            self.tree_csv_Tab1.delete(righe)
        
        #Rinominimao le colonne della tabella
        for colonna in self.tree_csv_Tab1["columns"]:
            self.tree_csv_Tab1.heading(colonna,text=colonna)

        #Impostiamo le colonne della tabella come vuote
        self.tree_csv_Tab1["columns"] = ()

        #inizializziamo con None la variabile che contiene il percorso del file in memoria in modo che una volta Chiuso il file si potrà procedere con l'inserimento di un nuovo file
        self.NomeFile_Csv_Tab1 = None

            

















    #--------------------------------------------------------------------------Metodi per la seconda Tab--------------------------------------------------------------------------------------

    #Metodo che ci consente di aprire e visualizzare un file csv e mostrarlo nella tabella con un bottone
    def ApriCsvFile_Tab2(self):
        
        #se non è stato specificato ancora il nome del percorso di un file csv, lo chiediamo all'utente
        if self.NomeFile_Csv_Tab2 is None:
            self.NomeFile_Csv_Tab2 = filedialog.askopenfilename(title="Apri un file",initialdir="/", filetypes=(("csv files","*.csv"),))
        

        #settiamo la label con il percorso del file che dobbiamo aprire
        self.label_NomeFile_Csv_Tab2["text"] = self.NomeFile_Csv_Tab2


        try:
            #Leggiamo il file con pandas
            self.df_csv_Tab2 = pd.read_csv(self.NomeFile_Csv_Tab2)

            #mettiamo nella tabella le colonne del dataframe
            self.tree_csv_Tab2["column"] = list(self.df_csv_Tab2.columns)
            self.tree_csv_Tab2["show"] = "headings"


            #inseriamo gli headings della tabella con i nomi delle colonne del dataframe
            for colonna in self.tree_csv_Tab2["columns"]:
                self.tree_csv_Tab2.heading(colonna, text=colonna)

            #Cambiare le righe del dataframe in righe di numpy che trasformeremo in list
            self.righe_df_csv_Tab2 = self.df_csv_Tab2.to_numpy().tolist()

            #Adesso possiamo inserire le righe nella tabella
            for riga in self.righe_df_csv_Tab2:
                self.tree_csv_Tab2.insert("","end",values=riga)
        except Exception as e:
            #inizializziamo con None la variabile che contiene il percorso del file in memoria in modo che una volta Chiuso il file si potrà procedere con l'inserimento di un nuovo file
            self.NomeFile_Csv_Tab2 = None
            messagebox.showerror(title="Error",message=f"Errore{e}")

    

                                                
    #metodo che ci consente di convertire il dataframe di un file csv in un file json
    def Converti_In_Json_Tab2(self):
        
        #se non è stato specificato ancora il nome del percorso di un file csv, lo chiediamo all'utente
        if self.NomeFile_Csv_Tab2 is None:
            messagebox.showinfo(title="info",message="Inserisci prima un file")

        #Altrimenti
        else:

            try:
                
                #chiediamo all'utente dove desidera salvare il file json
                path = filedialog.asksaveasfilename(defaultextension=".json",filetypes=[("Json files","*.json")], title="Salva il file Json")
                #convertiamo il dataframe csv in un file json
                self.df_csv_Tab2.to_json(path,index=False)
                #Messaggio di successo
                messagebox.showinfo(title="info",message="Conversione avvenuta con successo")
                #Inizializziamo il percorso del file json con il percorso dato dall'utente precedentemente
                self.NomeFile_Json_Tab2 = path
                #Chiamiamo il metodo per aprire il file json appena creato
                self.ApriJsonFile_Tab2()
            except Exception as e:
                messagebox.showerror(title="Errore", message=f"Errore:{e}")
    

    #metodo che ci consente di chiudere il file che abbiamo aperto e visualizzato/resettare i dati dalla tabella
    def Reset_Dati_Csv_Tab2(self):
        
        #Rinominiamo la label che indica il percorso del file
        self.label_NomeFile_Csv_Tab2["text"] = "Nessun File Selezionato"

        #Eliminiamo ogni riga nella tabella
        for righe in self.tree_csv_Tab2.get_children():
            self.tree_csv_Tab2.delete(righe)

        
        #Rinominimao le colonne della tabella
        for colonna in self.tree_csv_Tab2["columns"]:
            self.tree_csv_Tab2.heading(colonna,text=colonna)

        #Impostiamo le colonne della tabella come vuote
        self.tree_csv_Tab2["columns"] = ()

        #inizializziamo con None la variabile che contiene il percorso del file in memoria in modo che una volta Chiuso il file si potrà procedere con l'inserimento di un nuovo file
        self.NomeFile_Csv_Tab2 = None

    


    #Metodo che ci consente di aprire un file json e mostrarlo nella tabella con un bottone
    def ApriJsonFile_Tab2(self):

        #se non è stato specificato ancora il nome del percorso di un file json, lo chiediamo all'utente
        if self.NomeFile_Json_Tab2 is None:
            self.NomeFile_Json_Tab2 = filedialog.askopenfilename(title="Apri un file",initialdir="/", filetypes=(("json files","*.json"),))
        

        #settiamo la label con il percorso del file che dobbiamo aprire
        self.label_NomeFile_Json_Tab2["text"] = self.NomeFile_Json_Tab2


        try:
            #Leggiamo il file con pandas
            self.df_json_Tab2 = pd.read_json(self.NomeFile_Json_Tab2)

            #mettiamo nella tabella le colonne del dataframe
            self.tree_json_Tab2["column"] = list(self.df_json_Tab2.columns)
            self.tree_json_Tab2["show"] = "headings"


            #inseriamo gli headings della tabella con i nomi delle colonne del dataframe
            for colonna in self.tree_json_Tab2["columns"]:
                self.tree_json_Tab2.heading(colonna, text=colonna)
            
            #Cambiare le righe del dataframe in righe di numpy che trasformeremo in list
            self.righe_df_json_Tab2 = self.df_json_Tab2.to_numpy().tolist()

            #Adesso possiamo inserire le righe nella tabella
            for riga in self.righe_df_json_Tab2:
                self.tree_json_Tab2.insert("","end",values=riga)
        except Exception as e:
            #inizializziamo con None la variabile che contiene il percorso del file in memoria in modo che una volta Chiuso il file si potrà procedere con l'inserimento di un nuovo file
            self.NomeFile_Json_Tab2 = None
            messagebox.showerror(title="Error",message=f"Errore{e}")




    #metodo che ci consente di convertire il dataframe di un file excel in un file csv
    def Converti_In_Csv_Tab2(self):

        #se non è stato specificato ancora il nome del percorso di un file excel ricordiamo all'utente di inserirne uno prima di effettuare quest'operazione
        if self.NomeFile_Json_Tab2 is None:
            messagebox.showinfo(title="info",message="Inserisci prima un file")

        #Altrimenti
        else:

            try:

                #chiediamo all'utente dove desidera salvare il file csv
                path = filedialog.asksaveasfilename(defaultextension=".json",filetypes=[("Csv files","*.csv")], title="Salva il file Csv")
                #convertiamo il dataframe excel in un file csv
                self.df_json_Tab2.to_csv(path,index=False)
                #Messaggio di successo
                messagebox.showinfo(title="info",message="Conversione avvenuta con successo")
                #Inizializziamo il percorso del file csv con il percorso dato dall'utente precedentemente
                self.NomeFile_Csv_Tab2 = path
                #Chiamiamo il metodo per aprire il file csv appena creato
                self.ApriCsvFile_Tab2()
            except Exception as e:
                messagebox.showerror(title="Errore", message=f"Errore:{e}")



    #metodo che ci consente di chiudere il file che abbiamo aperto e visualizzato/resettare i dati dalla tabella
    def Reset_Dati_Json_Tab2(self):

        #Rinominiamo la label che indica il percorso del file
        self.label_NomeFile_Json_Tab2["text"] = "Nessun File Selezionato"

        #Eliminiamo ogni riga nella tabella
        for righe in self.tree_json_Tab2.get_children():
            self.tree_json_Tab2.delete(righe)

        
        #Rinominimao le colonne della tabella
        for colonna in self.tree_json_Tab2["columns"]:
            self.tree_json_Tab2.heading(colonna,text=colonna)

        
        #Impostiamo le colonne della tabella come vuote
        self.tree_json_Tab2["columns"] = ()


        #inizializziamo con None la variabile che contiene il percorso del file in memoria in modo che una volta Chiuso il file si potrà procedere con l'inserimento di un nuovo file
        self.NomeFile_Json_Tab2 = None


    



    #--------------------------------------------------------------------------Metodi per la terza Tab--------------------------------------------------------------------------------------





    #Metodo che ci consente di aprire un file excel e mostrarlo nella tabella con un bottone
    def ApriExcelFile_Tab3(self):
        #se non è stato specificato ancora il nome del percorso di un file excel, lo chiediamo all'utente
        if self.NomeFile_Excel_Tab3 is None:
            self.NomeFile_Excel_Tab3 = filedialog.askopenfilename(title="Apri un file", initialdir="/",filetypes=(("xlsx files","*.xlsx"),))
        
        #settiamo la label con il percorso del file che dobbiamo aprire
        self.label_NomeFile_Excel_Tab3["text"] = self.NomeFile_Excel_Tab3

        
        try:
            #Leggiamo il file con pandas
            self.df_excel_Tab3 = pd.read_excel(self.NomeFile_Excel_Tab3)
    


            #mettiamo nella tabella le colonne del dataframe
            self.tree_excel_Tab3["column"] = list(self.df_excel_Tab3.columns)
            self.tree_excel_Tab3["show"] = "headings"

            #inseriamo gli headings della tabella con i nomi delle colonne del dataframe
            for colonna in self.tree_excel_Tab3["columns"]:
                self.tree_excel_Tab3.heading(colonna, text=colonna)

            #Cambiare le righe del dataframe in righe di numpy che trasformeremo in list
            self.righe_df_excel_Tab3 = self.df_excel_Tab3.to_numpy().tolist()

            #Adesso possiamo inserire le righe nella tabella
            for riga in self.righe_df_excel_Tab3:
                self.tree_excel_Tab3.insert("","end",values=riga)
        except Exception as e:
            #inizializziamo con None la variabile che contiene il percorso del file in memoria in modo che una volta Chiuso il file si potrà procedere con l'inserimento di un nuovo file
            self.NomeFile_Excel_Tab3 = None
            messagebox.showerror(title="Error",message=f"Errore{e}")

    def Converti_In_Json_Tab3(self):
        #se non è stato specificato ancora il nome del percorso di un file csv, lo chiediamo all'utente
        if self.NomeFile_Excel_Tab3 is None:
            messagebox.showinfo(title="info",message="Inserisci prima un file")

        #Altrimenti
        else:

            try:
                
                #chiediamo all'utente dove desidera salvare il file json
                path = filedialog.asksaveasfilename(defaultextension=".json",filetypes=[("Json files","*.json")], title="Salva il file Json")
                #convertiamo il dataframe csv in un file json
                self.df_excel_Tab3.to_json(path,index=False)
                #Messaggio di successo
                messagebox.showinfo(title="info",message="Conversione avvenuta con successo")
                #Inizializziamo il percorso del file json con il percorso dato dall'utente precedentemente
                self.NomeFile_Json_Tab3 = path
                #Chiamiamo il metodo per aprire il file json appena creato
                self.ApriJsonFile_Tab3()
            except Exception as e:
                messagebox.showerror(title="Errore", message=f"Errore:{e}")



    #metodo che ci consente di chiudere il file che abbiamo aperto e visualizzato/resettare i dati dalla tabella
    def Reset_Dati_Excel_Tab3(self):
        #Rinominiamo la label che indica il percorso del file
        self.label_NomeFile_Excel_Tab3["text"] = "Nessun File Selezionato"

        #Eliminiamo ogni riga nella tabella
        for righe in self.tree_excel_Tab3.get_children():
            self.tree_excel_Tab3.delete(righe)

        #Rinominimao le colonne della tabella
        for colonna in self.tree_excel_Tab3["columns"]:
            self.tree_excel_Tab3.heading(colonna,text="")
        
        #Impostiamo le colonne della tabella come vuote
        self.tree_excel_Tab3["columns"] = ()

        #inizializziamo con None la variabile che contiene il percorso del file in memoria in modo che una volta Chiuso il file si potrà procedere con l'inserimento di un nuovo file
        self.NomeFile_Excel_Tab3 = None





    #Metodo che ci consente di aprire un file json e mostrarlo nella tabella con un bottone
    def ApriJsonFile_Tab3(self):
        #se non è stato specificato ancora il nome del percorso di un file json, lo chiediamo all'utente
        if self.NomeFile_Json_Tab3 is None:
            self.NomeFile_Json_Tab3 = filedialog.askopenfilename(title="Apri un file",initialdir="/", filetypes=(("json files","*.json"),))
        

        #settiamo la label con il percorso del file che dobbiamo aprire
        self.label_NomeFile_Json_Tab3["text"] = self.NomeFile_Json_Tab3


        try:
            #Leggiamo il file con pandas
            self.df_json_Tab3 = pd.read_json(self.NomeFile_Json_Tab3)

            #mettiamo nella tabella le colonne del dataframe
            self.tree_json_Tab3["column"] = list(self.df_json_Tab3.columns)
            self.tree_json_Tab3["show"] = "headings"


            #inseriamo gli headings della tabella con i nomi delle colonne del dataframe
            for colonna in self.tree_json_Tab3["columns"]:
                self.tree_json_Tab3.heading(colonna, text=colonna)
            
            #Cambiare le righe del dataframe in righe di numpy che trasformeremo in list
            self.righe_df_json_Tab3 = self.df_json_Tab3.to_numpy().tolist()

            #Adesso possiamo inserire le righe nella tabella
            for riga in self.righe_df_json_Tab3:
                self.tree_json_Tab3.insert("","end",values=riga)
        except Exception as e:
            #inizializziamo con None la variabile che contiene il percorso del file in memoria in modo che una volta Chiuso il file si potrà procedere con l'inserimento di un nuovo file
            self.NomeFile_json_Tab3 = None
            messagebox.showerror(title="Error",message=f"Errore{e}")




    #metodo che ci consente di convertire il dataframe di un file json in un file excel
    def Converti_In_Excel_Tab3(self):
        #se non è stato specificato ancora il nome del percorso di un file json, lo chiediamo all'utente
        if self.NomeFile_Json_Tab3 is None:
            messagebox.showinfo(title="info",message="Inserisci prima un file")

        #Altrimenti
        else:
            try:
                
                #chiediamo all'utente dove desidera salvare il file excel
                path = filedialog.asksaveasfilename(defaultextension=".xlsx",filetypes=[("xlsx", "*.xlsx")],title="Salva il file Excel")
                #convertiamo il dataframe json in un file excel
                self.df_json_Tab3.to_excel(path, index=False)
                #Messaggio di successo
                messagebox.showinfo(title="info",message="Conversione avvenuta con successo")
                #Inizializziamo il percorso del file excel con il percorso dato dall'utente precedentemente 
                self.NomeFile_Excel_Tab3 = path
                #Chiamiamo il metodo per aprire il file csv appena creato
                self.ApriExcelFile_Tab3()
            except Exception as e:
                messagebox.showerror(title="Errore", message=f"Errore: {e}")



    #metodo che ci consente di chiudere il file che abbiamo aperto e visualizzato/resettare i dati dalla tabella
    def Reset_Dati_Json_Tab3(self):
        
        #Rinominiamo la label che indica il percorso del file
        self.label_NomeFile_Json_Tab3["text"] = "Nessun File Selezionato"

        #Eliminiamo ogni riga nella tabella
        for righe in self.tree_json_Tab3.get_children():
            self.tree_json_Tab3.delete(righe)

        
        #Rinominimao le colonne della tabella
        for colonna in self.tree_json_Tab3["columns"]:
            self.tree_json_Tab3.heading(colonna,text=colonna)

        
        #Impostiamo le colonne della tabella come vuote
        self.tree_json_Tab3["columns"] = ()


        #inizializziamo con None la variabile che contiene il percorso del file in memoria in modo che una volta Chiuso il file si potrà procedere con l'inserimento di un nuovo file
        self.NomeFile_Json_Tab3 = None
