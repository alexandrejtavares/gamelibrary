from flask import Flask, render_template, request, redirect, session, flash


class Game:

    def __init__(self, name, category, console) -> None:
        self.name = name
        self.category = category
        self.console = console


game1 = Game("Tetris", "Puzzle", "Atari")
game2 = Game("God of War", "Rack 'n slash", "PS2")
game3 = Game("Mortal Kombat", "Fight", "PS2")

game_list = []
game_list.append(game1)
game_list.append(game2)
game_list.append(game3)

app = Flask(__name__)
app.secret_key = 'Pwd'


@app.route("/")
def index():
    return render_template("list.html", title="Games", games=game_list)


@app.route("/new")
def new_game():
    return render_template("newgame.html", title="New Game")


@app.route("/add", methods=['POST', ])
def add():
    name = request.form["name"]
    category = request.form["category"]
    console = request.form["console"]
    game = Game(name, category, console)
    game_list.append(game)
    return redirect("/")

<<<<<<< HEAD

@app.route("/login")
def login():
    return render_template("login.html", title="Login")


@app.route('/authenticate', methods=['POST', ])
def autenticar():
    user = request.form['user']
    if user == 'root' and request.form['password'] == 'password':
        session['logged_user'] = user
        flash(f"User { user } logged successfully.", "success")
        return redirect('/')
    else:
        flash("Incorrect user or password.", "warning")
        return redirect('/login')


@app.route("/logout")
def logout():
    session["logged_user"] = None
    return redirect("/")

=======
# @app.route("/delete", methods=['POST',])
# def add():
#     name = request.form["name"]
#     category = request.form["category"]
#     console = request.form["console"]
#     game = Game(name, category, console)
#     game_list.append(game)
#     return redirect("/")
>>>>>>> 4b28d6a196fc58d04f5c5d0d8d387ddb57df8256

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
