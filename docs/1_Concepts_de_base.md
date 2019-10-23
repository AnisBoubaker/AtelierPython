# À propos de Python

Le Python est un lagage qui est devenu fort populaire autant dans l'industrie que dans la recherche car il est très adapté à plusieurs contextes et est facile d'approche. Dans ce document, nous passons en revue quelques unes de ses particularités.

### 1. Un langage interprété

Le langage Python est un langage interprété. Ceci veut dire que le code qu'on écrit ne sera pas compilé (au sens traditionnel du terme) et un fichier exécutable ne sera pas généré. L'interpréteur Python exécute le code, au fur-et-à-mesure. Ceci procure aux programmes Python l'avantage de la portabilité: le même code peut être exécuté sur plusieurs plateformes, sans nécessiter de recompilation. Cependant, ceci est aussi un désavantage car le code ne sera pas optimisé et exécutable directement sur la plateforme : l'interpréteur doit s'exécuter pour interpréter le code Python et ceci introduit un surcout en termes de performances et d'occupation mémoire.

Le programmes en python ont traditionnellement l'extension `.py`. Pour exécuter un programme en Python, il faut donc l'exéter à travers l'interpréteur: 

```bash
python mon_programme.py
```



### 2. Un langage typé dynamiquement

Contrairement à certains langages comme le C/C++ ou Java, le Python est un langage typé dynamiquement. Ceci veut dire qu'il n'est pas nécessaire de déclarer les variables et les associer à un type spécifique. Ceci ne veut pas dire que les variables n'ont pas de type, mais plutôt que le type des variables est déterminé par l'interpréteur à l'exécution. 

Bien que ceci simplifie la création de variables, celà peut poser des risques à la maintenabilité des programmes (les vérifications statiques par le compilateur ne sont plus possibles). 

### 3. Des structures de données implantées et intégrées dans le langage

Le Python permet de créer facilement des données complexes (listes, dictionnaires, types) mutables. De plus, des opérateurs du langage permettent de manipuler facilement ces structures et de bâtir des algorithmes (ex.: le slicing). 

### 3. Un langage extensible

L'intérêt des développeurs dans le langage a permis de développer un catalogue important de modules et de librairies directement accessibles. Un mécanisme simple de téléchagement et d'inclusion de ces librairies (`pip`) dans un programme fait partie des outils offerts par le langage. 

### 4. Un langage... pythonesque (*pythonic*)

Ce qui fait certainement le réputation de Python c'est le style adopté lors de l'écriture de programmes. Le langage a été conçu de telle sorte que le code soit facilement lisible en minimisant le la quantitié de code à écrire pour effectuer des opérations communes. La syntaxe épurée du langage (ex.: pas de { } ni de ; ) contribue à cette facilité d'écriture et de lecture du code.