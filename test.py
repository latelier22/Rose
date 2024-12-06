class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def saluer(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")



# Création d'un objet
perso1 = Personne("Cyrille", 49)


perso1.saluer()

# commentaire
perso2 = Personne("Rose",15)
perso2.saluer()


class Trinome:
   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
      self.delta = b**2-4*a*c


trinome1 = Trinome(1,2,1)

print(trinome1.delta)

