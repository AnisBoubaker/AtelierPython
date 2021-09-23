# Les structures conditionnelles

Une structure conditionnelle permet de spécifier du code qui s'exécutera si une condition est vérifiée. Python ne déroge pas des autres langages et offre la traditionnelle structure `if..else`. Cependant, la syntaxe est quelque peu différente: 

```python
if <expression>:
  <instructions>
```

Par exemple: 

```python
if age >= 18:
  printf("Vous etes majeur-e!")
  offrir_de_lalcool()
```

Comme vous le remarquez, le bloc de code qui s'exécute si l'expression `age>=18` est vraie n'est pas délimité par des `{ ... }`. C'est l'indentation du code qui définit ce qui est exécuté. Remarquez également que la condition qui suit le mot-clé `if` n'est pas entre parenthèses (celles-ci sont optionnelles).

Notez que, du fait que l'indentation détermine un bloc de code, il n'est pas possible d'avoir des blocs vide. Bien que l'utilité d'un bloc vide soit souvent discutable, il est possible de passer outre cette limitation en utilisant l'instruction `pass`. Par exemple: 

```python
if x == 10:
  
print("Je ne suis pas dans le if!")
```

Ceci causera une erreur car le bloc du `if` est vide. Pour régler le problème, nous utilisons `pass`:

```python
if x == 10:
  pass
print("Je ne suis pas dans le if!")
```

Donc si `x` est bien égal à 10, rien de sera fait. le `print` sera exécuté quelque soit la valeur de `x`.

Il est possible d'utiliser la clause `else` pour définir du code qui s'exécute si la condition est fausse:  

```python
if age >= 18:
  print("Vous etes majeur-e!")
  offrir_de_lalcool()
else: 
  print("Désolé, attendez quelques années")
```

Finalement, nous pouvons avoir des conditions mutuellement exclusives en utilisant le mot clé `elif`: 

```python
if age >= 18:
  print("Vous etes majeur-e!")
  offrir_de_lalcool()
elif age >= 16:
  print("Vous y êtes presque! Apprenez à conduire d'abord.")
  passer_son_permis()
else: 
  print("Désolé, attendez quelques années")
```

Ainsi, on recommandera le passage de permis uniquement si l'age de la personne est dans l'intervalle [16, 18[ ans.

### L'opérateur ternaire

Le mal-aimé des langages de programmation, j'ai nommé l'opérateur ternaire `__?__:__`, existe aussi en Python, mais il est beaucoup plus lisible. Voici sa syntaxe: 

```python
variable = <val_si_vrai> if <condition> else <val_si_faux>
```

Par exemple: 

```python
peut_boire = True if age>=18 else False
```

### Le Switch-Case

La plupart des autres langages de programmation implémentent une structure conditionnelle `switch...case` permettant d'exécuter des instructions selons plusieurs cas de figure. Cette structure n'existe pas en Python. Le `if...elif....elif...else` peut jouer le même rôle. D'autre façons de faire existent aussi, en utilisant les fonctions et Google saura vous en dire plus.