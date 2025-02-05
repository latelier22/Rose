from flask import Flask, render_template, request
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Utilisation du backend non interactif
import matplotlib.pyplot as plt
import random
import os

app = Flask(__name__)

# Assurez-vous que le dossier "static" existe pour stocker les images
if not os.path.exists("static"):
    os.makedirs("static")

# Définition des listes nécessaires
angles_remarquables = [0, 30, 45, 60, 30, 45, 60, 90, 120, 135, 150, 180, -30, -45, -60,-30, -45, -60, -90, -120, -135, -150, -180]
unites = ["m", "N", "m/s"]
axes_reference = ["x", "-x", "y", "-y"]

def generate_vector_image():
    """Génère une image d'un vecteur aléatoire et retourne ses caractéristiques."""
    V = random.randint(1, 10)  # Intensité entre 1 et 10
    theta_deg = random.choice(angles_remarquables)  # Angle parmi les valeurs remarquables
    reference_axis = random.choice(axes_reference)  # Axe de référence
    unite = random.choice(unites)  # Unité choisie

    theta = np.radians(theta_deg)

    # Sélection d'un axe de référence et d'un angle
    arc_start_angle = 0 if reference_axis == "x" else (
        np.pi if reference_axis == "-x" else (
        np.pi / 2 if reference_axis == "y" else -np.pi / 2))
    
    # Ajuster le sens de l'arc en fonction du signe de theta
    arc_end_angle = arc_start_angle + theta  # Rotation trigonométrique

    arc_theta = np.linspace(arc_start_angle, arc_end_angle, 30)
    
    # Calcul des composantes Vx et Vy en fonction de l'axe choisi
    if reference_axis == "x":
        Vx, Vy = V * np.cos(theta), V * np.sin(theta)
    elif reference_axis == "-x":
        Vx, Vy = V * np.cos(theta-np.pi), V * np.sin(theta-np.pi)
    elif reference_axis == "y":
        Vy, Vx = V * np.cos(theta), -V * np.sin(theta)
    else:  # reference_axis == "-y"
        Vy, Vx = -V * np.cos(theta), V * np.sin(theta)


    # Création de la figure
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.quiver(0, 0, Vx, Vy, angles='xy', scale_units='xy', scale=1, color='b')
    
    # Tracé de l'arc de cercle indiquant l'angle
    arc_radius = V / 3
    arc_theta = np.linspace(arc_start_angle, arc_start_angle + np.radians(theta_deg), 30)
    arc_x = arc_radius * np.cos(arc_theta)
    arc_y = arc_radius * np.sin(arc_theta)
    ax.plot(arc_x, arc_y, 'purple', linewidth=1.5)
    ax.text(arc_x[5]+0.3, arc_y[5]+0.3, rf'$\theta={abs(theta_deg)}^\circ$', fontsize=12, color='purple')

    # Réglages
    ax.set_xlim(-V - 2, V + 2)
    ax.set_ylim(-V - 2, V + 2)
    ax.set_xlabel("Axe X")
    ax.set_ylabel("Axe Y")
    ax.set_title("Décomposition d'un vecteur en composantes")
    ax.grid(True, linestyle="--", alpha=0.5)

    # Sauvegarde de l'image
    image_path = "static/vector.png"
    plt.savefig(image_path)
    plt.close()

    return V, theta_deg, Vx, Vy, arc_start_angle, reference_axis, unite, image_path

@app.route("/", methods=["GET", "POST"])
def index():
    """Affiche la page web avec l'énoncé et le formulaire"""
    message = None
    show_components = False  # N'affiche pas les composantes au début

    V, theta_deg, Vx, Vy, arc_start_angle, reference_axis, unite, image_path = generate_vector_image()

    if request.method == "POST":
        try:
            user_Vx = float(request.form["vx"])
            user_Vy = float(request.form["vy"])
            
            # Vérification des réponses avec tolérance de 0.1
            if abs(user_Vx - Vx) < 0.1 and abs(user_Vy - Vy) < 0.1:
                message = "✅ Bonne réponse !"
            else:
                message = (f"❌ Mauvaise réponse. Les bonnes valeurs étaient : "
                           f"Vx = {Vx:.2f} {unite}, Vy = {Vy:.2f} {unite}.")
            
            show_components = True  # Afficher les composantes après validation
        except ValueError:
            message = "⚠️ Veuillez entrer des nombres valides."

    return render_template("index.html", V=V, Vx=Vx, Vy=Vy, arc_start_angle=arc_start_angle, theta_deg=abs(theta_deg), reference_axis=reference_axis,
                           unite=unite, image_path=image_path, message=message, show_components=show_components)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)