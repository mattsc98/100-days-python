import turtle as turtle_module
import random
import colorgram

def draw_square(t, s):
    for _ in range(4):
        t.forward(s) 
        t.left(90) 

def change_color(t):
    R = random.random()
    B = random.random()
    G = random.random()

    t.color(R, G, B)

def draw_shape(t, sides):
    change_color(t)
    for _ in range(sides):
        t.forward(100) 
        t.right(360/sides)     

def random_walk(t):
    change_color(t)
    t.pensize(15)
    t.speed("fastest")
    path = random.randint(0, 1)
    angles = [0, 90, 180, 270]
    if path == 0:
        t.right(angles[random.randint(0, len(angles)-1)])
        t.forward(30) 
    else: 
        t.left(angles[random.randint(0, len(angles)-1)])
        t.forward(30) 
 
def spirograph(t, size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        change_color(t)
        t.speed("fastest")   
        t.circle(100) 
        t.setheading(t.heading() + size_of_graph)         

def draw_spots_line(t, color_list, number_of_dots):
    for dot_count in range(1, number_of_dots + 1):
        t.dot(20, random.choice(color_list))
        t.forward(50)

        if dot_count % 10 == 0:
            t.setheading(90)
            t.forward(50)
            t.setheading(180)
            t.forward(500)
            t.setheading(0)

def draw_spots_art(t):
    color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
    turtle_module.colormode(255)
    t.speed("fastest")
    t.penup()
    t.hideturtle()
    number_of_dots = 100
    draw_spots_line(t, color_list, number_of_dots)


def draw_main():
    jeff = turtle_module.Turtle()


    #draw_square(jeff, 100)

    # for i in range (3, 10): 
    #     draw_shape(jeff, i)

    #for _ in range(200):
        #random_walk(jeff)

    #spirograph(jeff, 5)

    draw_spots_art(jeff)

    screen = turtle_module.Screen()
    screen.exitonclick()

draw_main()