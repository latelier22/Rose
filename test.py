import numpy as np
import matplotlib.pyplot as plt



class Trinome:
    def __init__(self, a, b, c):
        """
        Initialise un trinôme ax² + bx + c.
        :param a: Coefficient de x²
        :param b: Coefficient de x
        :param c: Terme constant
        """
        self.a = a
        self.b = b
        self.c = c
        self.delta = b**2 - 4*a*c

    def tracer(self, xmin=-10, xmax=10, points=500):
        """
        Trace le trinôme ax² + bx + c sur l'intervalle [xmin, xmax].
        :param xmin: Limite inférieure de l'intervalle
        :param xmax: Limite supérieure de l'intervalle
        :param points: Nombre de points pour le tracé
        """
        x = np.linspace(xmin, xmax, points)  # Génère les points x
        y = self.a * x**2 + self.b * x + self.c  # Calcule les valeurs y

        # Tracé du trinôme
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f"{self.a}x² + {self.b}x + {self.c}", color="blue")
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Axe des x
        plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Axe des y

        # Informations supplémentaires
        plt.title("Tracé du trinôme")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid()
        plt.show()

# Demande des coefficients à l'utilisateur
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Création de l'objet Trinome
trinome1 = Trinome(a, b, c)

# Affichage du discriminant
print(f"Delta = {trinome1.delta}")

# Tracé du trinôme
xmin = float(input("Entrez xmin : "))
xmax = float(input("Entrez xmax : "))
trinome1.tracer(xmin=xmin, xmax=xmax)
