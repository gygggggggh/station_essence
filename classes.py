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
        
    def random(self) -> list:
        voitures_random = voitures[random.randint(1, len(voitures)-1)]
        clients_random = clients[random.randint(1, len(clients)-1)]
        return [voitures_random, clients_random]

    def remplir_pompe_debut(self) -> list:
        self.pompes[0].enfiler(self.random())
        self.pompes[1].enfiler(self.random())
        self.pompes[2].enfiler(self.random())
        return self.pompes

    def remplir_pompe(self) -> list:
        return self.pompes[random.randint(0, 2)].enfiler(self.random())

    def videz_pompe(self, pompe: int) -> list:
        if self.pompes[pompe-1].est_vide():
            return "la pompe est vide" 
        else:
            return self.pompes[pompe-1].defiler()

    def __str__(self) -> str:
        return f"pompe 1 : {self.pompe1} \npompe 2 : {self.pompe2} \npompe 3 : {self.pompe3}"

    def pompe_vide(self) -> list:
        return [self.pompe1.est_vide(), self.pompe2.est_vide(), self.pompe3.est_vide()]

    def covid(self, intensité: int):
        if intensité == 1:
            while not self.pompe1.est_vide():
                self.pompe1.defiler()
        elif intensité == 2:
            while not self.pompe2.est_vide() and not self.pompe1.est_vide():
                self.pompe2.defiler()
                self.pompe1.defiler()
        elif intensité == 3:
            while not self.pompe3.est_vide() and not self.pompe2.est_vide() and not self.pompe1.est_vide():
                self.pompe3.defiler()
                self.pompe2.defiler()
                self.pompe1.defiler()

    def mutinerie (self, intensité: int) -> list:
         return self.pompes[random.randint(0,2)].enfiler([["camion essence", "tout", 300*intensité], ["lamda", 200*intensité, 1]])



class Essence : # dylan
    def __init__(self,  prix_gasoile: float, quantite_gasoile: float, prix_sans_plomb95: float, quantite_sans_plomb95: float, prix_sans_plomb98: float, quantite_sans_plomb98: float , nbr_jour : int) -> None:
        self.prix_gasoile = prix_gasoile
        self.quantite_gasoile = quantite_gasoile
        self.prix_sans_plomb95 = prix_sans_plomb95
        self.quantite_sans_plomb95 = quantite_sans_plomb95
        self.prix_sans_plomb98 = prix_sans_plomb98
        self.quantite_sans_plomb98 = quantite_sans_plomb98

        self.prix = [self.prix_gasoile, self.prix_sans_plomb95, self.prix_sans_plomb98]
        self.quantite = [self.quantite_gasoile, self.quantite_sans_plomb95, self.quantite_sans_plomb98]



    def __str__(self) -> str:
        return f"prix du gasoile : {self.prix_gasoile} €\nquantite du gasoile : {self.quantite_gasoile} L\nprix du sans plomb 95 : {self.prix_sans_plomb95} €\nquantite du sans plomb 95 : {self.quantite_sans_plomb95} L\nprix du sans plomb 98 : {self.prix_sans_plomb98} €\nquantite du sans plomb 98 : {self.quantite_sans_plomb98} L"

    def prix_de_vente(self, type_carburant: int, coef_de_vente : int) -> float:
        if 0.5 < coef_de_vente < 2.5:
            return f'la loi vous interdit de vendre a ce prix'
        return self.prix[type_carburant-1] + coef_de_vente 



class Clients:
    def __init__(self) -> None:
        self.clients = Pompe().random()[1]

    def __str__(self) -> str:
        return f"clients : {self.clients}"

    def special(self, vigile: bool) -> int:
        specialite = self.clients[2]
        match specialite:
            case "normal":
                return [150,0]
            case "stupide":
                return [200,10]
            case "malin":
                return [50 if vigile else 200, 20]
            case "fou":
                return [400 if vigile else 50, 30]
            case "grilleur": 
                return [100 if vigile else 50, 40] 
            case "angry":
                return [175, 10]
            case "cops":
                return [151,random.randint(0, 100)]
            case _:
                 print("erreur")
                 exit(1)

                
                
printClients = Clients()
print(printClients)
print(printClients.special())



class Station : # dylan
    def __init__(self) -> None:
        self.pompes = Pompe()
        self.essence = Essence(1.5, 1000, 1.6, 1000, 1.7, 1000, 1)
        self.anger = 0
        self.temps = 2400
    def __str__(self) -> str:
        return f"{self.pompes} \n{self.essence}"







'''


if __name__ == "__main__":
    carb =  Essence(1.5, 1000, 1.6, 1000, 1.7, 1000, 1)
    pompe = Pompe()
    print(pompe)
    print(carb)
    print(pompe.pompe_vide())
    print(pompe.videz_pompe(1))
    print(pompe)









if "__main__" == __name__:
    pompe = Pompe()
    pompe.covid(1)
    print('2222222222222222222')
    print(pompe)
'''