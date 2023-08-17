# Beer Command Line Application

## Introduction

L'objectif de ce projet est de réaliser un service qui sera exécuté en CLI.
Le rôle de ce service sera d'importer des données, à savoir une liste de bières, puis d'effectuer des opérations de tri et de filtre avant de les afficher et dans certains cas, les exporter.
Il faudra mettre à disposition plusieurs commandes qui effectueront chacune un tri bien spécifique.

### Contraintes techniques
* Le projet doit être exécuté en CLI
* Il doit être développé en pure PHP (pas de framework)
* Il doit suivre les recommandation PSR12 pour le code style
* Il est tout à fait possible d'utiliser des dépendances tierces à l'aide de composer

### Prérequis

Avoir php et composer d'installé sur la machine. 


### Package de départ

*It’s dangerous to go alone! Take this.*

Pour le bon déroulement du dev, vous avez à votre disposition la structure de base du projet et les données à manipuler :
* Un fichier php à exécuter en CLI qui fera appelle au service à développer
* Un fichier CSV open-beer-database.csv qui contient les données à importer
* Le dossier src contient la class Cli qui est le point de départ du service à développer



## Spécifications

### Fonctionnement générale du service

Le service doit être exécuté en CLI et prend en paramètre obligatoire : 
* Le nom de la commande à exécuter
* Le chemin du fichier CSV à traiter

```
$> ./cli <nom_de_la_commande> <chemin_du_csv>
``` 

### Gestion des erreurs
Le service doit à minima gérer les erreurs concernant les paramètres obligatoires et le nom des commandes invalides (commands not found)


### Commandes beer:strongest
Afficher la/les  bière(s) la/les plus fortes.

Commande : 
```
$> ./cli beer:strongest /file/path/beer.csv
```

Output :
```
<beer name> - <brewery> - <country>
<beer name> - <brewery> - <country>
...
```

### Bitterest Beer
Afficher la/les bière(s) la/les plus amères (IBU)

Commande : 
```
$> ./cli beer:bitterest /file/path/beer.csv
```

Output :
```
<beer name> - <brewery> - <country>
<beer name> - <brewery> - <country>
...
```


### World Brewery ranking by country
Afficher les pays producteurs de bière classés par nombre de brasserie

Commande
```
$> ./cli beer:ranking:brewery /file/path/beer.csv
```

Output
```
<nb_brewery> - <country name>
<nb_brewery> - <country name>
<nb_brewery> - <country name>
<nb_brewery> - <country name>
...
```

## Style ranking by name
Afficher les styles de bières classés par nombre de références.

Commande
```
$> ./cli beer:ranking:style /file/path/beer.csv
```

Output
```
<nb_ref> - <style>
<nb_ref> - <style>
<nb_ref> - <style>
...
```

## Ranking by alcohol
Afficher les bières classées par taux d'alcool 

Commande
```
$> ./cli beer:ranking:alcohol /file/path/beer.csv
```

Output
```
<beer name> - <brewery> - <alcohol>
<beer name> - <brewery> - <alcohol>
<beer name> - <brewery> - <alcohol>
<beer name> - <brewery> - <alcohol>
...
```

## Display

Ecrire une commande qui générera un nouveau fichier csv, les colonnes qui doivent figurer dans ce fichier sont :
* Name
* Style
* Brewery
* Alcohol
* IBU
* Description
* Country
* Website
 
