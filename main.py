# projet staion essance 
import random
from csv import reader

def ouvrir_csv(filename) -> list:
    """Ouvre le fichier CSV nommé nom_fichier et renvoie une liste de listes"""
    try:
        with open(filename, "r",encoding='utf-8') as file:
            data = reader(file)
            return list(data)
    except FileNotFoundError:
        print(f"Le fichier {filename} n'existe pas")
    except PermissionError:
        print(f"Le fichier {filename} ne peut pas être ouvert")
    except Exception as e:
        print(f"Une erreur inconnue est survenue: {e}")
    return []

voitures = ouvrir_csv("voitures.csv")
clients = ouvrir_csv("clients.csv")



class File:
    ''' creation de la fonction class vue en cours 
     pour la gestion de la classe Pompes ''' 

    def __init__(self) -> None: # Initialisation
        self.file = []  # Création d'une liste vide
        
    def __str__(self) -> str: # Affichage
        txt = ""
        for i in self.file:
            txt += str(i) + " <- "
        return txt
    
    def est_vide(self) -> bool: # Vérification de la liste
        return self.file == []
    
    def enfiler(self, x: int) -> None: # Ajout d'un élément à la liste
        self.file.append(x)

    def defiler(self) -> int: # Retrait d'un élément de la liste
        if not self.est_vide():
            self.file.pop(0)
        else:
            raise IndexError("La file est vide")


class Pompe:
    def __init__(self) -> None:
        self.pompe1 = File()
        self.pompe2 = File()
        self.pompe3 = File()
    def random(self) -> int:
        voitures_random = voitures[random.randint(1, len(voitures)-1)]
        clients_random = clients[random.randint(1, len(clients)-1)]
        return [voitures_random, clients_random]
    def remplir_pompe(self) -> None:
        self.pompe1.enfiler(self.random())
        self.pompe2.enfiler(self.random())
        self.pompe3.enfiler(self.random())
        

    def __str__(self) -> str:
        return f"pompe 1 : {self.pompe1} \npompe 2 : {self.pompe2} \npompe 3 : {self.pompe3}"

    def pompe_vide(self) -> list:
        return [self.pompe1.est_vide(), self.pompe2.est_vide(), self.pompe3.est_vide()]

    def covid(self, intensité: int):
        pass # a faire 

d = Pompe()
d.remplir_pompe()
d.remplir_pompe()
print(d)
print(d.pompe_vide())
