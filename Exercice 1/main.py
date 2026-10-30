from Chien import Chien
from Chat import Chat

# Fonction principale
def faire_parler(animal):
    print(animal.parler())


# Programme principal
if __name__ == "__main__":

    animaux = [
        Chien(),
        Chat(),
        Chien()
    ]

    for a in animaux:
        faire_parler(a)