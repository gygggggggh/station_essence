from classes import *


Station = Station()


def main(station):
    print(f"bienvenue dans le jeu")
    print(Station.affichage())
    while True:
        while station.temps > 0:
            for n in range(1, 3):
                station.pompes.remplir_pompe_debut()
                station.n_clients(n)
                station.retrait(n)
                print("\n")
                print("\n")
                station.pompes.remplir_pompe_debut()
        station.affichage()
        station.pompes.remplir_pompe_debut()
        station.pompes.remplir_pompe
        print(Station.augementation())
    
main(Station)