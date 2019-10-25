# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

#url = "https://www.leslibraires.ca/recherche/?s=michel+tremblay&p=1"

def scrape(url):
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