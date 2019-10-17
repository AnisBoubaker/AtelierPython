# Les fonctions

Comme tout langage de programmation, Python offres comme premier niveau de factorisation du code la possibilité de créer des fonctions. 

La syntaxe générale pour définir une fonction en Python est la suivante: 

```python
def identifiant_fonction( liste_parametres ):
	""" Commentaires de la fonction """
	<intructions>
  return <une_expression>
```

Par exemple, une fonction qui détermine si un entier est pair: 

```python
def est_pair(un_entier):
  """Renvoie True si un_entier est pair"""
  if un_entier%2==0:
    return True
  return False
```

Pour appeler une fonction, il suffit de faire référence à son identifiant et de transmettre ses paramètres:

```python
est_pair(5)
>>> False
est_pair(6)
>>> True
```

Les objets passés à une fonction sont toujours passés par référence (ex.: une liste, un tuple, etc.) mais ceci ne s'applique pas pour les types simples (int et float). Ainsi: 

```python
def ajouter_1(une_liste):
	une_liste.append(1)

  
ma_liste = [1, 4, 5, 10]
ajouter_1(ma_liste)
print(ma_liste)
>>> [1, 4, 5, 10, 1]
```

### Les paramètres nommés

Dans les exemples précédents, lors de l'appel de fonction,  nous avons spécifié les paramètres de façon positionnelle : c'est la position du paramètre lors de l'appel qui définit à quel paramètre de la fonctions il va donner sa valeur. 

Il est aussi possible de définir les paramètres de façon nommée. Prenons par exemple cette fonction: 

```python
def afficher_personne(nom, age):
	"""Affiche le nom de la personne et son age"""
  print("{} qui a {} ans".format(nom, age))
```

Nous pouvons appeler cette fonction ainsi: 

```python
afficher_personne(age=35, nom="Marie")
>>> Marie a 35 ans
```

Notez qu'en utilisant les noms des arguments, il n'est pas nécessaire de respecter l'ordre défini dans la fonction. Ceci a l'avantage de clarifier l'appel des fonctions, au prix d'avoir des appels de fonctions plus longs. 

### Les paramètres optionnels

Certains paramètres d'une fonction peuvent être optionnel, auquel cas, nous devons spécifier des valeurs par défaut, La valeur par défaut sera utilisée si l'appelant de la fonction n'a pas précisé de valeur. 

```python
def est_majeur(nom, age, age_majortie=18):
  if age >= age_majorite:
    return True
  return False
```

Nous pouvons appeler cette fonction ainsi: 

```python
est_majeur("Jean-Jacques", 18)
>>> True
est_majeur("Marshal", 18, 21)
>>> False
est_majeur(age=18, nom="Marshal", age_majorite=21)
>>> False
```

### Les fonctions anonymes

Une fonction anonyme (ou fonction *lambda* ) est une fonction simple (ne comporte qu'une seule instruction). Elles sont utiles pour faire des traitements simple et localisés ou en combinaison avec une structure de traitement avancée (chainage). 

Une fonction lambda se définit à l'aide du mot clé `lambda`: 

```python
operation = lambda x, y: x*2-y
val = operation(10, 15)
print(val)
>>> 5
```

Pas si anonyme diriez-vous. Dans cet exemple, nous avons créé une fonction anonyme, PUIS associé la fonction à un nom. L'intérêt des fonctions *lambda* est lorsqu'on l'associe à d'autre fonctions qui s'attendent à recevoir une fonction. 

Par exemple, la fonction `map` permet d'obtenir un objet itérable (ex.: une liste) à partir d'un autre objet itérable auquel on a appliqué une fonction à chacun des ses éléments. Par exemple: 

```python
l1 = [(10, 2), (11, 5), (14, 7)]
l2 = list( map(sum, l1) )
print(l2)
>>> [12, 16, 21]
```

Ici nous avons utilisé la fonction `map` avec la fonction `sum`: on a effectué la somme de chaque élément de l1 (des tuples) et stocké le résultat dans la liste l2. Supposons que l'on veuille faire la même chose avec une liste dont on souhaite élever au carré tous ses éléments. Nous utiliserons une fonction `carre` si elle existait mais on n'en a pas défini et nous ne souhaitons pas définir de nouvelle fonction. C'est là que les fonctions lambda sont utiles: 

```python
l3 = [3, 5, 6, 10]
l4 = list( map( lambda x: x**2 , l3) )
print(l4)
>>> [9, 25, 36, 100]
```



