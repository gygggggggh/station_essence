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

    def get_pompes(self,n : int) -> list:
        return self.pompes[n-1]

    def get_clients(self,n : int) -> list:
        return self.pompes[n-1].file[0][1]

    def get_voitures(self,n : int) -> list:
        return self.pompes[n-1].file[0][0]

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
        self.prix_vente = [self.prix_gasoile + 0.5  , self.prix_sans_plomb95 + 0.5, self.prix_sans_plomb98 + 0.5]

        self.round()

    def __str__(self) -> str:
        return f"prix d'achat du gasoile : {self.prix_gasoile} \nprix du gasoil vendu : {self.prix_vente[0]} \nquantité de gasoil : {self.quantite_gasoile} \n\nprix d'achat du sans plomb 95 : {self.prix_sans_plomb95} \nprix du sans plomb 95 vendu : {self.prix_vente[1]} \nquantité de sans plomb 95 : {self.quantite_sans_plomb95} \n\nprix d'achat du sans plomb 98 : {self.prix_sans_plomb98} \nprix du sans plomb 98 vendu : {self.prix_vente[2]} \nquantité de sans plomb 98 : {self.quantite_sans_plomb98}"
    def augmenter_prix(self)-> None:
        self.prix_vente[random.randint(0,2)] += random.randint(5, 20) / 100
    def baisser_prix(self) -> None:
        self.prix_vente[random.randint(0,2)] -= random.randint(5, 20) / 100

    def round(self) -> None:
        for i in range(3):
            self.prix_vente[i] = round(self.prix_vente[i], 3)
    def reaprovisionnement(self) -> None:
        for i in range(3):
            self.quantite[i] += 1000
   

class Clients: # dylan
    def __init__(self,p1 : list, p2 : list, p3 : list) -> None:
        self.pompes = [p1, p2, p3]

    def special(self, vigile: bool,n : int) -> list:
        specialite = self.pompes[n].file[0][1][2]
        match specialite:
            case "normal":
                return [int(self.pompes[1].file[0][1][1]) ,0]
            case "lent":
                return [int(self.pompes[1].file[0][1][1]) ,0]
            case "stupide":
                return [int(self.pompes[1].file[0][1][1]) ,10]
            case "malin":
                return [int(self.pompes[1].file[0][1][1]) / 2.5  if vigile else int(self.pompes[1].file[0][1][1]) , 20 if vigile else 0,]
            case "fou":
                return [int(self.pompes[1].file[0][1][1]) / 2.5  if vigile else int(self.pompes[1].file[0][1][1]) , 30 if vigile else 0]
            case "grilleur": 
                return [int(self.pompes[1].file[0][1][1]) /2.5  if vigile else int(self.pompes[1].file[0][1][1]) , 40 if vigile else 0]
            case "angry":
                return [int(self.pompes[1].file[0][1][1]), 10]
            case "cops":
                return [int(self.pompes[1].file[0][1][1]),random.randint(0, 40)]
            case _:
                print("erreur")
                exit(1)
    def affichage_clients(self) -> str:
        return  self.pompes[0] 






        


class Voiture: # dylan
    def __init__(self,p1 : list,p2 : list, p3 : list ) -> None:
        self.voitures = [p1, p2, p3]
    def __str__(self) -> str:
        return f"voiture : {self.voitures[0]} \nvoiture : {self.voitures[1]} \nvoiture : {self.voitures[2]}"

    
    def prelevement(self,n : int) -> list:
        carbu = self.voitures[n].file[0][0][2]
        return int(carbu)
    
    def special(self, n : int) -> list:
        Essence = str(self.voitures[n].file[0][0][1])
        return str(Essence)

'''
p = Pompe()
v = Voiture(p.get_pompes(1), p.get_pompes(2), p.get_pompes(3))
n = 2
print(v.special(n))
print(v.prelevement(0))
'''


class Station : # dylan
    def __init__(self) -> None:
        self.argent = 50_000
        self.pompes = Pompe()
        self.Clients =  Clients(self.pompes.get_pompes(1), self.pompes.get_pompes(2), self.pompes.get_pompes(3))
        self.Voitures = Voiture(self.pompes.get_pompes(1), self.pompes.get_pompes(2), self.pompes.get_pompes(3))
        self.essence = Essence(1.2, 1000, 1.3, 1000, 1.45, 1000, 1)
        self.anger = 0
        self.temps = 2400 * 3 
        self.jour = 1
        self.vigiles =  True
        self.temps_a_retraiter = 0
    def __str__(self) -> str:
        return f"{self.pompes}\n \n{self.essence} \n \n{self.Clients}"

    def debut_jour(self):
        '''fonction qui permet de commencer un jour'''
        self.essence.reaprovisionnement()
        self.argent -= (self.essence.prix[0] * 1000 + self.essence.prix[1] * 1000 + self.essence.prix[2] * 1000)
        print(f"jour {self.jour}")
        print()
        print(f"vous avez {self.argent} euros")
        print(f"les gens sont ernervés de {self.anger/10} %")
        print(f"temps restant : {self.temps}")
        while True:
            rep = input(f"voulez-vous augmenter[1] ou baisser[2] le prix de l'essence ? \n ==> ")
            match rep:
                case "1":
                    print("augmentation du prix de l'essence")
                    print(f"prix avant augmentation : {self.essence.prix_vente}\n")
                    self.essence.augmenter_prix()
                    self.anger += 5
                    self.essence.round()
                    break
                case "2":
                    print("baisse du prix de l'essence")
                    print(f"prix avant baisse : {self.essence.prix_vente}\n")
                    self.essence.baisser_prix()
                    self.anger -= 5
                    self.essence.round()
                    print
                    break
                case _:
                    print("attention, vous devez entrer 1 ou 2\n")
        print(f"prix après augmentation : {self.essence.prix_vente}\n")
        print(f"gasoil : {self.essence.prix_vente[0]} \nsans plomb 95 : {self.essence.prix_vente[1]} \nsans plomb 98 : {self.essence.prix_vente[2]}")

    def n_clients(self, n: int) -> None:
        '''fonction qui permet de faire arriver des clients'''
        print(f"voici le client de la pompe {n}")
        print(f"il est de type'{self.pompes.get_clients(n)[0]}' et  il a pris {self.pompes.get_clients(n)[1]} temps \n")
        if self.pompes.get_clients(n)[3] == "True" :
            print("il va avoir besoins d'un vigile")
            if self.vigiles:
                while True:
                    print("vous avez un vigile")
                    rep = input("voulez-vous le l'utiliser ? [1] ou [2] non ? ==> ")
                    match rep:
                        case "1":
                            print("vous avez utilisé un vigile")
                            self.vigiles = False
                            clients = self.Clients.special(self.vigiles, n)
                            self.temps -= clients[0]
                            self.anger += clients[1]
                            self.vigiles = False
                            break
                        case "2":
                            print("vous n'avez pas utilisé de vigile")
                            clients = self.Clients.special(self.vigiles, n)
                            self.temps -= clients[0]
                            self.anger += clients[1]
                            break
                        
                        case _:
                            print("vous devez entrer 1 ou 2")
                            rep = input("vovoulez-vous le l'utiliser ? [1] ou [2] non ? ==> ")
            
            else:
                print("vous n'avez pas de vigile")
                clients = self.Clients.special(self.vigiles, n)
                self.temps -= clients[0]
                self.anger += clients[1]
        
        else:
            clients = self.Clients.special(self.vigiles,n)
            self.temps -= clients[0]
            self.anger += clients[1]
        print(f"temps restant : {self.temps}")
        print(f"les gens sont ernervés de {self.anger/10} %")


    def retrait(self, n: int) -> None:
        '''fonction qui permet de faire retraiter les voitures'''
        print(f"voici la voiture de la pompe {n}")  
        pompe = self.pompes.get_pompes(n)
        print(f"elle est de type'{self.pompes.get_voitures(n)[0]}' et va prendre du  {self.pompes.get_voitures(n)[1]} ")
        voiture_type = self.Voitures.special(n)
        match voiture_type:
            case "gasoil":
                if self.essence.quantite_gasoile <  int(self.Voitures.prelevement(n)):
                    print("vous n'avez pas assez de gasoil")
                    print("les clients sont enervés")
                    self.anger += 10
                    self.argent += (self.essence.prix_vente[0] * (int(self.Voitures.prelevement(n) - self.essence.quantite_gasoile)))
                    self.essence.quantite_gasoile = 0
                else:
                    self.essence.quantite_gasoile -=  int(self.Voitures.prelevement(n))
                pompe.defiler()
            case "sans_plomb95":
                if self.essence.quantite_sans_plomb95 <  int(self.Voitures.prelevement(n)):
                    print("vous n'avez pas assez de sans plomb 95")
                    print("les clients sont enervés")
                    self.anger += 10
                    self.argent += (self.essence.prix_vente[1] * (int(self.Voitures.prelevement(n) - self.essence.quantite_gasoile)))
                    self.essence.quantite_sans_plomb95 = 0
                else:
                    self.essence.quantite_sans_plomb95 -=  int(self.Voitures.prelevement(n))
                pompe.defiler()
            case "sans_plomb98":
                if self.essence.quantite_sans_plomb98 <  int(self.Voitures.prelevement(n)):
                    print("vous n'avez pas assez de sans plomb 98")
                    print("les clients sont enervés")
                    self.anger += 10
                    self.argent += (self.essence.prix_vente[2] * (int(self.Voitures.prelevement(n) - self.essence.quantite_gasoile)))
                    self.essence.quantite_sans_plomb98 = 0
                else:
                    self.essence.quantite_sans_plomb98 -=  int(self.Voitures.prelevement(n))
                    self.essence.round()
                    self.argent += self.essence.prix_vente[2] * self.Voitures.prelevement(n) 

            case "tout":
                if self.essence.quantite_gasoile <  int(self.Voitures.prelevement(n)) or  self.essence.quantite_sans_plomb95 <  int(self.Voitures.prelevement(n)) or self.essence.quantite_sans_plomb98 <  int(self.Voitures.prelevement(n)):
                    self.essence.quantite_gasoile =  self.essence.quantite_gasoile - int(self.Voitures.prelevement(n))
                    self.essence.quantite_sans_plomb95 =  self.essence.quantite_sans_plomb95 - int(self.Voitures.prelevement(n))
                    self.essence.quantite_sans_plomb98 =  self.essence.quantite_sans_plomb98 - int(self.Voitures.prelevement(n))
                    self.essence.round()
                else:
                    self.essence.quantite_gasoile -=  int(self.Voitures.prelevement(n))
                    self.essence.quantite_sans_plomb95 -=  int(self.Voitures.prelevement(n))
                    self.essence.quantite_sans_plomb98 -=  int(self.Voitures.prelevement(n))
                    self.essence.round()


                pompe.defiler()

            case _:
                print("erreur")
                print(f"erreur : {voiture_type}")
                print(pompe)
                print(voiture_type)


    def covid(self,intensite: int):
        '''fonction qui permet de faire la gestion du covid'''
        if intensite == 1:
            while not self.pompes.pompe1.est_vide():
                self.pompes.pompe1.defiler()
        elif intensite == 2:
            while not self.pompes.pompe2.est_vide() and not self.pompes.pompe1.est_vide():
                self.pompes.pompes[0].defiler()
                self.pompes.pompes[1].defiler()
        elif intensite == 3:
            while not self.pompes.pompe3.est_vide() and not self.pompes.pompe2.est_vide() and not self.pompes.pompe1.est_vide():
                self.pompes.pompes[0].defiler()
                self.pompes.pompes[1].defiler()
                self.pompes.pompes[2].defiler()
        else:
            print("erreur")
            exit(1)
    def mutinerie (self, intensité: int) -> list:
        '''fonction qui permet de faire la gestion de la mutinerie'''
        self.essence.quantite_gasoile -= random.randint(5, 20) * intensité
        self.essence.quantite_sans_plomb95 -= random.randint(5, 20) * intensité
        self.essence.quantite_sans_plomb98 -= random.randint(5, 20) * intensité


    def ristourne(self, intensité: int) -> list:
        '''fonction qui permet de faire la gestion de la ristourne'''
        self.essence.prix_vente[0] -= random.randint(5, 20) / 100
        self.essence.prix_vente[1] -= random.randint(5, 20) / 100
        self.essence.prix_vente[2] -= random.randint(5, 20) / 100
        self.anger -= random.randint(5, 20) * intensité
        self.essence.round()


    def affichage(self) -> str:
        '''fonction qui permet d'afficher les informations'''
        return f"jour : {self.jour} \n|\n{self.pompes} \n|\n{self.essence} \n"
