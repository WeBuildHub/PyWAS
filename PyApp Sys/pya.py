"""PyApps Systems for modders - recreez votre avenir"""
# -*- coding: UTF-8 -*-
import os, sys

def out(caractere_a_afficher):
	"""Imprime le resultat de ce que vous entrez en parametre"""
	print(caractere_a_afficher)
	pass
def log(stri):
	"""Enregistre un Log dans le fichier Log"""
	lg = open("logs.log", "a")
	lg.write("...___...\n")
	lg.write(stri)
	lg.close
	pass
def start(log):
	"""Inscrit le depart du programme dans le fichier Log personnalisé"""
	lg = open(log ".log", "w")
	lg.write("Log of")
	pass
def ins(nom, repertoire):
	"""Instore un nouveau repertoire dans le répertoire courant grace au module os de Windows"""
	os.system('mkdir ', nom, repertoire)
	pass

def fun():
	print('C\'EST FUN NON ?')
	pass