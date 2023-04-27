import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(5)            # increase pensize (takes integer)
t.pencolor("blue")     # set pencolor (takes string)
t.shape("turtle")

for i in (1,2,3):
    t.forward(200)
    t.left(120)
    
t.left(180)

for i in (1,2,3,4):
    t.forward(175)
    t.right(90)





# end commands
win.mainloop()             # Wait for user to close window
