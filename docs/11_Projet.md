# Projet de fin d'atelier: comparateur de prix

Ce projet vise à créer un comparateur de prix entre les prix de deux compagnies. Les prix sont extraits des pages de recherche des sites en question puis formatés dans des structures de données de Python. 

Une fois les données récupérées, nous écrirons un algorithme permettant de combiner les listes de prix afin de refléter la différence entre les prix. Le résultat sera présenté sous forme d'un tableau. 

### Librairies nécessaires

Pour réaliser ce projet, nous aurons besoin de librairies dispobibles dans la bibliothèque PyPy de Python. Pour installer une librairie, nous utiliserons la commande `pip`. La liste des librairies dont nous aurons besoin est: 

* **request:** Afin de récupérer du contenu depui une page Web. Cette librairie fait partie de la librairie standard de Python (elle n'a pas à être installée)
* **BeautifulSoup:** qui nous permettra de parcourir le contenu structuré de la page Web à la recherche des informations qui nous intéressent. 
* **tabular**: Permet de formater des résultat à partir d'une structure itérable (ex.: liste) sous forme de tableau.

Avant de commencer, il donc exécuter les commandes suivantes dans la console pour que les librairie nécessaires soient téléchargées et ajoutées à votre installation de Python: 

```bash
pip3 install bs4
pip3 install tabular
```

