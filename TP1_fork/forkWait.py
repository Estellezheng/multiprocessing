import os, sys, time

# exo 8
#Ecrire un programme forkWait.py qui crée qui :
# Récupère en ligne de commande (sys.argv) un nombre N de processus qu’il doit créer.
# Une fois que les N processus fils sont créés, il se met en attente de la fin d’exécution de ses fils.
# Dès qu’un fils se termine, il affiche l’identité (PID) de ce fils et la valeur retournée par ce fils.
#Chaque processus fils affiche son PID et le PID de son père, et ensuite il fait une pause [time.sleep()] de
#2*i secondes. Après la pause, il indique qu’il reprend son exécution avant de faire appel à exit() avec la
#valeur de i (i est le numéro de l’itération de la boucle de création des processus fils).


# Création des N processus
def creation_process(N):
    fils = []
    for i in range(1, N + 1):
        pid = os.fork()
        if pid == 0:
            print("\nJe suis le processus", os.getpid(),
                  "mon père est le processus", os.getppid())
            os._exit(i)
        else:
            fils.append(pid)

    for pid in fils:
        pid, status = os.waitpid(pid, 0)
        exit_status = os.WEXITSTATUS(status)
        print(
            f"Processus fils {pid} terminé avec la valeur {exit_status}"
        )


if __name__ == "__main__":
    N = 8
    creation_process(N)
