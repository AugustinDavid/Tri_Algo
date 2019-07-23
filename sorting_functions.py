import math
from haversine import haversine



def get_distance_from_grenoble(city):
    """Retourne la distance entre la ville passée en paramètre et Grenoble

    Args:
        city (dict): Dictionnaire issu du csv. Contient les clés "latitude" et "longitude"

    Returns:
        int: la distance en km
    """
    grenoble_lat = 45.166667
    grenoble_long = 5.716667
    latitude = city["latitude"]
    longitude = city["longitude"]

    # On met en tuples pour pouvoir utiliser avec haversine
    grenoble = (grenoble_lat, grenoble_long)
    city = (float(latitude), float(longitude))

    dist_en_km = haversine(grenoble, city)

    print(latitude, longitude)

    return dist_en_km


def swap(liste, i, j):
    """Helper function to swap elements i and j of list A."""

    print(" # TODO # ")
    yield liste


def insertionsort(A,*args, **kwargs):
    """In-place insertion sort."""
    for j in range(len(A)):
        temp = A[j]
        i = j-1
        while i >= 0 and A[i] > temp:# i>= ne pas oublié le = sinon ne traite pas la première occurence
            A[i+1] = A[i]
            i = i-1
        A[i+1] = temp

        yield A




def bubblesort(A, *args, **kwargs):
    """In-place bubble sort."""

    n = len(A)# on crée une variable qui stocke la longueur du tab a traité

    for i in range(n): # on parcours tout le tableau

        for j in range(0, n-1):# fonction range a 3 paramètres( start, stop, pas dans la liste), là il y a start et stop

    #traitement de l'index en cours et de celui qu'on rencontre

            if A[j] > A[j+1]:# Si l'index en cours est plus grand que celui qu'on recontre
                temp = A[j]
                A[j] = A[j+1]
                A[j + 1] = temp
                yield A



def selectionsort(A, *args, **kwargs):
    """In-place selection sort."""
    n = len(A)

    for i in range(n):# Première boucle pour parcourir le tableau

        temp_min= i # stockage de  i en temporaire pour la verif

        for j in range(i+1,n):# on commence a boucler a i+1 jusqu'à la fin du tableau
            if A[temp_min] > A[j]:
                temp_min = j

        temp = A[i]
        A[i] = A[temp_min]
        A[temp_min] = temp

        yield A



#def mergesort(A, start, end):
def mergesort(A, *args, **kwargs):
    """Merge sort."""

   # On teste si le tableau est égal a 1
    if len(A) == 1:
        return A

    #on coupe le tableau A en deux en se servant de sa longueur
    tab_1 = A[:int((len(A)/2))]
    tab_2 = A[int((len(A)/2)):]

    #on applique la fonction mergesort de façon récursive ce qui permet de découper les tableau pour pouvoir ensuite appliquer le tri
    tab_1 = mergesort(tab_1)
    tab_2 = mergesort(tab_2)


    return merge(tab_1, tab_2)



#Fonction qui tri les tableaux, le mieux est de commencer par celle ci dans le tri par fusion pour voir le résultat dans la fonction mergesort
def merge(tab_A, tab_B):
    C = []

    while tab_A != [] and tab_B != []:#tant que A et B ne sont pas vide
        #Si A est sup a B on ajoute b a la fin de la liste C sinon ce sera A
        if tab_A[0] > tab_B[0]:

            C.append(tab_B[0])
            tab_B.pop(0)
        else:
            C.append(tab_A[0])
            tab_A.pop(0)
    #il faut créer deux while dans le cas où l'un des 2 tableaux serait vide ce qui bloquerai le 1er while
    while tab_A != []:
        C.append(tab_A[0])
        tab_A.pop(0)
    while tab_B != []:
        C.append(tab_B[0])
        tab_B.pop(0)

    return C



#def quicksort(A, start, end):
def quicksort(A, *args, **kwargs):
    """In-place quicksort."""
    tour = 1

    if A == []:
        return []

    else:
        pivot = A[0]
        print(pivot)
        A1 = []
        A2 = []
        for element in A[1:]:
            if element < pivot:
                A1.append(element)
                print(A1)
            else:
                A2.append(element)
                print(A2)
        tour += 1
        return quicksort(A1) + [pivot] + quicksort(A2)




def shellsort(A, *args, **kwargs):#tri shellsort : www.geeksforgeeks
    "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
    n = len(A)

    gap = int(n/2)# faire un gap de la longueur divisé par 2

    # Application du tri par insertion en utilisant le gap pour trouver les chiffres à comparer
    while gap > 0:

        for j in range(gap, n):# Boucler sur n de  nombre de gap
            temp = A[j]
            i = j
            while i >= gap and A[i-gap] > temp:  # i>= ne pas oublié le = sinon ne traite pas la première occurence
                A[i] = A[i-gap]
                i -= gap
            A[i] = temp
        gap -= 1
        yield A


def heapsort(A, *args, **kwargs):
    """Heap sort"""
    print(" # TODO # ")
    yield A

    
if __name__ == "__main__":
    test_data = [8, 5, 9, 34, 22, 12, 4, 2]


    for a in quicksort(test_data):
        print(a)

    # for a in shellsort(test_data):
    #     print(a)
