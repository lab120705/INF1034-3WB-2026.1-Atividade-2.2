from time import sleep

from turtle import *

t=Turtle()

t.speed(100)

#RETANGULO

t.pu()
t.goto(-100, -50)
t.pd()

for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(130)
    t.left(90)

#JAPAO

#circulo vermelho

t.pu()
t.goto(0, -25)
t.pd()
t.color("red")
t.begin_fill()
t.circle(40)
t.end_fill()

sleep(2)
t.clear()


#parte vermelha

t.pu()
t.goto(50, -100)
t.pd()
t.color("red")
t.begin_fill()



for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)

t.end_fill()

#IALIA

#parte verde

t.pu()
t.goto(-150, -100)
t.pd()
t.color("green")
t.begin_fill()

for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)

t.end_fill()

#parte branca

t.pu()
t.goto(-50, -100)
t.pd()
t.color("black", "white")
t.begin_fill()

for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)

t.end_fill()


#IEMEN DO SUL

# triangulo azul

t.pu()
t.goto(-150, -100)
t.pd()
t.color("skyblue")
t.begin_fill()
t.goto(-50, 0)
t.goto(-150, -100)
t.goto(-150, 100)
t.end_fill()









t.end_fill()









mainloop()





