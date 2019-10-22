# Les exceptions

Python offre le même type de mécanismes de gestion d'exceptions qu'on retrouve (entre-autres) dans les lagages C++ ou Java. Même la syntaxe y est très ressemblante. 

Une exception est une erreur qui se produit dynamiquement, lors de l'exécution du programme, qui n'est pas une une erreur de syntaxe. D'abord voyons la différence entre les erreurs de syntaxe et les exceptions.

Une erreur de syntaxe veut dire que le programme n'est pas un programme Pyhton valide. Par exemple: 

```python
a = 10
a++
```

L'opérateur ++ qu'on retrouve en C/C++ n'existe pas en Python. Nous obtenons l'erreur suivante: 

```python
    a++
      ^
SyntaxError: invalid syntax
```

Une exceptions, par contre se produit sur un programme syntaxiquement valide mais qui, lors de l'exécution, effectue une opération erronée. Par exemple: 

```python
a = "123z" # Ou alors que l'utilisateur saisit un entier invalide
b = 10 + int(a)
```

Ce programme est syntaxiquement valide. Cependant la conversion de `a` en entier va échouer car `a` ne contient pas un entier. L'erreur qui se produit ici sera une **exception** : 

```
File "/Users/anis/ateliers/exceptions.py", line 4, in <module>
    b = 10 + int(a)
ValueError: invalid literal for int() with base 10: '123z'
```

L'interpréteur Python nous a fait remonter ici l'exception **ValueError**.

Des exceptions de tout type peuvent se produire dans un programme et celles-ci ne sont pas toujours évitables car elles dépendent des données obtenues à l'exécution. Par exemple, un usager peut ne pas saisir le type de données attendu, un serveur peut ne pas répondre lorsqu'on tente de l'interroger, ou que les données qu'il fournit ne soient pas celles à laquelles on s'attend. Lorsqu'une exception se produit, le programme est interrompu (comme pour les erreurs de syntaxe), **sauf si nous avons géré l'exception**. 

*Gérer une exception* veut dire : 

- Intercepter l'exception dans le bloc de code qui est susceptible de la déclencher et 
- Fournir le code à exécuter pour traiter le cas problématique, de sorte que notre programme reste dans un état cohérent.

## Gestion des exceptions avec `try...except...`

Supposons que nous avons écrit le code suivant: 

```python
with open("toto.txt") as file:
	data = file.read()
```

Ce code, ne pose *à priori* aucun problème. Cependant, il pose un risque: celui où le fichier qu'on tente de lire n'existe pas à l'endroit où tentons d'y accéder. Si un tel scénario se produit, l'exception suivante se produira: 

```
File "/Users/anis/ateliers/exceptions.py", line 4, in <module>
    with open("toto.txt") as file:
FileNotFoundError: [Errno 2] No such file or directory: 'toto.txt'
```

Étant donné que les chances que cette erreur se produise ne sont pas néglégeables, nous décidons de gérer cette possible exception. Pour ce faire, nous allons mettre le bloc à risque dans un bloc `try:`, et fournir le code à excécuter, dans l'éventualité où l'exception se produirait: 

```python
try: 
```





## Note sur la programmation par exceptions

Comme dans les autres langages, l'existence d'un mécanisme de gestion d'exceptions peut inciter certains programmeur-euse-s à l'utiliser de façon intensive afin de se prémunir de toute exception. Par exemple, on pourrait être tentés de mettre un programme au complet dans un `try...except...`. Non seulement ceci n'aurait que peu d'intérêt car les exceptions générées peuvent être de multiples (donc on n'y réagirait pas forcément de façon appropriée), mais il faut savoir que le mécanisme de gestion d'exceptions introduit un coût en mémoire et en performances qui serait beaucoup plus élevé que si on utilisait des blocs conditionnels `if...:`.

Par exemple: 

```python
# supposons que la variable `a` existe et qu'elle a été lue dans un fichier
b = 240
try:
  c = b / a
except ZeroDivisionError: 
  c = 0
```

Ce même traitement peut-être réalisé sans exceptions: 

```python
# supposons que la variable `a` existe et qu'elle a été lue dans un fichier
b = 240
if a!=0:
  c = b / a
else: 
  c = 0
```

Dans les deux cas, le résultat observé du traitement sera identique. Cependant, la première option a un coût bien plus important que la seconde. Cependant, cette discussion ne disqualifie pas totalement la première solution. La question à se poser est la suivante: *est-ce que le fait que `a` vaille 0 est réellement une exception, ou est-ce une possibilité tout à fait plausible que `a` vaille 0 dans les données que je suis en train de lire?* 

Si la réponse est que `a` ne devrait normalement pas contenir 0 mais que, dans la vie tout est possible, et que je veux me prémunir contre cette éventualité (programmation défensive), dans ce cas le mécanisme d'exceptions est approprié. Sinon, on préfèrera la 2e approche.

À méditer...