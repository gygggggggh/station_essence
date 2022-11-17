# projet staion essance 
import random
from csv import reader

def ouvrir_csv(filename) -> list: # dylan
    """Ouvre le fichier CSV nommé nom_fichier et renvoie une liste de listes"""
    try:
        with open(filename, "r",encoding='utf-8') as file:
            data = reader(file)
            return list(data)
    except FileNotFoundError:
        print(f"Le fichier {filename} n'existe pas")
        exit(1)
    except PermissionError:
        print(f"Le fichier {filename} ne peut pas être ouvert")
        exit(1)
    except Exception as e:
        print(f"Une erreur inconnue est survenue: {e}")
        exit(1)
    
voitures = ouvrir_csv("voitures.csv")
clients = ouvrir_csv("clients.csv")



class File: # yanis
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


class Pompe: # yanis 
    def __init__(self) -> None:
        self.pompe1 = File()
        self.pompe2 = File()
        self.pompe3 = File()
        self.pompes = [self.pompe1, self.pompe2, self.pompe3]
        self.remplir_pompe_debut()
        
    def random(self) -> int:
        voitures_random = voitures[random.randint(1, len(voitures)-1)]
        clients_random = clients[random.randint(1, len(clients)-1)]
        return [voitures_random, clients_random]

    def remplir_pompe_debut(self) -> None:
        self.pompes[0].enfiler(self.random())
        self.pompes[1].enfiler(self.random())
        self.pompes[2].enfiler(self.random())
        return self.pompes

    def remplir_pompe(self) -> None:
        return self.pompes[random.randint(0, 2)].enfiler(self.random())

    def videz_pompe(self, pompe: int):
        if self.pompes[pompe-1].est_vide():
            return "la pompe est vide" 
        else:
            return self.pompes[pompe-1].defiler()

    def __str__(self) -> str:
        return f"pompe 1 : {self.pompe1} \npompe 2 : {self.pompe2} \npompe 3 : {self.pompe3}"

    def pompe_vide(self) -> list:
        return [self.pompe1.est_vide(), self.pompe2.est_vide(), self.pompe3.est_vide()]

    def covid(self, intensité: int):
        pass # a faire 

if "__main__" == __name__:
    pompe = Pompe()
    pompe.videz_pompe(1)
    print(pompe)
    print(pompe.pompe_vide())