from flask import Flask, render_template
import game_of_life as game

app = Flask(__name__)

@app.route('/')
def index():
    game.GameOfLife(25, 25)
    return render_template('index.html')

@app.route('/live')
def live():
    life = game.GameOfLife()
    if life.counter > 0:
        life.form_new_generation()
    life.counter += 1
    return render_template('live.html',
                            new_world=life.world,
                            old_world=life.old_world,
                            counter=life.counter)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)