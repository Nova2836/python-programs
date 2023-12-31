import turtle
 
sc = turtle.Screen()
sc.title("Smooth Movement Test")
sc.bgcolor("black")
sc.setup(width=800, height=800)

obj = turtle.Turtle()
obj.shape("triangle")
obj.color("white")
obj.penup()
obj.speed(0)

txt = turtle.Turtle()
txt.color("white")
txt.hideturtle()

sc.listen()

i = 0
k = 0
j = 0
l = 0


#_______________________________W
def w1():
    if l == 0 and j == 0:
        while obj.heading() != 90:
            obj.setheading(90)
            if obj.heading() == 90:
                break
        global i
        i += 1
        if i == 2:
            i -= 1
        elif i == 3:
            i -= 2
        if i > 0:
            while i != 0:
                obj.forward(1)
                if i == 0:
                    break
    elif l >= 1:
        while obj.heading() != 45:
            obj.setheading(45)
            if obj.heading() == 45:
                break
    elif j >= 1:
        while obj.heading() != 135:
            obj.setheading(135)
            if obj.heading() == 135:
                break
def w2():
    if l == 0 and j == 0:
        global i
        i -= i
    elif l >= 1:
        obj.setheading(0)
    elif j >= 1:
        obj.setheading(180)
#_______________________________S
def s1():
    if l == 0 and j == 0:
        while obj.heading() != 270:
                obj.setheading(270)
                if obj.heading() == 270:
                    break
        global k
        k += 1
        if k == 2:
            k -= 1
        elif k == 3:
            k -= 2
        if k > 0:
            while k != 0:
                obj.forward(1)
                if k == 0:
                    break
    elif l >= 1:
        while obj.heading() != 315:
            obj.setheading(315)
            if obj.heading() == 315:
                break
    elif j >= 1:
        while obj.heading() != 225:
            obj.setheading(225)
            if obj.heading() == 225:
                break
def s2():
    if l == 0 and j == 0:
        global k
        k -= k
    elif l >= 1:
        obj.setheading(0)
    elif j >= 1:
        obj.setheading(180)
#_______________________________A
def a1():
    if i == 0 and k == 0:
        while obj.heading() != 180:
                obj.setheading(180)
                if obj.heading() == 180:
                    break
        global j
        j += 1
        if j == 2:
            j -= 1
        elif j == 3:
            j -= 2
        if j > 0:
            while j != 0:
                obj.forward(1)
                if j == 0:
                    break
    elif i >= 1:
        while obj.heading() != 135:
            obj.setheading(135)
            if obj.heading() == 135:
                break
    elif k >= 1:
        while obj.heading() != 225:
            obj.setheading(225)
            if obj.heading() == 225:
                break
def a2():
    if i == 0:
        global j
        j -= j
    elif i >= 1:
        obj.setheading(90)
    elif k >= 1:
        obj.setheading(270)
#_______________________________D

def d1():
    if i == 0 and k == 0:
        while obj.heading() != 0:
            obj.setheading(0)
            if obj.heading() == 0:
                break
        global l
        l += 1
        if l == 2:
            l -= 1
        elif l == 3:
            l -= 2
        if l > 0:
            while l != 0:
                obj.forward(1)
                if l == 0:
                    break
    elif i >= 1:
        while obj.heading() != 45:
            obj.setheading(45)
            if obj.heading() == 45:
                break
    elif k >= 1:
        while obj.heading() != 315:
            obj.setheading(315)
            if obj.heading() == 315:
                break
def d2():
    if i == 0:
        global l
        l -= l
    elif i >= 1:
        obj.setheading(90)
    elif k >= 1:
        obj.setheading(270)
#________________

sc.onkeypress(w1, "w")
sc.onkey(w2, "w")

sc.onkeypress(s1, "s")
sc.onkey(s2, "s")

sc.onkeypress(a1, "a")
sc.onkey(a2, "a")

sc.onkeypress(d1, "d")
sc.onkey(d2, "d")


turtle.done()