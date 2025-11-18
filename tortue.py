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

def polygone(longueur, nb_cotes, ajout = 0):
    """
    Args:
        longueur (str): longueur du polygone
        nb_cotes (str): nombres de cotes du polygone
        ajout    (str): ajoute "ajout" a chaque cote 
    """
    for _ in range(nb_cotes):
        longueur += ajout
        t.forward(longueur)
        t.right(360/nb_cotes)


turtle.exitonclick()
