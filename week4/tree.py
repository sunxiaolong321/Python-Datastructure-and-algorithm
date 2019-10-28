#-*- coding:utf-8 -*
import turtle

def tree(t, n):
    if n > 5:
        t.forward(n)
        t.left(20)
        tree(t, n-5)
        t.right(40)
        tree(t, n-5)
        t.left(20)
        t.backward(n)

if __name__ == "__main__":
    t = turtle.Turtle()
    t.penup()
    t.right(90)
    t.fd(100)
    t.right(180)
    t.pendown()
    tree(t, 50)
    turtle.done()
