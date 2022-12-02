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
        
    def random_pompe(self) -> list:
        voitures_random = voitures[random.randint(1, len(voitures)-1)]
        clients_random = clients[random.randint(1, len(clients)-1)]
        return [voitures_random, clients_random]

    def remplir_pompe_debut(self) -> list:
        self.pompes[0].enfiler(self.random_pompe())
        self.pompes[1].enfiler(self.random_pompe())
        self.pompes[2].enfiler(self.random_pompe())
        return self.pompes

    def remplir_pompe(self) -> list:
        return self.pompes[random.randint(0, 2)].enfiler(self.random_pompe())

    def videz_pompe(self, pompe: int) -> list:
        if self.pompes[pompe-1].est_vide():
            return "la pompe est vide" 
        else:
            return self.pompes[pompe-1].defiler()

    def __str__(self) -> str:
        return f"pompe 1 : {self.pompe1} \npompe 2 : {self.pompe2} \npompe 3 : {self.pompe3}"

    def pompe_vide(self) -> list:
        return [self.pompe1.est_vide(), self.pompe2.est_vide(), self.pompe3.est_vide()]






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
        self.prix_vente = [self.prix_gasoile + 0.25  , self.prix_sans_plomb95 + 0.25, self.prix_sans_plomb98 + 0.25]

        self.round()

    def __str__(self) -> str:
        return f"prix d'achat du gasoile : {self.prix_gasoile} \nprix du gasoil vendu : {self.prix_vente[0]} \nquantité de gasoil : {self.quantite_gasoile} \n\nprix d'achat du sans plomb 95 : {self.prix_sans_plomb95} \nprix du sans plomb 95 vendu : {self.prix_vente[1]} \nquantité de sans plomb 95 : {self.quantite_sans_plomb95} \n\nprix d'achat du sans plomb 98 : {self.prix_sans_plomb98} \nprix du sans plomb 98 vendu : {self.prix_vente[2]} \nquantité de sans plomb 98 : {self.quantite_sans_plomb98}"
    def augmenter_prix(self):
        self.prix_vente[random.randint(0,2)] += random.randint(5, 20) / 100
    def baisser_prix(self):
        self.prix_vente[random.randint(0,2)] -= random.randint(5, 20) / 100

    def round(self):
        for i in range(3):
            self.prix_vente[i] = round(self.prix_vente[i], 3)

   

class Clients: # dylan
    def __init__(self) -> None:
        self.clients = Pompe().random_pompe()[1]

    def __str__(self) -> str:
        return f"clients : {self.clients}"

    def special(self, vigile: bool) -> list:
        specialite = self.clients[2]
        match specialite:
            case "normal":
                return [int(self.clients[1]) ,0]
            case "lent":
                return [int(self.clients[1]) ,0]
            case "stupide":
                return [int(self.clients[1]) ,10]
            case "malin":
                return [int(self.clients[1]) / 2.5  if vigile else int(self.clients[1]) , 20 if vigile else 0,]
            case "fou":
                return [int(self.clients[1]) / 2.5  if vigile else int(self.clients[1]) , 30 if vigile else 0]
            case "grilleur": 
                return [int(self.clients[1]) /2.5  if vigile else int(self.clients[1]) , 40 if vigile else 0]
            case "angry":
                return [int(self.clients[1]), 10]
            case "cops":
                return [int(self.clients[1]),random.randint(0, 40)]
            case _:
                print("erreur")
                exit(1)
    def affichage_clients(self) -> str:
        return  f"{self.clients[0]} qui prend {self.clients[1]} temps"


# print(Clients().affichage_clients()) 


class Station : # dylan
    def __init__(self) -> None:
        self.pompes = Pompe()
        self.Clients = Clients()
        self.essence = Essence(1.2, 1000, 1.3, 1000, 1.45, 1000, 1)
        self.anger = 0
        self.temps = 2400 * 3 
        self.jour = 1
        self.vigiles =  True
        self.temps_a_retraiter = 0
        #self.pompes.remplir_pompe_debut() // debug 
    def __str__(self) -> str:
        return f"{self.pompes}\n \n{self.essence}"

    def augementation(self):
        print(f"jour {self.jour}")
        print(f"les gens sont ernervés de {self.anger/10} %")
        print(f"temps restant : {self.temps}")
        while True:
            rep = input(f"voulez-vous augmenter[1] ou baisser[2] le prix de l'essence ? \n ==> ")
            match rep:
                case "1":
                    print("augmentation du prix de l'essence")
                    print(f"prix avant augmentation : {self.essence.prix_vente}\n")
                    self.essence.augmenter_prix()
                    self.essence.round()
                    break
                case "2":
                    print("baisse du prix de l'essence")
                    print(f"prix avant baisse : {self.essence.prix_vente}\n")
                    self.essence.baisser_prix()
                    self.essence.round()
                    print
                    break
                case _:
                    print("attention, vous devez entrer 1 ou 2\n")
        print(f"prix après augmentation : {self.essence.prix_vente}\n")
        print(f"gasoil : {self.essence.prix_vente[0]} \nsans plomb 95 : {self.essence.prix_vente[1]} \nsans plomb 98 : {self.essence.prix_vente[2]}")
    def covid(self,intensite: int):
        if intensite == 1:
            while not self.pompes.pompe1.est_vide():
                self.pompes[0].defiler()
        elif intensite == 2:
            while not self.pompes.pompe2.est_vide() and not self.pompes.pompe1.est_vide():
                self.pompes.pompes[0].defiler()
                self.pompes.pompes[1].defiler()
        elif intensite == 3:
            while not self.pompes.pompe3.est_vide() and not self.pompes.pompe2.est_vide() and not self.pompes.pompe1.est_vide():
                self.pompes[0].defiler()
                self.pompes[2].defiler()
                self.pompes[1].defiler()
        else:
            print("erreur")
            exit(1)
    def mutinerie (self, intensité: int) -> list:
         return self.pompes[random.randint(0,2)].enfiler([["camion essence", "tout", 300*intensité], ["lamda", 200*intensité, 1]])


    def ristourne(self, intensité: int) -> list:
        self.essence.prix_vente[0] -= random.randint(5, 20) / 100
        self.essence.prix_vente[1] -= random.randint(5, 20) / 100
        self.essence.prix_vente[2] -= random.randint(5, 20) / 100
        self.essence.round()


a = Station()   

def main():