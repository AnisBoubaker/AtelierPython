# Les modules et les paquetages

Nous avons vu qu'un premier niveau de factorisation de code en Python était les fonctions. Il est possible de factoriser d'avantages en regroupant des fonctions au sein de modules. À un niveau supérieur, nous pouvons même regrouper des modules au sein de paquetages. Bien que nous n'aborderons pas ceci dans le cadre de cet atelier, il est possible en Python d'organiser le code en classe et programmer selon le paradigme orienté-objet. 

## Les modules

Un module est un regroupement de fonctions dans un fichier `.py`. Plusieurs modules (et paquetages) sont disponibles avec la librairie standard de Python. D'autres peuvent être ajoutés en les plaçant dans le même dossier que notre programme ou en les ajoutant dans le dossier par défaut de votre installation Python. Nous allons d'abord apprendre à créer nos propres modules. 

Pour créer un module, il suffit de créer un fichier `.py` et d'y placer des fonctions. Par exemple, supposons que les fonctions suivantes se trouvent dans le fichier `mod_math.py`: 

```python
def pgcd(a, b):
	while b:
		if a>b:
			a-=b
		else:
			b-=a
	return a

def modulo(a, b):
	div = a // b
	return a-div*b

def puissance(base, puiss):
	resultat = 1
	while puiss:
		resultat*=base
		puiss-=1
	return resultat
```

Nous aimerions, d'abord, tester nos fonctions. Nous allons alors compléter ce script en ajouttant du code de test. voici le nouveau contenu de notre module: 

```python
def pgcd(a, b):
	while b:
		if a>b:
			a-=b
		else:
			b-=a
	return a

def modulo(a, b):
	div = a // b
	return a-div*b

def puissance(base, puiss):
	resultat = 1
	while puiss:
		resultat*=base
		puiss-=1
	return resultat

print(modulo(34,8))
print(pgcd(16,3))
print(puissance(5,3))
```

Cependant, notre objectif est que ce module puisse être *importé* pour être utilisé dans un programme ou d'autres modules. Si nous le laissons dans l'état dans lequel il est, à chaque fois que nous l'importerons, le code de test que nous avons mis sera exécuté aussi! 

Fort heureusement, Python nous offre une technique nous permettant de spécifier le code à exécuter si le module est exécuté comme un programme. Par contre, si celui-ci est plutôt *importé*, le code en question ne devrait pas s'exécuter. Pour ce faire, nous utiliserons la variable `__name__` qui vaut la chaine de caractères `"__main__"`  si c'est exécuté comme un progamme. Ainsi: 

```python
# -*- coding: utf-8 -*-

def pgcd(a, b):
	while b:
		if a>b:
			a-=b
		else:
			b-=a
	return a

def modulo(a, b):
	div = a // b
	return a-div*b

def puissance(base, puiss):
	resultat = 1
	while puiss:
		resultat*=base
		puiss-=1
	return resultat

def __main():
	print(modulo(34,8))
	print(pgcd(16,3))
	print(puissance(5,3))

if(__name__ == "__main__"):
	__main()
```

Si le module est exécuté directement (comme un programme), la fonction `main()` s'exécutera. Par contre, si le module est importé, la fonction `main()` ne s'exécutera pas. 

Voyons maintenant comment importer notre module. Nous allons créer un autre fichier qu'on appellera `mon_programme.py`.  Pour importer le module, nous utiliserons l'instruction `import`, en mettant le nom de fichier **sans l'extension `.py`**:

```python
import mod_math

val = mod_math.pgcd(24,4)
print(val)
```

Ainsi, en important le module, nous avons accès à toutes les fonctions qu'il offre. Cependant, nous sommes obligés de mettre le nom du module à chaque fois que nous tentons d'accéder aux fonctions du module. Pour comprendre pourquoi, nous devons comprendre la notion d'**espace de noms**.

Un espace de nom est une table qui associe chaque identifiant (identifiant de variable, de fonction, etc.) à la zone mémoire où elle se trouve. En démarrant un programme, un espace de noms **global** se crée et toutes les fonctions ou variables globales déclarée y seront consignées. Ainsi: 

```python
a = 10 
def une_fonction():
  b = a + 20
  a += 10
  return b

print(a)
```

Ici, la variable `a` et la fonction `une_fonction` sont dans l'espace de noms global. La variable `b` étant une variable locale de la fonction `une_fonction` n'est pas dans l'espace global. Dans notre programme, nous pouvons faire référence à la variable `a` de n'importe où (il faut toujours éviter les variables globales!). Selon le même raisonnement, nous pouvons appeler la fonction `une_fonction` depuis n'importe où dans notre programme. 

Supposons maintenant que nous importons notre module dans le programme: 

```python
import mod_math

a = 10 
def une_fonction():
  b = a + 20
  a += 10
  return b

print(a)
```

Un nouvel espace de noms est alors créé : l'espace de nom `mod_math`. Tout accès à un membre de cet espace de noms doit se faire en mentionnant le nom de l'espace de nom: `mod_math`. Ainsi, pour accéder à un membre de l'espace de noms global, on y accède directement. Par contre, pout tout autre espace de noms, il faut préciser son nom. 

Ceci a l'avange de nous permettre ceci: 

```python
import mod_math

def puissance(base, puiss):
  print("Fonction globale puissance!")
  return base**puiss

val1 = mod_math.puissance(10,3)
print(val1)
val2 = puissance(10,3)
print(val2)
```

Ici, nous avons deux fonctions qui s'appellent `puissance`: l'une dans l'espace de noms global, et l'autre dans l'espace de noms `mod_math` qui provient du module importé. 

Il est toutefois possible de demander à importer un module et d'ajouter sont contenu dans l'espace de noms global. Pour ce faire, nous utilisons l'instruction `from....import...`

```python
from mod_math import puissance

val1 = puissance(10,2)
print(val1)
```

Ainsi, la fonction `puissance` est importée dans l'espace de noms global, et nous pouvons y faire référence sans spécifier d'espace de noms. Il est même possible d'importer tout les identifiants d'un espace de noms dans l'espace de noms global avec `*`:

```python
from mod_math import *

val1 = puissance(10,2)
val2 = modulo(10, 3)
print(val1)
print(val2)
```

## Les paquetages

Tel qu'il a été mentionné en introduction, un paquetage est un regroupement de modules. Les modules doivent être regroupés dans un dossier. Ainsi, pour créer un paquetage, il suffit de créer un dossier dans le dossier courant. Supposons que nous créons un dossier intitulé `utils`. Nous allons déplacer, dans ce dossier, le module `mod_math` créé plus haut et ajouter un autre module dans le fichier `mod_listes.py` (que nous placerons dans le même dossier):

```python
def somme(liste):
  resultat = 0
  for item in liste:
    resultat+=item
  return resultat

def moyenne(liste):
  return somme(liste)/len(liste)

def __main():
	une_liste = [13, 23, 10, 4, 16]
	print(somme(une_liste))
	print(moyenne(une_liste))

if __name__ == '__main__':
	__main()
```

Finalement, la dernière étape pour créer notre paquetage, consiste à définir ce qui sera offer en dehors du paquetage. Pour cela, nous allons ajouter un fichier `__init__.py` qui contiendra les modules que nous souhaitons importer. Depuis Python3, ce fichier doit obligatoirement figurer dans la racine du module. 

Le fichier `__init__.py` est un fichier Python régulier mais qui sert à préparer à l'utilisation du paquetage, notamment à importer dans l'espace de noms du paquetage les modules qui seront offerts. Voici un premier fichier `__init__.py` que nous allons créer: 

```python
from .mod_math import *
from .mod_math import *
```

Revenons maintenant à notre programme *(rappel: Il se trouve en dehors du dossier `utils`)*, et importons le paquetage: 

```python
import utils

val1 = utils.mod_math.puissance(10,2)
print(val1)
```

En important le paquetage, nous créons un espace de noms `utils`. Dans cet espace de noms `utils`, deux *sous-espaces de noms* y ont été ajoutés par le fichier `__init__.py`. Par conséquent, pour accéder à la fonction puissance, nous devons parcourir les espaces de noms, en les séparant par des `.`. Donc, pour accéder à la fonction `puissance` qui se trouve dans le module `mod_math`, qui se trouve lui-même dans le paquetage `utils`, nous devons écrire `utils.mod_math.puissance()`. 

Essayons maintenant avec la syntaxe `from...import`: 

```python
from utils import mod_math

val1 = mod_math.puissance(10,2)
print(val1)
```

Ainsi, nous avons importé dans l'espace de noms global `mod_math`. Or, `mod_math` est lui même un module! Il aura donc son propre espace de noms et nous devons encore spécifier l'espace de noms `mod_math` pour accéder à notre fonction `puissance`. 

Nous aurions pu aussi importer tous les modules du paquetage: 

```python
from utils import *

val1 = mod_math.puissance(10,2)
print(val1)

une_liste = [13, 23, 10, 4, 16]
print(mod_listes.somme(une_liste))
```

Si, par contre, nous voulons vraiment que la fonction `puissance` fasse partie de l'espace de noms global. Dans ce cas, nous ferions ceci: 

```python
from utils.mod_math import puissance

val1 = puissance(10,2)
print(val1)
```

En définitive, nous pouvons importer des modules/paquetages de différentes façon, tout dépend de comment nous souhaitons les utiliser dans le code. Ceci oblige aussi à bien connaitre la structure du module qu'on veut utiliser. C'est pour cette raison que le fichier `__init__.py` peut nous être utile pour faciliter l'utilisation du paquetage. En d'autres termes, nous allons décider comment les utilisateurs de note paquetage vont l'utiliser.  Modifions, par exemple, le fichier `__init.py__` ainsi: 

```python
from .mod_math import *
from .mod_listes import *
```

Ici, nous avons décidé que toutes les fonctions des modules `mod_math` et `mod_listes` sont ajoutées à l'espace de noms du paquetage `utils`.  Ainsi, le paquetage aura l'allure d'un seul module contenant les quatre fonctions. Nous pourrions l'utiliser ainsi: 

```python
import utils

val1 = utils.puissance(10,2)
print(val1)
```

Ou encore: 

```python
from utils import *

val1 = puissance(10,2)
print(val1)
```

Supposons maintenant que notre fichier `__init__.py` contenait: 

```python
from .mod_math import puissance
from .mod_listes import moyenne
```

Seules les fonctions puissance et moyenne seront alors exposées au monde extérieur. Ainsi: 

```python
from utils import *

val1 = modulo(10,2)
print(val1)
```

produirait une erreur car la fonction `modulo()` ne fait pas partir de l'espace de noms du paquetage  `utils`, tel que ceci a été définit dans le fichier `__init__.py`.  Ceci est une technique qui permet de spécifier ce qu'un paquetage peut offrir au monde extérieur. 

## Les alias

Lorsuq'on importe un module ou un paquetage, il est possible de renommer son espace de noms en utilisant la commande `import ... as...` ou `from....import....as`. Par exemple: 

```python
import utils.puissance as puiss

val1 = puiss(10,2)
print(val1)
```

La fonction `puissance` qui a été importée du paquetage `utils` a ainsi été renommée en `puiss`. Nous pourrions également renommer le paquetage: 

```python
import utils as u

val1 = u.puissance(10,2)
print(val1)
```

Nous pouvons également utiliser cette technique dans le fichier `__init__.py` du paquetage:

```python
from .mod_math import puissance as m_puiss
from .mod_listes import moyenne as l_moy
```

Maintenant, pour utiliser notre paquetage dans notre programme principal, nous ferions ceci: 

```python
import utils

val1 = utils.m_puiss(10,2)
print(val1)
```

## Quelques normes

Tout d'abord, les commentaires. Chaque fonction d'un module ou un paquetage devrait être dûment commentée. Un module ou un paquetage permet de structurer le code mais ce sont aussi d'excellents candidats à la ré-utilisation ou à la distribution dans la communauté. La personne qui utilise votre module ou votre paquetage doit être en mesure de comprendre comment l'utiliser en lisant sa documentation avec l'outil standards de Python: la fonction `help()`. 

Les commentaires sont des *docstrings* (chaine de caractères multilignes `"""...."""` ) qu'on met au niveau du module, de la fonction et du paquetage. Nous avons déjà évoqué comment commenter convenablement une fonction. Pour commenter un module, nous utiliserons le même procédé (*docstring*) mais en plaçant le commentaire en haut du module. Voici à quoi pourrait ressembler notre module `mod_listes`:

```python
"""
Fonctions fréquemment utilisées avec les listes
"""

def somme(liste):
  """Fait la somme d'une liste"""
  resultat = 0
  for item in liste:
    resultat+=item
  return resultat


def moyenne(liste):
  """Effectue la moyenne d'une liste"""
  return somme(liste)/len(liste)


def __main():
	une_liste = [13, 23, 10, 4, 16]
	print(somme(une_liste))
	print(moyenne(une_liste))


if __name__ == '__main__':
	main()
```

Ainsi, depuis l'interpréteur interactif de Python, si nous faisons: 

```python
>>> import mod_listes
>>> help(mod_listes)
```

Voici ce qui s'affcihera: 

```
Help on module mod_listes:

NAME
    mod_listes - Fonctions fréquemment utilisées avec les listes

FUNCTIONS
    moyenne(liste)
        Effectue la moyenne d'une liste
    
    somme(liste)
        Fait la somme d'une liste
```

Pareillement, nous pouvons commenter le paquetage en ajoutant la *docstring* dans le fichier `__init__.py`: 

```python
"""Paquetage contenant des fonction très pratiques pour les calculs et les manipulations de listes"""

from .mod_math import *
from .mod_listes import *
```

Si nous demandons à afficher l'aide sur ce paquetage, voici ce que nous obtenons: 

```
Help on package utils:

NAME
    utils - Paquetage contenant des fonction très pratiques pour les calculs et les manipulations de listes

PACKAGE CONTENTS
    mod_listes
    mod_math
```

Pour finir, si votre objectif est de redistribuer votre paquetage/module, vous devriez lui donner la structure standard recommandée par Python, en y ajoutant notamment les fichiers `setup.py`, `README.md` et la License. Les détails peuvent être trouver sur la [page de documentation officielle](https://packaging.python.org/tutorials/packaging-projects/).

