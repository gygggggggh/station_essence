# projet staion essance 

from csv import reader

with open("voitures.csv", "r") as file:
    reader = reader(file)
    voiture = list(reader)

with open("clients.csv", "r") as file:
    reader = reader(file)
    client = list(reader)


print(client[2][2])
print(voiture[2][2])
