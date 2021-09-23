import renaud_bray
import leslibraires
from tabulate import tabulate


# on récupère les données [{'titre':..., 'prix':...}]
liste_leslibraires = leslibraires.scrape("https://www.leslibraires.ca/recherche/?s=michel+tremblay&p=1");
liste_renaudb = renaud_bray.scrape("https://www.renaud-bray.com/Recherche.aspx?langue=fr&words=michel+tremblay&wbgc_iNo=1&type=1&root=0&supersection=2&cPage=1&pSize=50")

precision = 15 # nombre de caractères considérés pour établir la correspondance entre titres de livres

# On construit la liste des résultats communs (selon précision) et la liste de tous les résultats
resultats_communs = set(s[:precision] for s in liste_renaudb.keys()) & set(s[:precision] for s in liste_leslibraires.keys())
tous_rersultats = set(liste_renaudb.keys()).union(liste_leslibraires.keys())

# On construit la liste de comparaison: les deux prix si les résultats sont commun, un seul prix sinon
comparatif = []
for resultat in tous_rersultats:
	if resultat[:precision] in resultats_communs:
		comparatif+=[{'titre':resultat, \
		'prix_rb':[value for key,value in liste_renaudb.items() if resultat[:precision]==key[:precision]], \
		'prix_lb':[value for key,value in liste_leslibraires.items() if resultat[:precision]==key[:precision]]}]
	elif resultat in liste_renaudb:
		comparatif+=[{'titre':resultat, \
		'prix_rb':[value for key,value in liste_renaudb.items() if resultat==key], \
		'prix_lb':[]}]
	elif resultat in liste_leslibraires:
		comparatif+=[{'titre':resultat, \
		'prix_rb':[], \
		'prix_lb':[value for key,value in liste_leslibraires.items() if resultat==key]}]

# On termine par trier les résultats et on affiche.
comparatif.sort(key=lambda x: x['titre'])

print( tabulate(comparatif, headers={'titre':'Titre', 'prix_rb':'Prix RB', 'prix_lb':'Prix LB'}) )