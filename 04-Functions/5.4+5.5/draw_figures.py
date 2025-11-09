import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

side_length = 200
figures.draw_square(side_length)
figures.draw_triangle(100 )
figures.draw_rectangle(70,35)
window.mainloop()