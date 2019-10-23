# Les fichiers

Les gestion des fichiers est grandement simplifiée en Python, comparativement à d'autres langages. La fonction de base est la fonction `open` permettant d'ouvrir un fichier autant en lecture qu'en écriture. Comme dans les autres langages, le mode d'ouverture de fichier doit être spécifié (`r`, `w`, `a`, etc. [Voir la liste sur le site python.org](https://docs.python.org/3/library/functions.html#open)): 

```python
mon_fichier = open("fichier_texte.txt", mode = "r")
```

Sans spécifier de mode d'ouverture, l'ouverture se fera en lecture. Mon fichier sera un objet de type `TextIOBase`. Nous passons en revue les principales fonctions ci-dessous. La documentation complète de la classe peut-être trouvée [sur cette page](https://docs.python.org/3/library/io.html#io.TextIOBase).

Pour lire le contenu d'un fichier, on utilise la fonction `read`: 

```python
contenu = mon_fichier.read() #Lit jusqu'à la fin du fichier
```

Si l'on souhaite lire le fichier ligne par ligne, nous utiliserons `readline`:

```python
une_ligne = mon_fichier.readline() 
```

Une façon plus simple de lire un fichier texte ligne par ligne consiste à utiliser une boucle `for..in`: 

``` python
for une_ligne in mon_fichier:
    print(une_ligne, end='')
```

Ceci aura pour effet d'afficher chaque ligne du fichier. Chaque ligne lue comprend le caractère de retour chariot (`\n`). La fonction `print` ajoute, normalement, à la fin de chaque ligne une retour chariot également. Pour éviter que le `\n` se dédouble, on spécifie à `print` qu'elle ne doit pas ajouter le `\n` à la fin de chaque ligne (avec le paramètre nommé `end=''`) .

Une fois que nous en avons terminé avec le fichier, il faut le fermer avec la fonction `close`:   

```python
close(mon_fichier)
```

Il existe aussi une forme d'ouverture d'un fichier qui évite de devoir le fermer, en utilisant un bloc `with`.  Le fichier sera fermé automatiquement à la fin du bloc `with`: 

```python
with open("fichier_texte.txt", mode="r") as mon_fichier:
    for ligne in mon_fichier:
        print(ligne, end='')
```

Un fichier peut également être ouvert en écriture (et création ou ajout). Pour écrire dans un fichier, nous utiliserons la fonction `write`: 

```python
with open("nouveau_fichier.txt", mode="w") as fichier:
    fichier.write("J'ai créé mon premier fichier en Python!\n")
    fichier.write("C'est plus facile que je pensais finalement..."
```

Finalement, et comme pour les langages tels que C/C++ et Java, il est possible de changer la position actuelle au sein d'un fichier en utilisant la fonction `seek(offset)`. Pour connaître la position actuelle dans un fichier, on utilisera la fonction `tell()`.

## À propos de l'encodage

Par défaut, votre script Python utilise l'encodage par défaut définit pour votre plateforme. Par exemple, sous Windows, les fichiers lus ou écrits le seront en utilisant l'encodage `cp1252`. Sous Linux ou MacOS, l'encodage utilisé sera `utf-8`.  

Pour éviter des problèmes de lecture/écriture lorsqu'un programme manipule des fichiers provenant de plusieurs plateformes, il est prudent de spécifier un encodage lors de l'ouverture des fichiers. Nous le faisons en utilisant le paramètre nommé `encoding`: 

```python
with open("mon_fichier.txt", mode="w", encoding="utf-8") as f:
    f.write("J'écris en UTF8")
```

Vous pouvez aussi consulter la [liste complète des format d'encodage standards disponibles](https://docs.python.org/3/library/codecs.html#standard-encodings).