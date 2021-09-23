def lecture_fichier(nom_fichier):
    try:
        with open(nom_fichier) as file:
            data = file.read()
            a = 10 / 0
    except FileNotFoundError:
        print("Fichier introuvable.")
        data = ""
    finally:
        print("Dans le bloc finally")
        data = data.strip()

try:
	lecture_fichier("exerciceA2.py")
except ZeroDivisionError: 
	print("Une erreur de division par zéro a été remontée par lecture_fichier!")