"""" Auteurs : Mehran Asadi  Matricule : 1047837
			   Lenny Siemeni Matricule : 1055234 """
class Regles:
		def __init__(self):
			"""Objet Regles qui contient la liste des regles 
				pour la survie d'une cellule, sa naissance et sa mort"""
			f=open('rules.txt','r')
			for ligneLue in f:
				ligneLue=(ligneLue.strip()).split(':')       #Ignore le \n, divise la chaine dans un tableau. ':' le separateur
				if ligneLue[0] in ['R','Y','G','B']:
					tabRegles=list(map(int,ligneLue[1].split(',')))     #convertit de string vers liste d'entier
					if ligneLue[0]=='R':
						self._rouge=tabRegles 
					elif ligneLue[0]=='G':
						self._vert=tabRegles
					elif ligneLue[0]=='B':
						self._bleu=tabRegles
					elif ligneLue[0]=='Y':
						self._jaune=tabRegles
			f.close()
