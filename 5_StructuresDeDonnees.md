# Les structures de données de base

Python offre un ensemble de structures de données de base qui sont fortement intégrées dans le langage. D'autre langages font de même (ex.: Java) mais les structures de données sont des types définis et l'intégration au sein du langage est très limitées. D'autres langages (ex.: C) n'offrent aucune structure de données autre que les tableaux statiques (qui sont des pointeurs). 

Ainsi, apprendre le Python nécessite de bien assimiler ces structures de données : les listes, les tuples, les dictionnaires. Nous retrouvons également les ensembles (`set`) et les ensembles figés  (`frozenset`) que nous n'aborderons pas mais qui sont facilement accessible à travers une recherche sur Internet. 

## 1. Les listes

Une liste se définit à l'aide des crochets `[ ...]`. Une liste contient un ensemble d'éléments hétérogènes. Par exemple: 

```python
ma_premiere_liste = [10, 23, 67, 'Et du texte']
```

Nous accédons aux éléments d'une liste en faisant référence à son indice. Comme dans les autres langages, les indices commencent à 0 : 

```python
print(ma_premiere_liste[2])
>>> 67
```

### 1.1. Fonctions des listes

Nous ne donnerons pas toutes les fonctions des listes ici mais citerons les plus utilisées.

La fonction (méthode) `append` permet d'ajouter des éléments à la fin d'une liste:

```python
l = [1, 45, 23, 10]
l.append(55)
print(l)
>>> [1, 45, 23, 10, 55]
```

La fonction `extend` permet d'ajouter tous les éléments d'une autre liste à la fin d'une liste. L'opérateur `+`  et  `+=` peut être utilisé pour obtenir le même résultat.

```python
l.extend(['a', b', 'c'])
print(l)
>>> [1, 45, 23, 10, 55, 'a', 'b', 'c']

l += ['d', 'e', 'f']
print(l)
>>> [1, 45, 23, 10, 55, 'a', 'b', 'c', 'd', 'e', 'f']
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

La fonction `count` compte le nombre d’occurrences d'un élément dans une liste: 

```python
l.count('a')
>>> 1
```

La fonction `sort` permet de trier une liste. Celle-ci la trie en ordre croissant par ordre croissant (numérique ou lexicographique). Les éléments doivent être du même type, autrement nous obtenons l'exception TypeError.

Il est possible d'effectuer le tri en ordre inverse en donnant la valeur True au paramètre nommé `reverse`.

```python
l2 = [23, 2, 18, 67, 23, 34]
l2.sort()
print(l2)
>>> [2, 18, 23, 23, 34, 67]

l3 = [23, 2, 18, 67, 23, 34]
l3.sort(reverse=True)
print(l3)
>>> [67, 34, 23, 23, 18, 2]
```

La fonction `reverse` permet d'inverser les éléments d'une liste.  

```python
l3.reverse()
print(l3)
>>> [2, 18, 23, 23, 34, 67]
```

Finalement, l'opérateur `*` permet de répéter une liste plusieurs fois et stocker le résultat dans une autre liste. Par exemple: 

```python
liste1 = [1, 2, 3]
liste2 = liste1 * 3
print(liste2)
>>> [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### 1.2. Le découpage des listes (*slicing*)

Nous pouvons obtenir une sous-liste depuis une liste originale en spécifiant les positions de début et de fin. La syntaxe générale est la suivante: 

```python
une_liste[pos_debut:pos_fin:pas]
```

Ceci sélectionne la sous-liste depuis `une_liste` en partant de l'élément à la position `pos_debut` jusqu'à l'élément à la position `pos_fin` (l'élément à `pos_fin` est exclu), en avançant par `pas` éléments. Tous les paramètres sont facultatifs.

Par exemple: 

```python
liste3 = [1,2,3,4,5,6,7,8,9,10]
print(liste3[2:8:1])
>>> [3, 4, 5, 6, 7, 8]
print(liste3[:5])
>>> [1, 2, 3, 4, 5]
print(liste3[::2])
>>> [1, 3, 5, 7, 9]
print(liste3[:])
[1,2,3,4,5,6,7,8,9,10]
```

Les positions peuvent être négatives, auquel cas, la position -1 réfère au dernier élément de la liste: 

```python
print(liste3[2:-2])
>>> [3, 4, 5, 6, 7, 8]
```

### 1.3. Composition de listes (*list comprehension*)

Une fonctionnalité puissante du python est la composition de listes depuis d'autres listes grâce à l'opérateur `for...in...if`

Supposons que l'on dispose d'une liste `liste1` contenant des entiers. Nous souhaitons extraire, dans une autre liste, les entiers de `liste1` qui sont supérieurs à 25:

```python
liste1 = [10, 34, 56, 18, 5, 118, 25, 10]
sup25 = [v for v in liste1 if v > 25]
print(sup25)
>>> [34, 56, 118]
```

Ceci permet de générer une liste facilement depuis une autre ou de filtrer une liste. Les éléments sélectionnés peuvent être manipulés. Par exemple, si nous souhaitons que les éléments supérieurs à 25 retenus soient divisés par 2: 

```python
liste1 = [10, 34, 56, 18, 5, 118, 25, 10]
sup25 = [v/2 for v in liste1 if v > 25]
print(sup25)
>>> [17.0, 28.0, 59.0]
```

## 2. Les tuples

Un tuple est un ensemble de valeurs immuable (les valeurs ne peuvent pas changer). Un tuple se déclare en utilisant des `(...)`. Ils peuvent être indexés et découpés comme une liste. On peut leur ajouter des éléments à l'aide de l'opérateur `+` ou `+=` et les construire depuis un autre tuple avec l'opérateur `*`.

```python
tuple1 = ('jean', 'valjean', 1782)
print(tuple1[0])
>>> jean
print(tuple1[:2])
>>> ('jean', 'valjean')
tuple1 += ('15 rue du cirque', )
print(tuple1)
('jean', 'valjean', 1782, '15 rue du cirque')
```

Les fonctions associées aux tuples sont plus limitées que celles des listes, compte tenu de l'immutabilité des tuples. Seules les fonctions `count` et `index` sont disponibles.

## 3. Les dictionnaires

Un dictionnaire est un ensemble d'éléments de type `clé:valeur`.  Comparativement aux listes, un dictionnaire est une liste dont les index ne sont pas des entier (0, 1....) mais des valeurs arbitraires. On déclare un dictionnaire à l'aide des accolades `{....}`

```python
personnage = {'nom': 'Valjean', 'prenom':'Jean', 'age':57}
```

Pour accéder à un élément, on y fait référence par son index: 

```python
print(personnage['prenom'])
>>> Jean
```

Il est possible de récupérer toutes les clés d'un dictionnaire avec la fonction `keys`:

```python
print( personnage.keys() )
>>> dict_keys(['nom', 'prenom', 'age'])
```

De même, nous pouvons récupérer la liste des valeurs d'un dictionnaire avec la méthode `values`: 

```python
print( personnage.values() )
>>> dict_values(['Valjean', 'Jean', 57])
```

Finalement, nous pouvons transformer un dictionnaire en une liste de tuples (couples), chaque couple ayant deux élélement: la clé et la valeur. Pour ce faire, nous utilisons la méthode `items`:

```python
print( personnage.items() )
>>> dict_items([('nom', 'Valjean'), ('prenom', 'Jean'), ('age', 57)])
```

Ces fonctions s'avèrent très utiles lors de la composition de dictionnaires (*dictionary compréhension*), comme on l'a vu pour les listes. par exemple: 

```python
dict1 = {'a':25, 'b': 10, 'c': 32, 'd':15}
dict2 = {k:v*2 for (k,v) in dict1.items() }
print(dict2)
>>> {'a': 50, 'b': 20, 'c': 64, 'd': 30}
```



### 4. Copie des structures

Nous pouvons affecter une structure de données dans une autre. Par exemple: 

```python
liste1 = [1, 2, 3, 4]
liste2 = liste1
```

Cependant, aucune copie n'est réellement créée ici (on dit qu'on copie la référence). En effet, suite à cette instruction, les deux variables `liste1` et `liste2` font référence au même objet qui contient `[1, 2, 3, 4]`. Ainsi, en modifiant `liste2`, **on modifie aussi `liste1`!** 

```python
liste1 = [1, 2, 3, 4]
liste2 = liste1
liste2[0] = 55
print(liste1)
>>> [55, 2, 3, 4]
```

Ce comportement s'observera avec toutes les structures mutables (notamment les listes et les dictionnaires). Les structures de données immutables (tuples et chaines de caractères) n'ont pas ce problème.

De ce fait, il faut être prudent lorsqu'on utilise l'opérateur d'affectation avec des structures de données mutables. Si nous souhaitons réellement créer une copie *indépendante* d'une structure de données, nous utiliserons la fonction `copy`: 

```python
liste1 = [1, 2, 3, 4]
liste2 = liste1.copy()
liste2[0] = 55
print(liste1)
>>> [1, 2, 3, 4]
print(liste2)
>>> [55, 2, 3, 4]
```

