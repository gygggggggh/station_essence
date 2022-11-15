# projet staion essance 
import random
from csv import reader

with open("voitures.csv", "r") as file , open("clients.csv","r") as file2:
    v = reader(file)
    c = reader(file2)
    voitures = list(v)
    clients = list(c)


class File:
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



class Pompe:
    def __init__(self) -> None:
        self.pompe1 = File()
        self.pompe2 = File()
        self.pompe3 = File()
    def remplir_pompe(self):
        self.pompe1.enfiler([voitures[random.randint(1, len(voitures)-1)], clients[random.randint(1, len(clients)-1)]])
        self.pompe2.enfiler([voitures[random.randint(1, len(voitures)-1)], clients[random.randint(1, len(clients)-1)]])
        self.pompe3.enfiler([voitures[random.randint(1, len(voitures)-1)], clients[random.randint(1, len(clients)-1)]])
    def __str__(self) -> str:
        return f"pompe 1 : {self.pompe1} \npompe 2 : {self.pompe2} \npompe 3 : {self.pompe3}"

    def pompe_vide(self):
        return [self.pompe1.est_vide() , self.pompe2.est_vide() , self.pompe3.est_vide()]



d = Pompe()
d.remplir_pompe()
d.remplir_pompe()
print(d)
print(d.pompe_vide())



t = [1,2,3,4,5,6,7,8,9,10]
while True:

    for i in range(random.randint(9, len(t))):
        print(t[i])