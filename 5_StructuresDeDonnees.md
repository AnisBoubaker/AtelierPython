# Les structures de données de base

Python offre un ensemble de structures de données de base qui sont fortement intégrées dans le langage. D'autre langages font de même (ex.: Java) mais les structures de données sont des types définis et l'intégration au sein du langage est très limitées. D'autres langages (ex.: C) n'offrent aucune structure de données autre que les tableaux statiques (qui sont des pointeurs). 

Ainsi, apprendre le Python nécessite de bien assimiler ces structures de données : les listes, les tuples, les dictionnaires. Nous retrouvons également les ensembles (`set`) et les ensembles figés  (`frozenset`) que nous n'aborderons pas mais qui sont facilement accessible à travers une recherche sur Internet. 

## Les listes

Une liste se définit à l'aide des crochets `[ ...]`. Une liste contient un ensemble d'éléments hétérogènes. Par exemple: 

```python
ma_premiere_liste = [10, 23, 67, 'Et du texte']
```

Nous accédons aux éléments d'une liste en faisant référence à son indice. Comme dans les autres langages, les indices commencent à 0 : 

```python
print(ma_premiere_liste[2])
>>> 67
```

### Fonctions des listes

Nous ne donnerons pas toutes les fonctions des listes ici mais citerons les plus utilisées.

La fonction (méthode) `append` permet d'ajouter des éléments à la fin d'une liste:

```python
l = [1, 45, 23, 10]
l.append(55)
print(l)
>>> [1, 45, 23, 10, 55]
```

La fonction `extend` permet d'ajouter tous les éléments d'une autre liste à la fin d'une liste: 

```
l.extend(['a', b', 'c'])
print(l)
>>> [1, 45, 23, 10, 55, 'a', 'b', 'c']
```

La fonction `insert` ajoute un élément à la position spécifiée, en décalant les éléments au besoin: 

```python
l.insert(2, 'x')
print(l)
>>> [1, 45, 'x', 23, 10, 55, 'a', 'b', 'c']
```

La fonction `index` permet d'obtenir la position d'un élément dans la liste. Si l'élément est introuvable une exception ValueError est déclenchée: 

```python
l.index('x')
>>> 2
```

