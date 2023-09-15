import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = 'Day 25\\day-25-us-states-game-start\\blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('Day 25\\day-25-us-states-game-start\\50_states.csv')
all_states = data.state.to_list()

guesses = []
while len(guesses) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing = [state for state in all_states if state not in guesses]
                
        new_data = pandas.DataFrame(missing)
        new_data.to_csv('Day 25\\day-25-us-states-game-start\\missing.csv')
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

