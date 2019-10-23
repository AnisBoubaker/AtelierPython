# Les chaines de caractères

En python, les chaines de caractères sont une structure de données intégrée dans le langage. Leur utilisation est extrêment simple, comparativement à d'autres langages comme le C/C++ ou le Java. 

Une chaine de caractères doit être écrite entre des apostrophes `'...'` ou des guillemets `"..."`  si c'est une chaine de caractères en une seule ligne. Une chaine peut s'écrire sur plusieurs lignes, auquel cas elle doit être écrite entre des triple-guillemets `"""......."""`

Par exemple: 

```python
chaine1 = 'Allo!'
chaine2 = "Bonjour le monde!"
chaine3 = """Je suis très heureux-se de suivre cet atelier de Python. 
Bientôt je maitriserai le Python!"""

print(chaine2)
>>> Bonjour le monde!
print(chaine3)
>>> Je suis très heureux-se de suivre cet atelier de Python. 
Bientôt je maitriserai le Python!
```

Une chaine de caractères peut être indéxée comme une liste : on accède à un caractère donné de la chaine en faisant référence à son indice (les indice commence toujours à 0): 

```python
chaine = "Bonjour le monde!"
print( chaine[2] )
>>> n
```

Comme pour les structures de données, on peut obtenir la taille d'une chaine de caractères avec la fonction `len`:

```python
print(len(chaine))
>>> 17
```

De plus, une chaine de caractères peut-être découpée (*slicing*) comme une liste: 

```python
print( chaine[8:-7] )
>>> le
```

### Méthodes (fonctions) des chaines de caractères

Plusieurs fonctions utiles sont fournies et sont directement accessibles pour toute chaine de caractères. La liste exhaustive peut-être obtenue sur la documentation de python ([classe str](https://docs.python.org/3/library/string.html)) ou depuis l'interpréteur interactif avec `dir(str)`. En voici toutefois quelques unes choisies: 

* les méthodes `lower` et `upper` pour convertir une chaine de caractères en minuscules ou en majuscules (resp.).

  ```python
  chaine = "Bonjour le monde!"
  print( chaine.upper() )
  >>> BONJOUR LE MONDE!
  ```

* La méthode `strip` supprime les caractères d'espacement qui se trouvent au début et à la fin de la chaine

* Les méthodes `isalpha`, `isdigit` permettent de savoir si une chaine de caractères contient des caractères alphanumériques ou un nombre (respectivement)

* Les méthodes `startswith(une_chaine)` et `endswith(une_chaine)` permettent de vérifier si une chaine donnée commence (resp. se termine) par `une_chaine`

* La méthode `find(une_chaine)` détermine si la chaine de caractères contient une autre  chaine. Si c'est le cas, la position de sa première occurence est retournée. Sinon, la fonction retourne -1.

* La méthode `replace(ancien, nouveau)` remplace toutes les occurences de `ancien` dans la chaine par `nouveau`.

* La méthode `split(separateur)` permet de construire une liste de chaines de caractères, en découpant la chaine initiale selon le séparateur. 

* La méthode `join([...])` effectue l'opération inverse que `split`: elle combine les chaines se trouvant dans une liste, en les séparant par le contenu de la chaine initiale: 

  ```python
  s = ":"
  resultat = s.join(['Bonjour', 'le', 'monde'])
  print(resultat)
  >>> Bonjour:le:monde
  ```

### Concaténation de chaines de caractères

Pour concaténer (combiner) des chaines de caractères, nous utilisons l'opérateur +:

```python
c1 = "Bonjour "
c2 = "le monde"
resultat = c1+c2
print(resultat)
>>> Bonjour le monde
```



### Formatage de chaines de caractères

Commande dans les langages dérivés du C (C, C++, Java, Matlab, etc.), on peut construire une chaine de caractères on y injectant des valeurs provenant de variable ou expressions ( à la `printf`).

Cependant, compte tenu qu'en Python une chaine de caractères est un objet, nous utilisons une méthode pour le faire : la méthode `format`. Cette méthode s'applique sur une chaine de caractères contenant des indications d'emplacements pour effectuer l'injection. Ces emplacements sont indiqués par des `{ ... }`. Ainsi: 

```python
mois = 10
annee = 2019
str1 = "Nous sommes dans le {}ième mois de l'année {}".format(mois, annee)
print(str1)
>>> "Nous sommes dans le 10ième mois de l'année 2019"
```

Les emplacements `{...}` sans paramètres, sont traités par ordre positionnel: le premier `{}` sera remplacé par la valeur du premier paramètre de `format`, le deuxième `{}` sera remplacé par le deuxième paramètre de `format`, etc. 

Il est possible aussi de préciser quel paramètre de format nous souhaitons injecter à chaque emplacement, en utilisant l'ordre des paramètres de format entre les `{}`. Par exemple: 

```python
mois = 10
annee = 2019
str1 = "Nous sommes dans le {1}ième mois de l'année {0}".format(annee, mois)
print(str1)
>>> "Nous sommes dans le 10ième mois de l'année 2019"
```

