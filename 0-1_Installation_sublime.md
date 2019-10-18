# L'éditeur Sublime pour développer en Python

L'interpréteur interactif *PyPy* est assez pratique pour tester des commandes, mais il n'est absolument pas adapté pour écrire des programmes. Pour ce faire, nous devons écrire le code de notre programme dans un éditeur afin d'être en mesure de le ré-exécuter.

Plusieurs environnements de développement en Python existent sur le marché, dont:
- IDLE: l'éditeur fournit avec Python lorsqu'on le télécharge depuis [python.org](Python.org);
- PyCharm: disponible depuis [JetBrains](https://www.jetbrains.com/pycharm/download/) (commercial mais gratuit pour les étudiants);
- Spider: Disponible depuis [spider-ide.org](https://www.spyder-ide.org/)
- et bien d'autres.

Ces éditeurs offrent beaucoup de fonctionnalités qui aident au développement. Cependant toutes ces facilités offertes ne sont pas nécessaires à notre niveau et seraient même contre productives pour bien débuter. Nous allons donc utiliser un simple éditeur de textes: Sublime. Toutefois, Sublime offre quelques facilités bienvenues pour nous, notamment:
- la coloration syntaxique
- la possibilité d'exécuter le code directement depuis l'éditeur.

### Installation de Sublime

- Téléchargez Sublime depuis [sublimetext.com](https://www.sublimetext.com/download)
- Nous allons maintenant vérifier que Sublime est bien configuré pour la compilation en Python3. Créez un nouveau fichier contenant le code suivant:
```python
import sys 
print(sys.version)
```
- Sauvegardez le fichier en mettant `.py` comme extension (ex.: test.py)
- Exécutez le programme en pressant CTRL+B
- Vérifiez le numéro de version de Python qui s'affiche. 
- Si le numéro de version est dans la série 3.x.x, vous avez terminé.
- Sinon, vous devez configurer Sublime pour qu'il utilise la version 3 de Python. Pour ce faire [suive ce gist](https://gist.github.com/zaemiel/4fbd8b5125fda7a140be)
