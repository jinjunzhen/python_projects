from turtle import Turtle

class State_name:
    def __init__(self):
        self.name_tags = []

    def add_name_tag(self, name, x, y):
        new_tag = Turtle()
        new_tag.penup()
        new_tag.color('black')
        position = (x, y)
        new_tag.goto(position)
        new_tag.write(name, font=("Arial", 12, "normal"))
        new_tag.hideturtle()
        self.name_tags.append(new_tag)








