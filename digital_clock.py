# Import modules needed
import turtle
import time

#Creating the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width = 500, height = 250)
wn.tracer(0)
wn.title("An Analogue Clock by TokyoEdTech")

#Create a pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(100)

def draw_clock(h, m, pen):
# Place the hour value
    pen.penup()
    pen.color("lightgreen")
    pen.goto(-170,-160)
    pen.setheading(90)
    pen.fd(140)
    pen.write(h, move= False, align = "center", font = ("Ariel", 50, "bold"))

# Place the min value
    pen.penup()
    pen.color("yellow")
    pen.goto( 0,-160)
    pen.setheading(90)
    pen.fd(140)
    pen.write(m, move= False, align = "center", font = ("Ariel", 50, "bold"))

    # Place the : separator
    pen.penup()
    pen.color("white")
    pen.goto( -75,-160)
    pen.setheading(90)
    pen.fd(140)
    pen.write(":", move= False, align = "center", font = ("Ariel", 50, "bold"))

    h = h + 12
    if (h >= 0 and h <= 12):
      x = "AM"
    else:
      x = "PM"
 
     # Place the AM/PM indicator
    pen.penup()
    pen.color("red")
    pen.goto( 150,-160)
    pen.setheading(90)
    pen.fd(140)
    pen.write(x, move= False, align = "center", font = ("Ariel", 50, "bold"))

 
# Getting time values
while True:
  h = int(time.strftime("%I"))
  h = h + 5 # to correct for time zone
  m = int(time.strftime("%M"))

# Add the hands as per actual time
  draw_clock(h, m, pen)
  wn.update()
  time.sleep(10)
  pen.clear()



wn.mainloop()
