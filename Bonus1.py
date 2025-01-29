def main():
    # Demander à l'utilisateur d'entrer une phrase
    phrase = input("Entrez une phrase : ")

    # Gérer une entrée vide
    if not phrase:
        # Si l'utilisateur n'entre pas de phrase, afficher un message et quitter la fonction
        print("Vous n'avez pas entré de phrase.")
        return

    # Calculer le nombre total de caractères (y compris les espaces)
    total_caracteres = len(phrase)  # Utilise la fonction len() pour obtenir la longueur de la chaîne

    # Découper la phrase en mots
    mots = phrase.split()  # Utilise les espaces pour séparer les mots et crée une liste de mots
    nombre_mots = len(mots)  # Compte le nombre de mots dans la liste

    # Identifier les voyelles
    voyelles = "aeiouyAEIOUY"  # Liste des voyelles en minuscules et majuscules
    nombre_voyelles = sum(1 for char in phrase if char in voyelles)  # Compte les voyelles dans la phrase

    # Afficher les résultats
    print(f"Nombre total de caractères (y compris les espaces) : {total_caracteres}")
    print(f"Nombre de mots : {nombre_mots}")
    print(f"Nombre de voyelles : {nombre_voyelles}")

if __name__ == "__main__":
    main()