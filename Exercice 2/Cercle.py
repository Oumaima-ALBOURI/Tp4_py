from Forme import Forme
import math

class Cercle(Forme):

    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2