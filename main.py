# projet staion essance 

from csv import reader

with open("voitures.csv", "r") as file , open("clients.csv","r") as file2:
    v = reader(file)
    c = reader(file2)
    voitures = list(v)
    clients = list(c)

print(clients[0][2])
print(voitures[0][2])
