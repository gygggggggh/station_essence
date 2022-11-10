# projet staion essance 

from csv import reader

with open("voitures.csv", "r") as file , open("clients.csv","r") as file2:
    v = reader(file)
    c = reader(file2)
    voitures = list(v)
    clients = list(c)

print(clients[0][2])
print(voitures[0][2])


k = [voitures[1],clients[1]]

print(k[0][2])