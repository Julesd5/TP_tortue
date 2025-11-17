import turtle
t = turtle.Turtle()
t.speed(0) # maximum speed
s = turtle.getscreen()
def equilateral(longueur):
    """
    longueur(int) : longueur d'un coter du triangle
    Dessine un triangle equilateral de cote longueur
    """
    for _ in range(3):
        t.forward(longueur)
        t.right(180-60)
    

equilateral(100)
turtle.exitonclick()
