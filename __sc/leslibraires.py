# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


url = "https://www.leslibraires.ca/recherche/?s=michel+tremblay&p=1"
contenu = requests.get(url)

if contenu.status_code != 200:
	exit()

soup = BeautifulSoup(contenu.content, 'html.parser')
liste_prix = soup.select("li.book div.book-desc ul li h4 span.price")

prix_reels = []
for prix in liste_prix:
	prix_reels+=[float( prix.string[:-2].replace(",", ".") )]

liste_titres = soup.select("li.book div.book-desc h2 a")
titres_reels = []
for titre in liste_titres:
	titres_reels += [titre.string]

print(prix_reels)
print(titres_reels)

with open("titres.txt", "w") as fichier:
	for titre in titres_reels:
		fichier.write(titre + '\n')

