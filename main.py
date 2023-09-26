import turtle
import random
import time

oyunSuresi = 20
score = 0
textFont = ('Arial', 12, 'normal')

drawing_screen = turtle.Screen()
drawing_screen.bgcolor("light yellow")
drawing_screen.title("Catch It Homework")
playerName = drawing_screen.textinput("Selam Oyuncu!", "Oyuncunun ismi:")
ekranGenislik = drawing_screen.window_width() / 2
ekranYukseklik = drawing_screen.window_height() / 2
ekranX = ekranGenislik * 0.9        # ekranın yüzde doksanını kullanmak anlamına geliyor
ekranY = ekranYukseklik * 0.9       # ekranın yüzde doksanını kullanmak anlamına geliyor


''' Oyuncuya görsel olarak konumu gösterecek obje  '''
drawing_instance = turtle.Turtle()
drawing_instance.color("green")
drawing_instance.resizemode("user")  # auto veya noresize olabilir
drawing_instance.shapesize(2, 2, 2)  # genişlik , uzunluk , outline
drawing_instance.shape("turtle")
drawing_instance.penup()

''' Oyuncunun gördüğü kaplumbağaya tıklayacağı obje '''
second_instance = turtle.Turtle()
#  second_instance.hideturtle()
second_instance.speed("fastest")
second_instance.penup()

''' Oyuncunun tıklamasından sonra görsel kaplumbağanın konumunu alıp tıklanan ile karşılaştıracak obje '''
third_instance = turtle.Turtle()
third_instance.color("green")
third_instance.resizemode("user")  # auto veya noresize olabilir
third_instance.shapesize(2, 2, 2)  # genişlik , uzunluk , outline
third_instance.shape("turtle")
third_instance.penup()
third_instance.hideturtle()

''' Ana Yazıları yazdıracak olan obje '''
writing_instance = turtle.Turtle()
writing_instance.color("black")
writing_instance.hideturtle()
writing_instance.penup()
writing_instance.setposition(-250, 260)
print(writing_instance.pos())
writing_instance.write("Kalan Süre:", True, align="right", font=textFont)
writing_instance.setposition(231, 260)
writing_instance.write("Skorun:", True, align="left", font=textFont)
print(writing_instance.pos())

''' Değişken yazıları yazdıracak olan obje '''
writing_instance_second = turtle.Turtle()
writing_instance_second.color("red")
writing_instance_second.hideturtle()
writing_instance_second.penup()
writing_instance_second.speed("fastest")


def gameMain():
    global oyunSuresi
    global score
    if oyunSuresi > 0:

        drawing_instance.hideturtle()

        randomx = random.randint(int(-ekranX), int(ekranX))
        randomy = random.randint(int(-ekranY), int(ekranY))
        drawing_instance.setposition(randomx, randomy)

        drawing_instance.showturtle()

        drawing_screen.listen()
        drawing_screen.onclick(second_instance.goto)

        time.sleep(0.2)

        third_instance.setposition(randomx, randomy)
        x = second_instance.distance(third_instance)
        if x < 30:
            score = score + 1
        print(drawing_instance.pos())
        print(second_instance.pos())
        print(x)
        print(score)

        time.sleep(0.1)
        oyunSuresi = oyunSuresi - 1
        writing_instance_second.clear()
        writing_instance_second.setposition(-230, 260)
        writing_instance_second.write(oyunSuresi, True, align="right", font=textFont)
        writing_instance_second.setposition(298, 260)
        writing_instance_second.write(score, True, align="right", font=textFont)

        drawing_screen.ontimer(gameMain, 500)

    else:
        print(f"Oyun bitti, Skorun {score}")
        drawing_screen.bye()


gameMain()

turtle.mainloop()
