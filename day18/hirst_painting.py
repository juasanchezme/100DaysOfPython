# import colorgram

# # Extract 256 colors from an image.
# colors = colorgram.extract('day18/Hirst_painting.png', 256)

# # could only extract 34 because of the image quality
# #print(len(colors))


# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[1]
# rgb = first_color.rgb # e.g. (255, 151, 210)

# color_list = []

# for i in range(0, 34):
#     color = colors[i].rgb
#     r, g, b = color.r, color.g, color.b
#     color_list.append((r,g,b))

# print(color_list)


from turtle import Turtle, Screen
import random
t = Turtle()
screen = Screen()
screen.colormode(255)


painting_colors = [(130, 165, 206), (26, 42, 64), (232, 149, 91), (202, 220, 236), (205, 135, 148), (238, 210, 86), (133, 183, 161), (33, 109, 162), (173, 59, 45), (157, 31, 30), (178, 27, 30), (51, 39, 42), (237, 212, 218), (136, 70, 81), (37, 61, 54), (239, 164, 152), (219, 80, 72), (52, 122, 107), (230, 164, 168), (1, 103, 73), (213, 228, 226), (196, 99, 107), (23, 62, 118), (59, 54, 50), (17, 83, 107), (180, 189, 216), (110, 126, 151), (167, 205, 215), (170, 204, 191), (85, 151, 138), (62, 146, 185), (63, 66, 59), (127, 129, 124)]

def run_color():
    color = random.choice(painting_colors)
    return color


t.hideturtle()
t.penup()
t.goto(-325, -325)
t.showturtle()
t.pendown()
t.speed(0)


altura = 0
for i in range(10):
    altura += 50
    for i in range(10):
        t.pencolor(run_color())
        t.dot(20)
        t.penup()
        t.forward(50)
        t.pendown()
        

    t.penup()
    t.goto(-325, -325 + altura)
    t.pendown

t.hideturtle()


screen.screensize(40000,45000)
screen.exitonclick()

