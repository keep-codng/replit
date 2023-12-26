import turtle
 
t = turtle.Turtle()
t.pensize(4)
 
# face
t.circle(100)
 
# eyes
t.up()
t.goto(-35, 120)
t.dot(25)
t.goto(35, 120)
t.dot(25)
 
# nose
t.goto(0, 80)
t.dot(25)
 
# mouth
t.down()
t.goto(40, 60)
t.goto(0, 40)
t.goto(-40, 60)