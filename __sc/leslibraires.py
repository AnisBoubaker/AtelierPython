# -*- coding: utf-8 -*-

"""Module offrant la fonction scrape qui permet d'extraire une liste de prix depuis une
page de recherche du site LesLibraires.ca"""

from bs4 import BeautifulSoup
import requests

#url = "https://www.leslibraires.ca/recherche/?s=michel+tremblay&p=1"

def scrape(url):
	"""Récupère les informations de produit à partir d'une page de recherche du site leslibraires.ca. 
	Le résultat obtenu est une liste ayant le format: 
	 	[{titre_du_livre:prix} ...]
	Pour chaque résultat: 
	- titre_du_livre est une chaine de caractères (str)
	- prix est un réel (float)
	"""
	contenu = requests.get(url)

	if contenu.status_code != 200:
		raise ValueError('Accès impossible au site.')

	soup = BeautifulSoup(contenu.content, 'html.parser')
	liste_prix = soup.select("li.book div.book-desc ul li h4 span.price")

	prix_reels = []
	for prix in liste_prix:
		prix_reels+=[float( prix.string[:-2].replace(",", ".") )]

	liste_titres = soup.select("li.book div.book-desc h2 a")
	titres_reels = []
	for titre in liste_titres:
		titres_reels += [titre.string]

	ouvrages = zip(titres_reels, prix_reels)
	return dict(ouvrages)

def __main():
	livres = scrape("https://www.leslibraires.ca/recherche/?s=michel+tremblay&p=1");
	print(livres)


if __name__ == "__main__":
	__main()