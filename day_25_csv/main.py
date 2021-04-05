import pandas
import turtle
from state_name import State_name

screen = turtle.Screen()
screen.title("U.S. States Game")
data = pandas.read_csv("50_states.csv")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


game = State_name()
game_is_on = True



while game_is_on:
    answer_state = screen.textinput(title="Guess the state",  prompt="write any of the state name")
    count = len(data[data.state == answer_state])
    if count > 0:
        data_state = data[data.state == answer_state]
        game.add_name_tag(answer_state, int(data_state.x), int(data_state.y))
    else:
        game_is_on = False

screen.exitonclick()
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()