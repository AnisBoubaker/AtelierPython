# Les variables et les opérateurs

En python, il n'est pas nécessaire de déclarer des variables. Il suffit d'utiliser une nouvelle variable au besoin.

```python
ma_variable = 20

un_reel = 20.8

une_chaine = "Bonjour Python!"
```

Pour afficher le contenu d'une variable, il est possible d'utiliser la fonction `print` :

```python
a = 10
print(a)
>>> 10
```

Bien qu'il ne soit pas nécessaire de déclarer une variable avec un type, tel qu'on le ferait avec des langages "traditionnels" . Cependant, ceci ne veut pas dire que les variables n'ont pas de type, mais ceux-ci sont déterminés de façon dynamique à l'exécution. La commande `type` permet d'obtenir le type inféré par l'interpréteur.

```python
type(a)
>>> <class 'int'>
```

## Les types de base

Les types de base sont les types définis directement dans le langage (il est aussi possible de créer ses propres types/classe).  Les types de base sont : 

* Les entiers (int)
  `un_enter = 10`
* Les nombres à virgule flottante (float)
  `un_reel = 25.2`
* Les nombres complexes qui se définissent ainsi:  <partie réelle> + <partie imaginaire>j
  `un_complexe= 2+3j`
* Les booléens, des variables pouvant prendre une des valeurs suivantes: `True` ou `False`
* Les chaines de caractères. Contrairement au langage C, les chaines de caractères sont un type de base du langage et des fonctions rattachées permettent de les manipuler simplement. Nous consacrons un document aux chaines de caractères.

### Conversions de types

Il est possible de convertir un type en un autre type, simplement en récréant un objet du nouveau type. Par exemple, pour convertir un entier en réel à virgule flottante: 

```python
a = 10 
a = float(a)
print(a)
>>> 10.0
```

On utilise le même procédé pour convertir une chaine de caractères contenant une valeur numérique en un type numérique. Par exemple: 

```python
une_chaine = "40"
a = int(une_chaine)
print(a+10)
>>> 50
```

Ceci s'avère particulièrement utile si vous souhaitons interpréter la saisie d'un usager avec la fonction `input`. En effet, la fonction input renvoir toujours une chaine de caractères. Si la valeur attendue de l'utilisateur est un entier (par exemple), il faut convertir la chaine en un entier: 

```python
a = input("Veuillez saisir un entier: ")
a = int(a)
"""
Nous pouvons à présent manipuler `a` comme un entier et effectuer des
opérations arithmétiques.
"""

```

Notez cependant que, si l'usager n'a pas saisi un entier, une erreur de type `ValueError` se produira. Nous verrons comment nous pourrons gérer ces erreurs par la suite.

## Les opérateurs

Les opérateurs traditionnels (des autres langages) se retrouvent dans le langage Python. De plus, d'autres opérateurs ont été ajoutés pour simplifier des traitements qui devaient être calculés manuellement par le programmeur dans d'autres langages (ex.: les puissances).

### Les opérateurs arithmétiques

| Opérateur |             Description              |                         Exemple                         |
| :-------: | :----------------------------------: | :-----------------------------------------------------: |
|     +     |               Addition               |                       a + b = 30                        |
|     -     |             Soustraction             |                       a – b = -10                       |
|     *     |            Multiplication            |                       a * b = 200                       |
|     /     |               Division               |                        b / a = 2                        |
|     %     | Modulo: reste de la division entière |                        b % a = 0                        |
|    **     |              Puissance               |              10**20 =10 à la puissance 20               |
|    //     |           Division entière           | 9//2 = 4 , 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0 |

### Opérateurs d'assignation

Comme dans les autres langages, l'opérateur d'assignation est le `=` (à ne pas confondre avec l'opérateur de comparaison d'égalité `==` présenté à la section suivante).

De plus, il existe plusieurs opérateurs d'assignation combinés à un opérateur arithmétique. Par exemple l'opérateur +=, utilisé ainsi: 

```python
a = 10
a += 25
```

est équivalent à : 

```python
a = 10
a = a + 25
```

Ou encore, avec l'opérateur d'affectation avec puissance `**=`:

```python
c = 5
c **= 2 #Équivalent à c = c**2 
print(c)
>>> 25
```

Tous les opérateurs arithmétiques peuvent se combiner à l'opérateur d'affectation.

### Les opérateurs de comparaison

| Operator |              Description              |
| :------: | :-----------------------------------: |
|    ==    |   Vrai si deux valeurs sont égales    |
|    !=    | Vrai si deux valeurs sont différences |
|    <>    |            Identique à !=             |
|    >     |               Supérieur               |
|    <     |               Inférieur               |
|    >=    |           Supérieur ou égal           |
|    <=    |           Inférieur ou égal           |

### Les opérateurs logiques

On retrouve les 3 opérateurs logiques traditionnels: 

* `and`: le ET logique
* `or`: le OU logique
* `not`le NON logique

Notez que les opérateurs logiques traditionnels des autres langages (&&, || et ! ) ne fonctionnent pas. 

Les opérateurs logiques s'utilisent dans des expressions logiques contenant des opérandes booléennes (ayant pour valeurs `True` et  `False`) ainsi qu'avec des valeurs numériques. L'approche du C/C++ est alors utilisées: la valeur 0 est fausse, toute autre valeur est vraie.

### D'autres opérateurs

Le langage offre également d'autres opérateurs spécifiques que nous introduirons dans d'autres documents, notamment: 

* Les opérateurs d'appartenance à une liste/tuple/dictionnaire (`in` et `not in`)
* Les opérateurs d'identité (`is` et `is not`)

