# projet staion essance 

from random import randint


class Voiture:
    def __init__(self):
        self._type = ""
        self._carburant = ""
        self._reservoir = 0
        self.voiture = [self._type, self._carburant, self._reservoir]

    def fiate_punto(self):
        self.voiture = ["Fiat Punto", "gasoil", 45]
    def renault_clio(self):
        self.voiture = ["Renault Clio", "sans plomb95", 65]
    def cybertruck(self):
        self.voiture = ["Cybertruck", "sans plomb98", 100]
    def SUV(self):
        self.voiture = ["SUV", "sans plomb95", 100]
    def camion(self):
        self.voiture = ["Camion", "gasoil", 200]
    def moto(self):
        self.voiture = ["Moto", "sans plomb95", 10]
    def scooter(self):
        self.voiture = ["Scooter", "gasoilsans plomb98", 7]
    def bus_a_essence(self):
        self.voiture = ["Bus a essence", "sans pomb95", 300]
    def tracteur(self):
        self.voiture = ["Tracteur", "gasoil", 150]
    def lambo(self):
        self.voiture = ["Lambo", "sans plomb98", 80]

    def random(self):
        voiture = [self.fiate_punto, self.renault_clio, self.cybertruck, self.SUV, self.camion, self.moto, self.scooter, self.bus_a_essence, self.tracteur, self.lambo]
        voiture[randint(0,9)]()
        return self.voiture

a = Voiture().random()
print(a)