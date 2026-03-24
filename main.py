from time import sleep
from turtle import *

t=Turtle()
t.speed(100)
t.hideturtle()

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

#ITALIA

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

sleep(2)
t.clear()

#IEMEN DO SUL

#faixa vermelha

t.pu()
t.goto(-150, 33)
t.pd()
t.color("red")
t.begin_fill()
for _ in range(2):
    t.forward(300)
    t.left(90)
    t.forward(67)
    t.left(90)
t.end_fill()

#faixa branca

t.pu()
t.goto(-150, -34)
t.pd()
t.color("black", "white")
t.begin_fill()
for _ in range(2):
    t.forward(300)
    t.left(90)
    t.forward(67)
    t.left(90)
t.end_fill()

#faixa preta

t.pu()
t.goto(-150, -100)
t.pd()
t.color("black")
t.begin_fill()
for _ in range(2):
    t.forward(300)
    t.left(90)
    t.forward(67)
    t.left(90)
t.end_fill()

# triangulo azul 

t.pu()
t.goto(-150, -100)
t.pd()
t.color("skyblue")
t.begin_fill()
t.goto(-50, 0)
t.goto(-150, 100)
t.goto(-150, -100)
t.end_fill()

#estrela vermelha

t.pu()
t.goto(-125, 20)
t.pd()
t.color("red")
t.right(20)
t.begin_fill()

for _ in range(5):
    t.forward(45)
    t.right(144)

t.end_fill()

sleep(2)
t.clear()

#SUDAO

t.left(20)

#parte vermelha

t.pu()
t.goto(-100, 36.6)
t.pd()
t.color("red")
t.begin_fill()
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(43.3)
    t.left(90)
t.end_fill()

#parte branca

t.pu()
t.goto(-100, -6.7)
t.pd()
t.color("black", "white")
t.begin_fill()
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(43.3)
    t.left(90)
t.end_fill()

#parte preta

t.pu()
t.goto(-100, -50)
t.pd()
t.color("black")
t.begin_fill()
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(43.3)
    t.left(90)
t.end_fill()

#triangulo verde

t.pu()
t.goto(-100, -50)
t.pd()
t.color("green")
t.begin_fill()
t.goto(-30, 15)      
t.goto(-100, 80)     
t.goto(-100, -50)    
t.end_fill()

sleep(2)
t.clear()

#CHILE

#parte vermelha 

t.pu()
t.goto(-100, -50)
t.pd()
t.color("red")
t.begin_fill()
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(65)
    t.left(90)
t.end_fill()

#parte branca 

t.pu()
t.goto(0, 15)
t.pd()
t.color("black", "white")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(65)
    t.left(90)
t.end_fill()

#quadrado azul 

t.pu()
t.goto(-100, 15)
t.pd()
t.color("blue")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(65)
    t.left(90)
t.end_fill()

#estrela branca 

t.pu()
t.goto(-65, 50) 
t.pd()
t.color("white")
t.begin_fill()
for _ in range(5):
    t.forward(30)
    t.right(144)
t.end_fill()

sleep(2)
t.clear()

#PANAMA

#quadrante azul 
t.pu()
t.goto(-100, -50)
t.pd()
t.color("navy")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(65)
    t.left(90)
t.end_fill()

#quadrante vermelho
t.pu()
t.goto(0, 15)
t.pd()
t.color("red")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(65)
    t.left(90)
t.end_fill()

#quadrante branco cima 
t.pu()
t.goto(-100, 15)
t.pd()
t.color("black", "white")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(65)
    t.left(90)
t.end_fill()

#estrela azul
t.pu()
t.goto(-65, 50)
t.pd()
t.color("navy")
t.begin_fill()
for _ in range(5):
    t.forward(30)
    t.right(144)
t.end_fill()

#quadrante branco baixo 

t.pu()
t.goto(0, -50)
t.pd()
t.color("black", "white")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(65)
    t.left(90)
t.end_fill()

#estrela vermelha

t.pu()
t.goto(35, -12)
t.pd()
t.color("red")
t.begin_fill()
for _ in range(5):
    t.forward(30)
    t.right(144)
t.end_fill()

sleep(2)
t.clear()

#JORDANIA

#parte preta

t.pu()
t.goto(-100, 36.6)
t.pd()
t.color("black")
t.begin_fill()
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(43.3)
    t.left(90)
t.end_fill()

#parte branca 

t.pu()
t.goto(-100, -6.7)
t.pd()
t.color("black", "white")
t.begin_fill()
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(43.3)
    t.left(90)
t.end_fill()

#parte verde

t.pu()
t.goto(-100, -50)
t.pd()
t.color("green")
t.begin_fill()
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(43.3)
    t.left(90)
t.end_fill()

#triangulo vermelho

t.pu()
t.goto(-100, -50)
t.pd()
t.color("red")
t.begin_fill()
t.goto(-30, 15)      
t.goto(-100, 80)     
t.goto(-100, -50)    
t.end_fill()

#estrela branca de 7 pontas

t.pu()
t.goto(-82, 12)      
t.pd()
t.color("white")
t.begin_fill()


for _ in range(7):
    t.forward(18)
    t.right(154.2)
    
t.end_fill()

sleep(2)
t.clear()

#PAQUISTAO

#parte branca vertical

t.pu()
t.goto(-100, -50)
t.pd()
t.color("black", "white")
t.begin_fill()
for _ in range(2):
    t.forward(50)
    t.left(90)
    t.forward(130)
    t.left(90)
t.end_fill()

#parte verde 

t.pu()
t.goto(-50, -50)
t.pd()
t.color("darkgreen")
t.begin_fill()
for _ in range(2):
    t.forward(150)
    t.left(90)
    t.forward(130)
    t.left(90)
t.end_fill()

#lua crescente branca 

t.pu()
t.goto(15, -15)      
t.pd()
t.color("white")
t.begin_fill()
t.circle(35)         
t.end_fill()

#circulo verde 
t.pu()
t.goto(25, -5)       
t.pd()
t.color("darkgreen")
t.begin_fill()
t.circle(35)
t.end_fill()

#estrela branca inclinada
t.pu()
t.goto(35, 50)       
t.pd()
t.color("white")

# inclinando a estrela para a direita

t.right(30) 

t.begin_fill()

for _ in range(5):
    t.forward(20)
    t.right(144)

t.end_fill()

sleep(2)

t.clear()

#ESTADOS UNIDOS

t.left(30)


t.pu()
t.goto(-100, 80)
t.pd()
t.color("red")
t.begin_fill()
t.goto(100, 80)   
t.goto(100, -50)  
t.goto(-100, -50) 
t.goto(-100, 80)  
t.end_fill()

# 2. LISTRAS BRANCAS

t.pu()
t.goto(-20, 70)
t.pd()
t.color("white")
t.begin_fill()
t.goto(100, 70)
t.goto(100, 60)
t.goto(-20, 60)
t.goto(-20, 70)
t.end_fill()

# Listra 4 
t.pu()
t.goto(-20, 50)
t.pd()
t.begin_fill()
t.goto(100, 50)
t.goto(100, 40)
t.goto(-20, 40)
t.goto(-20, 50)
t.end_fill()

# Listra 6 
t.pu()
t.goto(-20, 30)
t.pd()
t.begin_fill()
t.goto(100, 30)
t.goto(100, 20)
t.goto(-20, 20)
t.goto(-20, 30)
t.end_fill()

# Listra 8 
t.pu()
t.goto(-100, 10)
t.pd()
t.begin_fill()
t.goto(100, 10)
t.goto(100, 0)
t.goto(-100, 0)
t.goto(-100, 10)
t.end_fill()

# Listra 10
t.pu()
t.goto(-100, -10)
t.pd()
t.begin_fill()
t.goto(100, -10)
t.goto(100, -20)
t.goto(-100, -20)
t.goto(-100, -10)
t.end_fill()

# Listra 12 
t.pu()
t.goto(-100, -30)
t.pd()
t.begin_fill()
t.goto(100, -30)
t.goto(100, -40)
t.goto(-100, -40)
t.goto(-100, -30)
t.end_fill()

# 3. canto azul
t.pu()
t.goto(-100, 80)
t.pd()
t.color("navy")
t.begin_fill()
t.goto(-20, 80)
t.goto(-20, 10)
t.goto(-100, 10)
t.goto(-100, 80)
t.end_fill()


# 4. ESTRELAS BRANCAS
t.color("white")

#  FILEIRA 1
t.pu()
t.goto(-92, 72)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-76, 72)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-60, 72)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-44, 72)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-28, 72)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

#  FILEIRA 2
t.pu()
t.goto(-92, 54)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-76, 54)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-60, 54)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-44, 54)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-28, 54)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

# FILEIRA 3 
t.pu()
t.goto(-92, 36)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-76, 36)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-60, 36)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-44, 36)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-28, 36)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

#  FILEIRA 4 
t.pu()
t.goto(-92, 18)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-76, 18)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-60, 18)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-44, 18)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

t.pu()
t.goto(-28, 18)
t.pd()
t.begin_fill()
for _ in range(5):
    t.forward(5)
    t.right(144)
t.end_fill()

sleep(2)
t.clear()

#COREIA DO NORTE

#  LISTRA AZUL SUPERIOR
t.pu()
t.goto(-150, 80)     
t.pd()
t.color("navy")
t.begin_fill()
t.goto(150, 80)      
t.goto(150, 50)      
t.goto(-150, 50)    
t.goto(-150, 80)     
t.end_fill()

#  LISTRA BRANCA SUPERIOR 
t.pu()
t.goto(-150, 50)
t.pd()
t.color("white")
t.begin_fill()
t.goto(150, 50)
t.goto(150, 40)
t.goto(-150, 40)
t.goto(-150, 50)
t.end_fill()

# LISTRA VERMELHA CENTRAL 
t.pu()
t.goto(-150, 40)
t.pd()
t.color("red")
t.begin_fill()
t.goto(150, 40)
t.goto(150, -40)
t.goto(-150, -40)
t.goto(-150, 40)
t.end_fill()

#  LISTRA BRANCA INFERIOR 
t.pu()
t.goto(-150, -40)
t.pd()
t.color("white")
t.begin_fill()
t.goto(150, -40)
t.goto(150, -50)
t.goto(-150, -50)
t.goto(-150, -40)
t.end_fill()

# LISTRA AZUL INFERIOR
t.pu()
t.goto(-150, -50)
t.pd()
t.color("navy")
t.begin_fill()
t.goto(150, -50)
t.goto(150, -80)
t.goto(-150, -80)
t.goto(-150, -50)
t.end_fill()



# CÍRCULO BRANCO 
t.pu()
t.goto(-50, -30)    
t.pd()
t.color("white")
t.begin_fill()
t.circle(30)         
t.end_fill()

# ESTRELA VERMELHA

t.pu()
t.goto(-75, 10)      
t.pd()
t.color("red")
t.begin_fill()
for _ in range(5):
    t.forward(50)    
    t.right(144)
t.end_fill()

sleep(2)

t.clear()

t.left(30)

#CANADA (DESAFIO)

# 1. RETÂNGULO VERMELHO DA ESQUERDA
t.pu()
t.goto(-200, 100)
t.pd()
t.color("red")
t.begin_fill()
t.goto(-100, 100)
t.goto(-100, -100)
t.goto(-200, -100)
t.goto(-200, 100)
t.end_fill()

# 2. RETÂNGULO VERMELHO DA DIREITA
t.pu()
t.goto(100, 100)
t.pd()
t.begin_fill()
t.goto(200, 100)
t.goto(200, -100)
t.goto(100, -100)
t.goto(100, 100)
t.end_fill()

# 3. QUADRADO BRANCO CENTRAL
t.pu()
t.goto(-100, 100)
t.pd()
t.color("white")
t.begin_fill()
t.goto(100, 100)
t.goto(100, -100)
t.goto(-100, -100)
t.goto(-100, 100)
t.end_fill()

# 4. FOLHA DE BORDO 
t.pu()
t.color("red")
t.goto(0, -30)
t.pd()
t.begin_fill()

# Lado esquerdo 
t.goto(-8, -20)
t.goto(-20, -40)
t.goto(-15, -15)
t.goto(-45, -10)
t.goto(-30, 10)
t.goto(-60, 20)
t.goto(-35, 30)
t.goto(-50, 55)
t.goto(-20, 45)
t.goto(-10, 70)

# topo
t.goto(0, 90)

# Lado direito (
t.goto(10, 70)
t.goto(20, 45)
t.goto(50, 55)
t.goto(35, 30)
t.goto(60, 20)
t.goto(30, 10)
t.goto(45, -10)
t.goto(15, -15)
t.goto(20, -40)
t.goto(8, -20)

# fechar
t.goto(0, -30)

t.end_fill()

mainloop()