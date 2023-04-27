import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(10)            # increase pensize (takes integer)
t.pencolor("blue")     # set pencolor (takes string)
t.shape("turtle")

t.left(180)
t.penup()
t.forward(50)
t.right(90)
t.forward(200)
t.left(90)
t.pendown()
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)

t.right(180)
t.penup()
t.forward(250)
t.pendown()
t.forward(200)
t.left(90)
t.forward(400)
t.left(180)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)


# end commands
win.mainloop()             # Wait for user to close window
