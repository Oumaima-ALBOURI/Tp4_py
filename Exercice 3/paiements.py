
from abc import ABC, abstractmethod


# Classe mère
class Paiement(ABC):

    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")

        self._montant = montant

    @abstractmethod
    def payer(self):
        pass


# Classe CarteBancaire
class CarteBancaire(Paiement):

    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        self.numero = numero
        self.cvv = cvv

    def payer(self):
        return f"Paiement par Carte Bancaire : {self._montant} DH"


# Classe PayPal
class PayPal(Paiement):

    def __init__(self, montant, email, token):
        super().__init__(montant)
        self.email = email
        self.token = token

    def payer(self):
        return f"Paiement par PayPal : {self._montant} DH"


# Classe Crypto
class Crypto(Paiement):

    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        self.wallet_id = wallet_id
        self.reseau = reseau

    def payer(self):
        return f"Paiement par Crypto ({self.reseau}) : {self._montant} DH"


# Fonction de traitement
def traiter_paiements(liste):
    for paiement in liste:
        print(paiement.payer())


# Programme principal
if __name__ == "__main__":

    paiements = [
        CarteBancaire(200, "1234567890123456", "123"),
        CarteBancaire(350, "9876543210987654", "456"),
        PayPal(150, "alice@gmail.com", "TOKEN123"),
        PayPal(250, "bob@gmail.com", "TOKEN456"),
        Crypto(500, "WALLET001", "BTC"),
        Crypto(700, "WALLET002", "ETH")
    ]

    traiter_paiements(paiements)
