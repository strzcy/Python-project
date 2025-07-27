import turtle

t = turtle.Turtle()
t.shape('turtle')
t.shapesize(1)
t.color('green')

def maju():
    t.forward(10)

def kiri():
    t.left(5)

def kanan():
    t.right(5)
    
turtle.listen()
turtle.onkeypress(maju, 'w')
turtle.onkeypress(kiri, 'a')
turtle.onkeypress(kanan, 'd')

turtle.done()
