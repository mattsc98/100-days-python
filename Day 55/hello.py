from flask import Flask
import random

app = Flask(__name__)

app.debug = True
ran_num = random.randint(0, 9)

@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>'

@app.route('/bye')
def bye():
    return 'Bye!'

@app.route('/username/<name>')
def greet_name(name):
    return f"AWwwwww {name} aaaa!"

@app.route('/<int:num>')
def number(num):
    if num > ran_num:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    
    elif num < ran_num:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>" 
               
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"                  
    

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
    
    
