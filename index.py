import turtle
import functions as func

t = turtle.Pen()


def shape(length, angle, times):
    for i in range(times):
        t.forward(length)
        t.left(angle)

shape(150, 133, 105)


func.pause() 