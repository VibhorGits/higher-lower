from flask import Flask
import random

random_num = random.randint(0, 9)
print(random_num)

app = Flask(__name__)


def h1_decorator(function):
    def wrapper():
        return f'<h1>{function()}</h1> ' \
               f'<img src = "https://media.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.gif"/>'

    return wrapper


@app.route('/')
@h1_decorator
def guess_num():
    return "Guess a number between 0 and 9"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_num:
        return "<h1 style = 'color: orange'> Too High! Try Again! </h1>"\
               "<img src = 'https://media.giphy.com/media/v1" \
               ".Y2lkPTc5MGI3NjExdTF5c2cxdmRnbGl2Y2lsZXl5NzB1MWUzcTVmYmFtZnR4NnhqeTVrNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qT4lb3cV4K1h8hrzkZ/giphy.gif'/>"

    elif guess < random_num:
        return "<h1 style = 'color: purple'> Too Low! Try Again! </h1>"\
               "<img src = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmUxOWUzYzVpNDJydGMybm5kYm14ZGNxZHZkbnBtaDZya3k3ajhxcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l1J9u3TZfpmeDLkD6/giphy.gif'/>"

    else:
        return "<h1 style = 'color: purple'> Damn You found me! </h1>" \
               "<img src = 'https://media.giphy.com/media/LW6hZxaWkkWrK/giphy.gif'/>"



if __name__ == "__main__":
    app.run(debug=True)
