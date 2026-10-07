"""Exercices Python : fonctions, listes, algorithmes et affichage."""


import random
from functools import wraps


def lo(value):
    """Calcule récursivement la somme de 1 à value."""
    if value == 1:
        return 1
    return value + lo(value - 1)


def test_bases():
    """Teste quelques fonctionnalités de base de Python."""
    print("---------- Bases Python ----------")

    result = lo(3)
    print("Somme récursive de 1 à 3 :", result)

    words = ["python", "is", "awesome"]
    print("-".join(words))

    word = "ami"
    print(word * 3)

    binary_value = int("11", 2)
    print("11 en base 2 :", binary_value)

    integer_value = int(8.9)
    print("Partie entière de 8.9 :", integer_value)

    numbers = [1, 2, 3, 4]
    print("Liste :", numbers)

    for index in range(3):
        print(index)


def test_parite():
    """Teste la parité d'un nombre."""
    print("---------- Parité ----------")

    number = 5

    if number % 2 == 0:
        print(f"Le nombre {number} est pair.")
    else:
        print(f"Le nombre {number} est impair.")


def cal(first_number, second_number, operator):
    """Effectue une opération arithmétique."""
    if operator == "+":
        return first_number + second_number

    if operator == "-":
        return first_number - second_number

    if operator == "*":
        return first_number * second_number

    if operator == "/":
        return first_number / second_number

    raise ValueError("Opérateur non reconnu.")


def test_calculatrice():
    """Teste la calculatrice."""
    print("---------- Calculatrice ----------")

    print(cal(2, 3, "+"))
    print(cal(2, 3, "-"))
    print(cal(2, 3, "*"))
    print(cal(2, 3, "/"))
    print(cal(6, 3, "/"))


def maxi(first_number, second_number, third_number):
    """Retourne le plus grand de trois nombres."""
    return max(first_number, second_number, third_number)


def test_maxi():
    """Teste la fonction maxi."""
    print("---------- Maximum ----------")

    print(maxi(1, 2, 3))
    print(maxi(-1, -2, -3))


def som(number):
    """Calcule la somme des nombres de 1 à number."""
    total = 0

    for current_number in range(number + 1):
        total += current_number

    return total


def test_somme():
    """Teste le calcul d'une somme."""
    print("---------- Somme ----------")

    print(som(3))
    print(som(10))


def mult(number):
    """Affiche la table de multiplication d'un nombre."""
    for multiplier in range(11):
        print(f"{multiplier} * {number} = {multiplier * number}")


def mult1(number):
    """Retourne la table de multiplication sous forme de liste."""
    result = []

    for multiplier in range(11):
        result.append(multiplier * number)

    return result


def mult2(number):
    """Retourne la table de multiplication avec une compréhension."""
    return [multiplier * number for multiplier in range(11)]


def test_multiplication():
    """Teste les différentes méthodes de multiplication."""
    print("---------- Tables de multiplication ----------")

    for number in range(11):
        print(f"Table de multiplication de {number}")
        mult(number)

    print(mult1(5))
    print(mult2(5))


def test_random():
    """Teste la génération d'un nombre aléatoire."""
    print("---------- Random ----------")

    target = 100
    random_number = random.randint(1, 100)

    print("La valeur de random est :", random_number)
    print("La valeur cible est :", target)

    if random_number == target:
        print("Vous avez gagné !")
    elif random_number > target:
        print("Le nombre généré est trop grand.")
    else:
        print("Le nombre généré est trop petit.")


def test_reverse():
    """Teste différentes méthodes pour inverser une chaîne."""
    print("---------- Inversion de chaîne ----------")

    word = "david raya"

    print("Méthode slicing :", word[::-1])

    reversed_word = ""

    for character in word:
        reversed_word = character + reversed_word

    print("Méthode boucle :", reversed_word)

    another_word = "salut rabah"
    reversed_iterator = reversed(another_word)

    print("Avec join :", "".join(reversed_iterator))


def test_join():
    """Teste différentes méthodes pour joindre des chaînes."""
    print("---------- Join ----------")

    words = ["python", "is", "fun"]
    result = ""

    for index, word in enumerate(words):
        result += word

        print(index, word)

        if index < len(words) - 1:
            result += " "

    print(result)

    print(" ".join(words))


def my_decorator(function):
    """Crée un décorateur affichant des messages avant et après une fonction."""

    @wraps(function)
    def wrapper():
        """Exécute la fonction décorée avec des messages."""
        print("Avant l'appel de la fonction.")
        result = function()
        print("Après l'appel de la fonction.")
        return result

    return wrapper


@my_decorator
def saluer():
    """Affiche un message de salutation."""
    print("Bonjour !")


def test_decorator():
    """Teste le décorateur."""
    print("---------- Décorateur ----------")
    saluer()


def compter_voyelles(word):
    """Compte le nombre de voyelles dans une chaîne."""
    vowels = "aeiouy"
    count = 0

    for character in word.lower():
        if character in vowels:
            count += 1

    return count


def test_voyelles():
    """Teste le comptage des voyelles."""
    print("---------- Voyelles ----------")

    word = "abcefgiuo"
    print(compter_voyelles(word))


def fact(number):
    """Calcule récursivement le factoriel d'un nombre."""
    if number == 0:
        return 1

    return number * fact(number - 1)


def test_factoriel():
    """Teste le calcul du factoriel."""
    print("---------- Factoriel ----------")
    print(fact(3))


def premier(number):
    """Vérifie si un nombre est premier."""
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def test_premier():
    """Teste la détection des nombres premiers."""
    print("---------- Nombre premier ----------")

    print(premier(5))
    print(premier(10))


def comp(sentence):
    """Compte le nombre de mots dans une chaîne."""
    words = sentence.split()
    return len(words)


def test_compteur_mots():
    """Teste le compteur de mots."""
    print("---------- Compteur de mots ----------")

    sentence = "bonjour dev, comment vas tu !"
    print(comp(sentence))


def jeu():
    """Lance une partie de pierre-papier-ciseaux."""
    choices = ["pierre", "papier", "ciseaux"]
    computer = random.choice(choices)

    player = input(
        "Choisis pierre, papier ou ciseaux : "
    ).lower()

    print("Ordinateur :", computer)

    winning_choices = {
        "pierre": "ciseaux",
        "papier": "pierre",
        "ciseaux": "papier",
    }

    if player not in choices:
        print("Choix invalide.")
    elif player == computer:
        print("Égalité.")
    elif winning_choices[player] == computer:
        print("Tu as gagné !")
    else:
        print("Tu as perdu !")


def som_des():
    """Affiche la somme de deux dés lancés aléatoirement."""
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    total = first_dice + second_dice

    print(f"Le dé 1 : {first_dice}")
    print(f"Le dé 2 : {second_dice}")
    print(f"Résultat des deux dés : {total}")


def tri(numbers):
    """Trie une liste avec l'algorithme de sélection."""
    size = len(numbers)

    for index in range(size):
        minimum_index = index

        for current_index in range(index + 1, size):
            if numbers[current_index] < numbers[minimum_index]:
                minimum_index = current_index

        numbers[index], numbers[minimum_index] = (
            numbers[minimum_index],
            numbers[index],
        )

    return numbers


def test_tri():
    """Teste le tri par sélection."""
    print("---------- Selection sort ----------")

    numbers = [3, 4, 2, 1, 3, 5, 6, 1, 1, 2, 4, 5, 3, 0]

    print("Liste triée :", tri(numbers))


def bubble(numbers):
    """Trie une liste avec l'algorithme Bubble Sort."""
    size = len(numbers)

    for pass_number in range(size - 1):
        swapped = False

        for index in range(size - 1 - pass_number):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = (
                    numbers[index + 1],
                    numbers[index],
                )
                swapped = True

        if not swapped:
            break

    return numbers


def test_bubble():
    """Teste le Bubble Sort."""
    print("---------- Bubble Sort ----------")

    numbers = [6, 5, 4, 2, 1, 4, 6, 8, 0, 1, 2, 4]

    print("Liste triée :", bubble(numbers))


def afficher_triangle_centre(size):
    """Affiche un triangle centré."""
    for row in range(1, size + 1):
        print(" " * (size - row), end="")

        for _ in range(row):
            print("*", end=" ")

        print()


def afficher_triangle_croissant(size):
    """Affiche un triangle croissant."""
    for row in range(1, size + 1):
        for _ in range(row):
            print("*", end=" ")

        print()


def afficher_triangle_decroissant(size):
    """Affiche un triangle décroissant."""
    for row in range(size, 0, -1):
        for _ in range(row):
            print("*", end=" ")

        print()


def afficher_diamant(size):
    """Affiche un diamant."""
    afficher_triangle_centre(size)

    for row in range(size - 1, 0, -1):
        print(" " * (size - row), end="")

        for _ in range(row):
            print("*", end=" ")

        print()


def afficher_triangle_nombres(size):
    """Affiche un triangle de nombres croissants."""
    for row in range(1, size + 1):
        for number in range(1, row + 1):
            print(number, end="")

        print()


def afficher_carre(size):
    """Affiche un carré avec uniquement les contours."""
    for row in range(size):
        for column in range(size):
            if (
                row == 0
                or row == size - 1
                or column == 0
                or column == size - 1
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()


def afficher_table_multiplication():
    """Affiche les tables de multiplication de 0 à 10."""
    for first_number in range(11):
        for second_number in range(1, 11):
            print(
                second_number,
                "*",
                first_number,
                "=",
                first_number * second_number,
                end=" | ",
            )

        print()


def afficher_triangle_decroissant_decale(size):
    """Affiche un triangle décroissant décalé."""
    for row in range(size, 0, -1):
        print("  " * (size - row), end="")

        for _ in range(row):
            print("*", end=" ")

        print()


def afficher_nombres_decroissants(size):
    """Affiche des nombres décroissants sur chaque ligne."""
    for row in range(size, 0, -1):
        for number in range(row, 0, -1):
            print(number, end=" ")

        print()


def afficher_diagonale(size):
    """Affiche une diagonale descendante."""
    for row in range(1, size):
        for column in range(1, size):
            if row == column:
                print(" " * (size - row), "*", end="")

        print()


def afficher_x(size):
    """Affiche un X avec des étoiles."""
    for row in range(size):
        for column in range(size):
            if row == column or row + column == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()


def afficher_compteur_triangle():
    """Affiche des nombres consécutifs dans un triangle."""
    number = 1

    for row in range(1, 5):
        for _ in range(row):
            print(number, end="")
            number += 1

        print()


def afficher_triangle_lignes():
    """Affiche le numéro de ligne plusieurs fois."""
    for row in range(1, 5):
        for _ in range(row):
            print(row, end="")

        print()


def test_affichages():
    """Exécute les différents exercices d'affichage."""
    print("---------- Affichages ----------")

    print("Triangle centré")
    afficher_triangle_centre(6)

    print("Triangle croissant")
    afficher_triangle_croissant(6)

    print("Triangle décroissant")
    afficher_triangle_decroissant(6)

    print("Diamant")
    afficher_diamant(6)

    print("Triangle de nombres")
    afficher_triangle_nombres(6)

    print("Carré")
    afficher_carre(6)

    print("Tables de multiplication")
    afficher_table_multiplication()

    print("Triangle décroissant décalé")
    afficher_triangle_decroissant_decale(6)

    print("Nombres décroissants")
    afficher_nombres_decroissants(5)

    print("Diagonale")
    afficher_diagonale(6)

    print("X")
    afficher_x(5)

    print("Compteur")
    afficher_compteur_triangle()

    print("Triangle par ligne")
    afficher_triangle_lignes()


def main():
    """Lance les différents exercices Python."""
    test_bases()
    test_parite()
    test_calculatrice()
    test_maxi()
    test_somme()
    test_multiplication()
    test_random()
    test_reverse()
    test_join()
    test_decorator()
    test_voyelles()
    test_factoriel()
    test_premier()
    test_compteur_mots()
    som_des()
    test_tri()
    test_bubble()
    test_affichages()
    


if __name__ == "__main__":
    main()
