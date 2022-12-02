# projet station essence

## 1. les types de données

### 1.1 la gestion des type de clients

- le type de *clients* sont dans  un fichier csv qui contient les informations sur les types de clients leurs **temps** de **remplissage** et leur **particularité**

![clients_csv](c_csv.png)

#### 1.1.1 retour sur le csv clients

- nous avons preferer utiliser les "case" pour une meilleur lisibilité du code et pour simplifier le fichier csv donc la derniere colonne est inutile avec les "case"

### 1.2 la gestion des voitures

- les *voiture* sont dans  un fichier csv qui contient les **informations** sur les voitures leurs **carburant** et leur **capacité** de remplissage

![voiture_csv](v_csv.png)

### 1.3 dans python

- nous convertissons les fichiers csv en liste avec la methode **Reader** de la librarie **CSV**

## 2. structure du code python

### 2.1 la class pompe yanis

- la pompe est une **class** qui utlisera la **class File** (vue predecament en cours ) pour combiner les informations des fichiers csv et efiler les informmations dans la  File d'attente de la station essence
  
#### 2.1.1 l'atribut random_pompe

- cette atribut permet de crée une combinaison aléatoire d'un type de **client** et d'une **voiture**

#### 2.1.2 l'atribut remplir_pompe_debut

- cette atribut permet de remplir chaque pompe avec un **client** et une **voiture** de plus cette atribut est utliser dans le init de la class pompe

#### 2.1.3 l'atribut remplir_pompe

- cette atribut utlise l'atribut random_pompe pour remplir une pompe aleatoire avec un **client** et une **voiture** de plus cette atribut est utliser dans le init de la class pompe

#### 2.1.4 l'atribut  vide_pompe

- cette atribut permet de vider la pompe indique en parametre d'un cran et verifie si la pompe est vide ou non avant de la vider pour eviter les erreurs

#### 2.1.5 l'atribut  pompe_vide

- cette atribut permet de verifier si les pompe sont vide ou non

### 2.2 la class essence dylan

- la class essence est une **class** qui permet de gerer les **prix** des **carburants**  et elle initialiser les **type de carburent** et les **prix** des **carburants**

#### 2.2.1 l'atribut  augmenter_prix

- cette atribut permet d'augmenter le prix du carburant de maniere aleatoire

#### 2.2.2 l'atribut  diminuer_prix

- cette atribut permet de diminuer le prix du carburant de maniere aleatoire

#### 2.2.3 l'atribut  round

- cette atribut permet d'arrondir le prix du carburant a 2 chiffres apres la virgule

### 2.3 la class client dylan

- la class Client est une **class** qui permet de gerer les **clients** et leurs **particularités** et leurs **temps** de **remplissage**

#### 2.3.1 l'atribut  special

- cette atribut va renvoyé un entier qui correspond a la  vitesse et la particularité du client et la presence ou non d'un vigile

#### 2.3.2 l'atribut  affichage_client

- cette atribut va renvoyé un string qui correspond au type de client et a la vitessse du client
  
### 2.4 la class voiture yanis

- WIP(Work In Progress), la class voiture sera une **class** qui permetera de gerer les **voitures** , leurs **carburant** et leurs **capacité** de remplissage

### 2.5 la class station dylan

- la class Station est une class qui regroupe toutes les autres class et permet de gerer la station essence et ses **Clients** , **Voitures** , **Pompe** , **essence**  , elle gere aussi les evenements de la station essence

## 3 Structure du code

### 3.1 le fichier class.py

- il contient les class

### 3.2  le fichier main.py

- il contient la boucle principale du code
[![wakatime](https://wakatime.com/badge/user/1dff2156-409d-4a9c-83e3-80e9582fd198/project/b51493e9-3bee-43bd-aea6-798a15f0a435.svg)](https://wakatime.com/badge/user/1dff2156-409d-4a9c-83e3-80e9582fd198/project/b51493e9-3bee-43bd-aea6-798a15f0a435)
