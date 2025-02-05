def configuration_electronique(atomic_number):
    """
    Calcule la configuration électronique d'un atome donné en fonction de son numéro atomique.
    :param atomic_number: Numéro atomique de l'élément
    :return: Configuration électronique sous forme de chaîne
    """
    orbitals = [
        (1, 's'), (2, 's'), (2, 'p'), (3, 's'), (3, 'p'), (4, 's'),
        (3, 'd'), (4, 'p'), (5, 's'), (4, 'd'), (5, 'p'), (6, 's'),
        (4, 'f'), (5, 'd'), (6, 'p'), (7, 's'), (5, 'f'), (6, 'd'), (7, 'p')
    ]

    max_electrons = {'s': 2, 'p': 6, 'd': 10, 'f': 14}
    configuration = []

    for n, orbital_type in orbitals:
        capacity = max_electrons[orbital_type]
        if atomic_number >= capacity:
            configuration.append(f"{n}{orbital_type}{capacity}")
            atomic_number -= capacity
        else:
            if atomic_number > 0:
                configuration.append(f"{n}{orbital_type}{atomic_number}")
                atomic_number = 0
            break

    return ' '.join(configuration)

# Programme principal
if __name__ == "__main__":
    print("=== Configuration électronique des éléments ===")
    numero_atomique = int(input("Entrez le numéro atomique de l'élément : "))
    config = configuration_electronique(numero_atomique)
    print(f"Configuration électronique : {config}")
