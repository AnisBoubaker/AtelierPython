# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

def scrape(url):
	contenu = requests.get(url)

	if contenu.status_code != 200:
		raise ValueError('Accès impossible au site.')

	soup = BeautifulSoup(contenu.content, 'html.parser')
	print(contenu.content)
	liste_prix = soup.select("table.pRowCtrl tbody tr td.pmWi div.cont div.divPrice span")

	prix_reels = []
	for prix in liste_prix:
		prix_reels+=[float( prix.string[:-2].replace(",", ".") )]

	liste_titres = soup.select("table.pRowCtrl tbody tr td.pmWi table.prod tbody tr td a")
	titres_reels = []
	for titre in liste_titres:
		titres_reels += [titre.string]

	ouvrages = zip(titres_reels, prix_reels)
	return dict(ouvrages)

def __main():
	livres = scrape("https://www.renaud-bray.com/Recherche.aspx?langue=fr&words=michel+tremblay&wbgc_iNo=1&type=1&root=0&supersection=2&cPage=1&pSize=50");
	print(livres)


if __name__ == "__main__":
	__main()