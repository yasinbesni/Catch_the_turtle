import turtle
import random

# Kaplumbağa ekranını ayarla
screen = turtle.Screen()
screen.title("Catch the Turtle")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Kaplumbağayı oluştur
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.speed(0)

# Skor değişkenini başlat
score = 0

# Kaplumbağa hareket fonksiyonu
def move_turtle():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    t.goto(x, y)
    screen.ontimer(move_turtle, random.randint(500, 1500))

# Kaplumbağayı tıklama fonksiyonu
def catch_turtle(x, y):
    global score
    score += 1
    print("Skor:", score)

# Kaplumbağayı tıklamaya duyarlı hale getir
t.onclick(catch_turtle)

# Kaplumbağayı hareket ettir
move_turtle()

# Oyun döngüsü
screen.mainloop()