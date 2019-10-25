# -*- coding: utf-8 -*-

"""Module offrant la fonction scrape qui permet d'extraire une liste de prix depuis une
page de recherche de Renaud-Bray"""

from bs4 import BeautifulSoup
import requests

def scrape(url):
	"""Récupère les informations de produit à partir d'une page de recherche du site de RenaudBray. 
	Le résultat obtenu est une liste ayant le format: 
	 	[{titre_du_livre:prix} ...]
	Pour chaque résultat: 
	- titre_du_livre est une chaine de caractères (str)
	- prix est un réel (float)
	"""

	contenu = requests.get(url)

	# En cas d'erreur de connexion, on lève une exception ValueError
	if contenu.status_code != 200:
		raise ValueError('Accès impossible au site.')

	soup = BeautifulSoup(contenu.content, 'html.parser')
	
	# Récupération de la liste de tous les prix de la page
	liste_prix = soup.select("table.pRowCtrl tr td.pmWi div.cont div.divPrice span.lblPrice")
	prix_reels = []
	for prix in liste_prix:
		prix_reels+=[float( prix.string[:-2].replace(",", ".") )]

	# Ensuite on récupère les titres
	liste_titres = soup.select("table.pRowCtrl tr td.pmWi table.prod tr td a")
	titres_reels = []
	for titre in liste_titres:
		titres_reels += [titre.string]

	# Finalement, on se crée un beau dictionnaire contenant les titres comme clé et les prix comme valeur
	ouvrages = zip(titres_reels, prix_reels)
	return dict(ouvrages)

def __main():
	livres = scrape("https://www.renaud-bray.com/Recherche.aspx?langue=fr&words=michel+tremblay&wbgc_iNo=1&type=1&root=0&supersection=2&cPage=1&pSize=50");
	print(livres)


if __name__ == "__main__":
	__main()
