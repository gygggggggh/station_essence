# projet staion essance 
import random
from csv import reader

with open("voitures.csv" , "r") as v ,open("clients.csv", "r") as c:
    reader1 = reader(v)
    reader2 = reader(c)
    voitures = list(reader1)
    clients = list(reader2)


class waiting_line:
    def __init__(self):
        self.file = []
        
    def __str__(self):
        txt = ""
        for i in self.file:
            txt += str(i) + " <- "
        return txt
    
    def est_vide(self):
        return self.file == []
    
    def enfiler(self, x):
        self.file.append(x)

with open("voitures.csv", "r") as file , open("clients.csv","r") as file2:
    v = reader(file)
    c = reader(file2)
    voitures = list(v)
    clients = list(c)

print(clients[0][2])
print(voitures[0][2])

print(random_voiture())
print(random_client())

k = [voitures[1],clients[1]]

print(k[0][2])