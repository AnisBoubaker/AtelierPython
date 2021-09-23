# Exercices

### A. Les bases (variables, opérateurs, chaines de caractères, structures conditionnelles)

1. Supposez que vous ayez deux variables `a`et `b`. Écrivez le code permettant de permuter le contenu des deux variables.
2. Écrire un programme qui demande à l'utilisateur de saisir les dimensions d'une pièce rectangulaires. Votre programme doit lui afficher la superficie de la pièce. 
3. Écrire le code permettant de conserver, dans une chaine de caractères, les deux première lettres et les deux dernières (de n'importe quelle chaine de caractères initiale). Si la chaine initiale contient moins que 4 caractères, le résultat devrait être une chaine vide.
4. Écrire un programme qui remplace toutes les occurences du premier caractère d'une chaine de caractères par des *, sauf le premier. Par exemple, si la chaine initiale était`nonne`, le résultat serait  `no**e`. 

### B. Structures de données

1. Écrire un programme qui construit une liste contenant exactement la première moitié des éléments d'une autre liste.
2. Sans utiliser la fonction reverse, écrire un programme qui inverse les éléments d'une liste. (*indice: pensez au découpage (slicing)*)
3. Écrire un programme qui construit une liste à partir d'une autre liste, en prenant le cube de chaque éleément si celui-ci est multiple de 4.
4. Écrire un programme qui génère crée une matrice identité de taille 3x3: 
   <img src="./images/idMatrix.png" alt="Matrice 3x3" style="zoom:50%;" />
   La matrice peut être représentée par une liste de listes (ci-dessous). Celle-ci doit être créée de façon automatique. 

```python
[ [1, 0, 0], 
  [0, 1, 0], 
  [0, 0, 1]]
```



## C. Les boucles

1. Écrire un programme qui affiche tous les éléments d'une liste en ordre inverse. 

2. Écrire un programme qui affiche tous les nombres multiples de 3 d'une liste d'entiers. 

3. Écrire un programme qui affiche tous les nombres multiples de 3 inférieurs à qui sont inférieurs à 100

4. En disposant d'un dictionnaire dont les clés sont des chaines de caractères et les valeurs sont des entiers, écrivez un programme qui affiche sur chaque ligne les éléments du dictionnaire en respectant la forme: `clé = valeur `
   Par exemple, si nous disposons de la variable `mon_dict = {'a':10, 'b':20, 'c':30}`, votre programme devra l'afficher sous cette forme: 

   ```
   a = 10
   b = 20
   c = 30
   ```

### C. Fonctions

Pour chacune des fonctions suivantes, vous devez écrire la fonction demandée et la tester en y faisant appel. 

1. Écrire une fonction qui reçoit deux tuples contenant la latitute et la longitude de deux points sur terre. Votre fonction doit calculer la distance entre ces deux points. 

   En supposant `lat1` et `lon1` la latitude et la longitude du premier point, `lat2` et `lon2` celles du deuxième point, la distance se calcule selon la formule suivante: 

   ```
   distance = 6371.01 × acos(sin(lat1) × sin(lat2) + cos(lat1) × cos(lat2) × cos(lon1 − lon2))
   ```

   Notez que, pour utiliser les fonctions mathématique, vous devez importer le module `math`: 

   ```python
   from math import *
   ```

2. Écrire une fonction qui lit demande à l'utilisateur de saisir des entiers dans la console, et qui s'arrête lorsque l'utilisateur saisit une chaine vide ou une chaine qui n'est pas un nombre. Ensuite votre fonction doit afficher les valeurs saisies en commençant par les valeurs négatives, les valeurs nulles puis les valeurs positives. Par exemple, si l'utilisateur saisit les valeurs dans cet ordre: 3, -4, 1, 0, -1, 0, et -2 , votre programme doit afficher: -4, -1, -2, 0, 0, 3, 1.   

3. Écrire une fonction qui reçoit un montant d'argent en *sous* et qui renvoie un dictionnaire indiquant combien cela ferait en billets de 100\$, 20\$, 10\$ et 5\$, et combien de pièces de 2\$, 1\$, 25cts et 1cts. 