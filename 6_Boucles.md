# Les boucles

Il existe deux structures de boucles en Python: 

* les boucles `while` qui se rapproche beaucoup des boucles `while` des autres langages
* la boucle `for` qui a des particularités pythonesques.



## La boucle `while`

La syntaxe générale d'une boucle `while` est la suivante:

```python
while condition:
  <instructions1>
else:
  <instruction2>
```

Comme dans les autres langages, la liste d'instructions `instructions1` sera exécutée autant de fois que la condition est vraie. La particularité ici est le bloc optionnel  `else` qu'on ne retrouve pas ailleurs. Ce dernier sera exécuté une seule fois, lorsque la condition devient fausse. 

Par exemple: 

```python
cpt = 0
while cpt < 3:
  print("J'aime le python")
  cpt+=1
else:
  print("Et je l'aimerai toujours!")
```

Ceci affichera : 

```
J'aime le python
J'aime le python
J'aime le python
Et je l'aimerai toujours!
```

Il est aussi possible de sortir de la boucle avec l'instruction `break`. Ceci aura également pour effet d'ignorer le bloc `else`. 

Finalement, l'instruction `continue` permet d'ignorer le restant du bloc de la boucle et de passer à l'itération suivante. 

## La boucle `for..in`

La boucle `for` est un peu particulière en Python, comparativement aux autres langages. Elle s'apparente plutôt à la boucle `foreach` qu'on retrouve dans des langages tels que le PHP. 

Une boucle `for` permet ainsi d'itérer sur tous les éléments d'un objet *itérable*. Parmis les objets qu'on a déjà rencontrés, les listes, les tuples, les dictionnaires et les chaines de caractères sont des objets itérables. 

La syntaxe du `for..in...` est la suivante: 

```python
for <variable> in <iterable>:
  <instructions1>
else: 
  <instructions2>
```

La boucle s'exécutera (en répétant le traitement des `instructions1`) tant que nous avons des éléments dans `iterable`.  Par exemple: 

```python
une_liste = [10, 20, 30]
resultat = []
for val in une_liste:
  resultat+=[val*2]
  
print(resultat)
>>> [20, 40, 60]
```

Le bloc du else, si présent, s'exécutera dès que la boucle `for..in` sera terminée. Par exemple: 

```python
une_liste = [10, 20, 30]
resultat = []
for val in une_liste:
  resultat+=[val*2]
else: 
  print("Traitement de la liste terminé!")
  
print(resultat)
>>> Traitement de la liste terminé!
>>> [20, 40, 60]
```

Il est possible de simuler les boucles `for` des autres langages avec une boucle Python `for..in..` en utilisant la fonction `range`. La fonction `range` permet d'obtenir une liste d'entiers entre un entier `debut` (0 par défaut) et un entier `fin` . Ainsi: 

```python
resultat = 0
for i in range(1, 10):
  resultat+=i
  
print(resultat)
>>> 45
```

Dans l'exemple précédent, `range(1, 10)` produira la liste [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. La boucle `for..in..` itèrera sur cette liste.