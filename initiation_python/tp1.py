"""Exercices d'apprentissage Python : variables, listes, dictionnaires et fonctions."""

import time

import numpy as np


def count_up():
    """Génère les nombres 1 et 2."""
    yield 1
    yield 2


def fibo(n):
    """Calcule le n-ième nombre de Fibonacci."""
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


def fact(n):
    """Calcule le factoriel de n."""
    if n == 0:
        return 1
    return n * fact(n - 1)


def modif_valeur(a):
    """Modifie localement la valeur de a."""
    a = 10
    print(a)


def asy(s):
    """Compte le nombre de voyelles dans une chaîne."""
    return sum(1 for char in s if char.lower() in "oueyia")


def somm(a, b):
    """Calcule le PGCD de deux nombres avec l'algorithme d'Euclide."""
    while b != 0:
        a, b = b, a % b
    return a


def main():
    """Exécute les différents exercices Python."""

    print("Lancer mon premier programme Python")
    print("Bonjour")  # Python affiche Bonjour à l'écran.

    # Utilisation des variables
    nom = "rabs"
    print(nom)

    # Concaténer des chaînes
    print("bonjour " + nom + "!")

    # Opérations sur les nombres
    age = 31
    print(type(age))
    print("vous avez :", age, "ans")
    print("vous avez :", age + 1, "ans")

    # Gestion des exceptions
    charr = "33"

    try:
        age_prochain = int(charr) + 1
        print(age_prochain)
    except ValueError:
        print("erreur")

    # Les listes
    print("des opérations sur les listes")

    li = [10, 20, 30, 40, 50]
    print(li[0])
    print(li[-1])
    print(li[1:3])
    print(li[:3])
    print(li[2:])

    li2 = ["pomme", "banane", "cerise"]
    print(li2)

    li2.append("pasteque")
    print(li2)

    li2.insert(1, "ananas")
    print(li2)

    li2.extend(["dates", "oignons"])
    print(li2)

    li2.remove("dates")
    print(li2)

    li2.pop()
    print(li2)

    print(li2)

    li2.reverse()
    print(li2)

    # Les matrices
    print("des opérations sur les matrices")

    matrix = [
        [5, 4, 3],
        [3, 4, 5],
        [1, 2, 3],
    ]

    print(matrix[1][2])
    print("affichage de la matrice")

    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()

    print("un autre affichage :")

    for row in matrix:
        print(row)

    lig = len(matrix)
    print(lig)

    colonnes = len(matrix[0])
    print(colonnes)

    # NumPy
    print("import de la bibliothèque NumPy")

    array_a = np.array([[1, 2], [3, 4]])
    array_b = np.array([[5, 6], [7, 8]])

    print(array_a + array_b)
    print(array_a - array_b)
    print(array_a * 2)
    print(array_a.dot(array_b))
    print(array_a.T)

    # Opérations sur les ensembles
    print({1, 2, 3} & {2, 3, 4})
    print({1, 2, 3} or {2, 3, 4})

    # Boucles
    for number in range(1, 4):
        print(number, end="\n")

    nums = [1, 2, 3, 4]
    result = list(map(lambda x: x * 2, nums))
    print(result)

    li = ["python is fun"]
    si = "java is not"

    print(" ".join(li))
    print(si.split(" "))

    for number in range(1, 4):
        print(number)

    for number in range(1, 4):
        print(number, end=" ")

    print("")

    for number in range(1, 4):
        print(number, end="\n")

    # Barre de progression
    for _ in range(5):
        print(".", end="")
        time.sleep(0.5)

    print()

    # Copie de listes
    x = [1, 2, 3]
    y = x
    c = x.copy()

    y += [4]

    print(x)
    print(y)
    print(c)

    # Sort
    x = [3, 1, 2, 1]
    y = sorted(x)

    print(y)
    print(x)

    names = ["rabah", "anis"]
    ages = [31, 32]

    print(list(zip(names, ages)))

    # Générateur
    generator = count_up()
    print(next(generator))
    print(next(generator))

    # Manipulation dictionnaire
    dictionary = {"x": 10, "y": 20, "z": 30}

    dictionary["y"] = dictionary["z"]

    print("affichage après l'affectation")
    print(dictionary)

    del dictionary["x"]

    print("affichage après la suppression de x")

    dictionary["z"] = dictionary["y"] + 5

    print(dictionary)

    # Fibonacci
    for number in range(8):
        print(f"Fibonacci({number}) =", fibo(number))

    # Factorielle
    for number in range(7):
        print(f"Factorielle({number}) =", fact(number))

    # Range
    values = range(0, 4)
    print(values)
    print(list(values))

    # Utilisation de _
    for _ in range(7):
        print("hello")

    for number in range(7):
        print(number, "ok")

    first, *_ = [1, 2, 3, 4]
    print(first)

    data = [(1, "A"), (2, "B"), (3, "C")]

    for _, letter in data:
        print(letter)

    for number, letter in data:
        print(number, letter)

    # Les tuples
    tup = ("rabah", "anis", "mohamed", "bilal")

    for index, value in enumerate(tup):
        print(index, value)

    test = 5
    print(test)

    modif_valeur(test)

    print(test)

    # Afficher le byte d'un caractère
    byte_string = b"ABC"
    print(byte_string[0])

    # Dictionnaire avec des clés équivalentes
    dictionary = {}
    dictionary[1] = "A"
    dictionary[True] = "B"
    dictionary[1.0] = "C"

    print(dictionary)
    print(len(dictionary))

    # Copie de listes
    list_a = [1, 2]
    list_b = list_a * 2

    list_b[0] = 99

    print("a", list_a)
    print("b", list_b)

    # Conversion en liste
    depuis_string = list("Python")
    print(depuis_string)

    depuis_tuple = list((1, 2, 3))
    print(depuis_tuple)

    # Pop
    list_values = [0, 3, 1, 4, 1, 5, 9, 2, 6]

    last_value = list_values.pop()
    first_value = list_values.pop(0)

    print(first_value)
    print(list_values)
    print(last_value)

    nums = [3, 1, 4, 1, 5, 9]

    print(len(nums))
    print(sum(nums))
    print(min(nums), max(nums))
    print(sorted(nums))
    print(list(reversed(nums)))

    # Map et filter
    squared = list(map(lambda x: x**2, nums))
    print(squared)

    filtered = list(filter(lambda x: x > 3, nums))
    print(filtered)

    booleans = list(map(lambda x: x > 3, nums))
    print(booleans)

    # Listes
    list_a = [1, 2]
    list_b = [3, 4, 5]

    list_c = list_b * 2

    print(list_c)
    print(list_a + list_b)

    # Tuples
    tuple_values = (1, 2, 3)
    tuple_values = tuple_values + (4,)

    print(tuple_values)

    tuple_values = tuple_values * 2

    print("t*2:")
    print(tuple_values)

    tuple_values = tuple_values[:5]
    print(tuple_values)

    # Continue
    for number in range(1, 6):
        if number == 3:
            continue
        print(number)

    value_a = "4"
    value_b = "5"

    value_c = value_a * int(value_b)

    print(value_c)

    # Dictionnaires
    dictionary = {
        "nom": "Alice",
        "age": 30,
        "ville": "Paris",
    }

    value = dictionary.pop("xyz", "défaut")
    print(value)

    del dictionary["ville"]
    print(dictionary)

    value = dictionary.pop("age")
    print(value)

    dictionary = {"a": 1, "b": 2, "c": 3}

    keys = list(dictionary.keys())
    print(keys)

    # Tuple contenant une liste
    tuple_values = ([1, 2], "x")
    tuple_values[0].append(3)

    print(tuple_values)

    tuple_values = (1, 2, 3, 2, 4, 2)

    print(tuple_values.count(2))
    print(tuple_values.index(3))
    print(tuple_values.index(2, 2))

    # Pop
    list_values = [3, 1, 4, 1, 5, 9, 2, 6]

    first_value = list_values.pop(0)

    print(first_value)
    print(list_values)

    # Compréhension de liste
    print([
        (x, y)
        for x in range(3)
        for y in range(3)
    ])

    # Trouver les paires dont la somme vaut 6
    list_values = [1, 2, 3, 4, 5]
    target = 6
    pairs = []

    for index, value_a in enumerate(list_values):
        for value_b in list_values[index + 1:]:
            if value_a + value_b == target:
                pairs.append((value_a, value_b))

    print(pairs)

    # Comparaison de listes
    list_a = [1, 2]
    list_b = [1, 2]

    print(list_a == list_b, list_a in [list_b])

    # Attention : les lignes suivantes créent des références vers
    # la même liste.
    matrix = [[0] * 3 for _ in range(3)]
    matrix[0][0] = 1

    print(matrix[0])

    # Opérations sur les ensembles
    list_a = [1, 2, 3, 4]
    list_b = [3, 4, 5, 6]

    common = list(set(list_a) & set(list_b))
    only_a = list(set(list_a) - set(list_b))
    union = list(set(list_a) | set(list_b))
    symmetric_difference = list(set(list_a) ^ set(list_b))

    print(common)
    print(only_a)
    print(union)
    print(symmetric_difference)

    # Voyelles
    print(asy("audiu"))

    # PGCD
    print(somm(48, 18))


if __name__ == "__main__":
    main()