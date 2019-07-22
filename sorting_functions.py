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


def swap(A, i, j):
    """Helper function to swap elements i and j of list A."""
    print(" # TODO # ")
    yield A


def insertionsort(get_distance_from_grenoble):
    """In-place insertion sort."""
    for city in len(tableau):
        temp = tableau[city]
        j = city
        while j>0 and temp< tableau[j-1]:

    print(" # TODO # ")
    yield A


def bubblesort(A, *args, **kwargs):
    """In-place bubble sort."""
    print(" # TODO # ")
    yield A


def selectionsort(A, *args, **kwargs):
    """In-place selection sort."""
    print(" # TODO # ")
    yield A


def mergesort(A, start, end):
    """Merge sort."""
    print(" # TODO # ")
    yield A


def quicksort(A, start, end):
    """In-place quicksort."""
    print(" # TODO # ")
    yield A


def shellsort(A, *args, **kwargs):
    "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
    print(" # TODO # ")
    yield A


def heapsort(A, *args, **kwargs):
    """Heap sort"""
    print(" # TODO # ")
    yield A

    
if __name__ == "__main__":
    test_data = [8, 5, 9, 34, 22, 12, 4, 2]

    # for a in insertionsort(test_data):
    #     print(a)

    # for a in shellsort(test_data):
    #     print(a)
