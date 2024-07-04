import pymongo
from pymongo import MongoClient


#Classe che ci consente di effettuare una connessione con mongodb cloud in modo da poter effettuare login e signup 
class connessione():
    def __init__(self):
        self.client = MongoClient('mongodb+srv://nicoangioi75:CYnt5M30kvLAqaGP@cluster0.ydx7iah.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        self.db = self.client.PyMongo

        self.CollezioneUtenti = self.db.utenti

