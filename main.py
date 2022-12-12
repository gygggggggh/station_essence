from classes import *
from time import sleep
from random import randint

Station = Station()


def main(station):
    print(f"bienvenue dans le jeu")
    print(Station.affichage())
    event = 0
    while True:
        event += 1
        for n in range(1, 3):
            if station.temps > 0:
                print("\n")
                print("\n")
                station.n_clients(n)
                station.retrait(n)
                print("\n")
                print("\n")
                if event == 3:
                    station.mutinerie(randint(1, 3))
                    station.n_clients(1)
                    station.retrait(1)
                sleep(3)
        station.pompes.remplir_pompe_debut()   
        station.affichage()
        station.jour += 1
        station.debut_jour()
        print("\n")
        sleep(1)
        if station.anger >= 100 * 10 :
            print("vous avez perdu")
            break
        elif station.argent < 0:
            print("vous avez perdu")
            break
    print(station.anger)
main(Station)

