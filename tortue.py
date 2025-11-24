import turtle
t = turtle.Turtle()
t.speed(0) # maximum speed
s = turtle.getscreen()
def equilateral(longueur):
    """
    longueur(int) : longueur d'un coter du triangle
    Dessine un triangle equilateral de cote longueur
    """
    polygone(longueur, 3)

def carre(longueur):
    """
    longueur(int) : longueur d'un coter du carre
    Dessine un carre de cote longueur
    """
    polygone(longueur, 4)

def polygone(longueur, nb_cotes, ajout = 0, deviation = 0):
    """
    Args:
        longueur (str): longueur du polygone
        nb_cotes (str): nombres de cotes du polygone
        ajout    (str): ajoute "ajout" a chaque cote 
        deviation(str): ajoute "deviation" a chaque angle
    """
    total_dev = 0
    for _ in range(nb_cotes):
        longueur += ajout
        t.forward(longueur)
        t.right(360/nb_cotes + total_dev)
        total_dev += deviation

def figure1():
    longueur = 5
    for n in range(100):
        polygone(longueur, 4, ajout=1, deviation=1)
        longueur += 4
def figure2(longueur):
    for _ in range(200):
        polygone(longueur,4,1,1)
        longueur = longueur + 4

figure2(5)
turtle.exitonclick()
