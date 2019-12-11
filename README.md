# Beer Commande Line Application

Cette CLI prend en parametre obligatoire un fichier utiliser celui fournit(open-beer-database.csv).

Cette cli possede plusieurs commande possible.

Cette cli sera faite en pure PHP, sans framework, suivre les recommandations PSR12 pour le code style. Il est tout a fait possible d'utiliser des dependances tierces a l'aide de composer. 

**Prerequis**
> Avoir php et composer d'installer sur la machine. 

## Strongest Beer
Remonter la/les  biere(s) la plus forte.

```
$> ./cli beer:strongest /file/path/beer.csv
beer name - brewery - country
```

## Bitterest Beer
Trouver la/les biere(s) la/les plus amere (IBU)

```
$> ./cli beer:bitterest /file/path/beer.csv
beer name - brewery - country
```

## World Brewery ranking by country
Classement des pays, par nombre de brasserie

```
$> ./cli beer:ranking:brewery /file/path/beer.csv
nb_brewery - country
nb_brewery - country
nb_brewery - country
nb_brewery - country
```
## Style ranking by name
Classement des style de bieres par nombre de reference.

```
$> ./cli beer:ranking:style /file/path/beer.csv
nb_ref - style
nb_ref - style
nb_ref - style
nb_ref - style
```

## Ranking by alcohol
Classement des bieres par taux d'alcool 

```
$> ./cli beer:ranking:alcohol /file/path/beer.csv
beer name - brewery - alcohol
beer name - brewery - alcohol
beer name - brewery - alcohol
beer name - brewery - alcohol
beer name - brewery - alcohol
```

## Display

Ecrire une commande qui generera un nouveau fichiers csv, les colonnes qui doivent figurer dans ce fichiers sont:
* Name
* Style
* Brewery
* Alcohol
* IBU
* Description
* Country
* Website
 