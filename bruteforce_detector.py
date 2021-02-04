import os
import subprocess
from collections import Counter
from os import walk
import re


#parcourir les fichiers dans un repertoire donne
def parcourir_repertoire(repertoire):

    listeFichiers = []
    for (repertoire, sousRepertoires, fichiers) in walk(repertoire):
        listeFichiers.extend(fichiers)
        
    for f in listeFichiers:
        trouver_les_ip(f)
        with open('output.txt', 'r') as f2:
            fff = f2.read()
        ip_addresses = fff.split("\n")
        if len(ip_addresses) > 1 :
            #recuperer les adresses ip avec leur nombre d'apparition dans un fichier
            count = Counter(ip_addresses)
            plus_commun = count.most_common(len(count))
            print "Dans le fichier : " + f
            verifier_ip(plus_commun)
            print "\n-------------------------------------------------------\n\n"
            

#trouver les adresses ip dans un fichier et les mettre dans un fichier output.txt
def trouver_les_ip(fichier):
    with open("/home/humex/Desktop/var/log/"+fichier, 'r') as file:
        fi = file.readlines()
    f2 = open('output.txt', 'w')
    #expression reguliaire pour recuprer les adresses ip dans le fichier
    #on simule une adresse ip \d pour decimale
    re_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    for line in fi:
        ip = re.findall(re_ip, line)
        if len(ip) != 0:
            #on ecrit l'adresse ip dans le fichier output
            f2.write("\n".join(ip))
            f2.write("\n")
    f2.close()


def verifier_ip(yy):
    #on recupere le nombre d'apparition de chaque adresse ip
    nb_occurences = [addr for cnt,addr in yy]    
    les_ip = [addr for addr,cnt in yy]
    for i in range(0, len(les_ip)):
        if nb_occurences[i] > 10:
            print "L'adresse "+les_ip[i]+" a fait une attaque Brute force"



parcourir_repertoire("/home/humex/Desktop/var/log/")
