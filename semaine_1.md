# projet station essence

## 1. les types de données

### 1.1 la gestion des type de clients

- le type de *clients* sont dans  un fichier csv qui contient les informations sur les types de clients leurs **temps** de **remplissage** et leur **particularité**

![voiture_csv](c_csv.png)

### 1.2 la gestion des voitures

- les *voiture* sont dans  un fichier csv qui contient les **informations** sur les voitures leurs **carburant** et leur **capacité** de remplissage

![voiture_csv](v_csv.png)

### 1.3 dans python

- nous convertissons les fichiers csv en liste avec la methode **Reader** de la librarie **CSV**

## 2. structure du code python

### 2.1 la station essence

- la station essence est une **class** qui utlisera la **class File** (vue predecament en cours ) pour combiner les informations des fichiers csv et efiler les informmations dans la  File d'attente de la station essence

- 