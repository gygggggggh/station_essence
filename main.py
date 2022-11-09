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

    def defiler(self):
        if self.est_vide():
            raise MemoryError("File vide")
        return self.file.pop(0)


def random_voiture():
    return random.choice(voitures)

def random_client():
    return random.choice(clients)

print(random_voiture())
print(random_client())

