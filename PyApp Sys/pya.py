"""PyApps Systems for modders - recreez votre avenir"""
# -*- coding: UTF-8 -*-
import os, sys

def out(caractere_a_afficher):
	"""Imprime le resultat de ce que vous entrez en parametre"""
	print(caractere_a_afficher)
	pass
def log(stri):
	"""Enregistre un Log dans le fichier Log"""
	lg = open("Logs.log", "a")
	lg.write("...___...\n")
	lg.write(stri)
	lg.close
	pass
def start(log):
	"""Inscrit le depart du programme dans le fichier Log personnalisé"""
	lg = open("Logs.log", "w")
	lg.write("Log of")
	pass
def ins(nom, repertoire):
	"""Instore un nouveau repertoire dans le répertoire courant grace au module os de Windows"""
	os.system('mkdir ', nom, repertoire)
	pass

def fun():
	print('C\'EST FUN NON ?')
	pass
def openF(f, t, c):
	""""""
	if t == "lire":
		file = open(f, "r")
		pass
	if t == "re-ecrit":
		file = open(f, "w")
		file.write(c)
	if t == "rajouter":
		file = open(f, "a")
		file.write(c)
	file.close()
	pass
def userIn(message):
	"""Permet a l'utilisateur de saisir des donnees renvoyees par la fonction"""
	in = raw_input(message)
	return in
	pass
