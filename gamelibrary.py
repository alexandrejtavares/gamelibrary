from re import template
from tkinter.messagebox import YES
from flask import Flask, render_template

class Game:

    def __init__(self, name, category, console) -> None:
        self.name = name
        self.category = category
        self.console = console

app = Flask(__name__)

@app.route("/main")
def hello_world():
    game1 = Game("Tetris", "Puzzle", "Atari")
    game2 = Game("God of War", "Rack 'n slash", "PS2")
    game3 = Game("Mortal Kombat", "Fight", "PS2")
    game_list = [game1, game2, game3]
    return render_template("list.html", title="Games", games=game_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)