import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify

def main():
    # Définition de la variable symbolique
    x = symbols('x')

    # Saisie de la fonction par l'utilisateur
    expression = input("Entrez une fonction de x (par exemple : x**2 + 3*x + 2): ")
    fonction = eval(expression)  # Interprétation de l'expression

    # Calcul de la dérivée
    derivee = diff(fonction, x)
    print(f"La dérivée de la fonction est : {derivee}")

    # Conversion de la fonction et de sa dérivée en fonction numérique pour évaluation
    f = lambdify(x, fonction, modules=['numpy'])
    f_prime = lambdify(x, derivee, modules=['numpy'])

    # Saisie de l'abscisse pour tracer la tangente
    a = float(input("Entrez l'abscisse (a) pour tracer la tangente : "))

    # Valeurs pour la tangente
    f_a = f(a)  # f(a)
    f_prime_a = f_prime(a)  # f'(a)
    y0 = f_a - f_prime_a * a  # Ordonnée à l'origine de la tangente

    # Tracé de la fonction et de la tangente
    xmin, xmax = -10, 10
    x_vals = np.linspace(xmin, xmax, 500)
    y_vals = f(x_vals)

    # Tangente : y = f'(a) * x + y0
    y_tangent = f_prime_a * x_vals + y0

    # Création du graphique
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f"f(x) = {expression}", color='blue')
    plt.plot(x_vals, y_tangent, label=f"Tangente en x={a}: y = {f_prime_a:.2f}*x + {y0:.2f}", color='red')
    plt.scatter(a, f_a, color='green', label=f"Point ({a}, {f_a:.2f})")
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Axe des x
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Axe des y

    # Personnalisation du graphique
    plt.title("Tracé de la fonction et de la tangente")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()

# Lancer le programme
if __name__ == "__main__":
    main()
