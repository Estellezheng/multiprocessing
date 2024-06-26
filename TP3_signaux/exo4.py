
import os
import signal
import sys
import time
 

"""Ecrire un programme composé de 2 processus : Le père fait des affichages toutes les
secondes dans une boucle for et le fils fait des affichages toutes les secondes aussi mais dans une boucle
infinie. Quand le compteur de boucle du père arrive à 3, le père envoie un signal SIGKILL au fils. On a
constaté dans l'exercice 2, l'impossibilité d'ignorer ce signa"""

def child_process():
    """Processus fils qui affiche un message dans une boucle infinie."""
    while True:
        print("Fils: En cours...")
        time.sleep(1)

def parent_process(child_pid):
    """Processus père qui affiche un message dans une boucle et tue le fils après 3 itérations."""
    for i in range(3):
        print(f"Père: Compteur = {i}")
        time.sleep(1)

    print("Père: Envoi de SIGKILL au fils")
    os.kill(child_pid, signal.SIGKILL)

if __name__ == "__main__":

    pid = os.fork()
    if pid > 0:
        parent_process(pid)
    else :
        child_process()
