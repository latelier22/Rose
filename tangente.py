import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify

class InteractivePlot:
    def __init__(self, expression):
        """
        Initialise l'objet avec une fonction et sa dérivée.
        :param expression: Chaîne représentant la fonction (ex. : "x**2 - 4*x + 4")
        """
        self.x = symbols('x')  # Variable symbolique
        self.f_sym = eval(expression, {"x": self.x})  # Fonction symbolique
        self.f_prime_sym = diff(self.f_sym, self.x)  # Dérivée symbolique

        # Conversion en fonctions numériques pour tracé
        self.f = lambdify(self.x, self.f_sym, modules=['numpy'])
        self.f_prime = lambdify(self.x, self.f_prime_sym, modules=['numpy'])

        # Préparer l'intervalle de tracé
        self.xmin, self.xmax = -10, 10
        self.x_vals = np.linspace(self.xmin, self.xmax, 500)
        self.y_vals = self.f(self.x_vals)

        # Création de la figure
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.plot(self.x_vals, self.y_vals, label=f"f(x) = {expression}", color="blue")
        self.ax.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Axe des x
        self.ax.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Axe des y
        self.ax.set_title("Cliquez sur la courbe pour tracer la tangente")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.legend()
        self.ax.grid()

        # Connecter l'événement de clic
        self.fig.canvas.mpl_connect("button_press_event", self.on_click)

    def on_click(self, event):
        """
        Gère le clic de l'utilisateur pour tracer la tangente.
        :param event: Événement généré par Matplotlib
        """
        # Vérifie si le clic est dans les limites de l'axe
        if event.xdata is None or event.ydata is None:
            return

        # Récupère l'abscisse du clic
        a = event.xdata

        # Calcul de f(a) et f'(a)
        f_a = self.f(a)
        f_prime_a = self.f_prime(a)

        # Calcul de l'équation de la tangente
        y0 = f_a - f_prime_a * a  # Ordonnée à l'origine
        x_tangent = np.linspace(a - 5, a + 5, 100)
        y_tangent = f_prime_a * x_tangent + y0

        # Supprime les tracés précédents de tangentes
        for line in self.ax.lines[1:]:
            line.remove()

        # Tracé de la tangente
        self.ax.plot(x_tangent, y_tangent, label=f"Tangente : y = {f_prime_a:.2f}*x + {y0:.2f}", color="red")
        self.ax.scatter(a, f_a, color='green', label=f"Point ({a:.2f}, {f_a:.2f})")

        # Mise à jour de la légende et du graphique
        self.ax.legend()
        self.fig.canvas.draw()

    def afficher(self):
        """
        Affiche le graphique interactif.
        """
        plt.show()


# Programme principal
if __name__ == "__main__":
    expression = input("Entrez une fonction de x (par exemple : x**2 - 4*x + 4): ")
    plot = InteractivePlot(expression)  # Création de l'objet interactif
    plot.afficher()  # Affichage du graphique
