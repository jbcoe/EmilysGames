import words_with_emily

g = words_with_emily.Game()

from flask import Flask, abort, redirect, url_for
app = Flask(__name__)
from jinja2 import Template


@app.route("/game")
def game():
    word, matches = g.generate_word_and_matches()
    return Template("""
            <h1>{{word}} [{{score}}]</h1>
            <ul>
            {% for m in matches %}<li><a href="../match/{{word}}/{{m}}">{{m}}</a></li>{% endfor %}
            </ul>
            """).render({'word': word, 'score': g.get_score(), 'matches': matches})


@app.route("/match/<word>/<match>")
def match(word, match):
    points, common = words_with_emily.calculate_points(word, match)
    g.increase_score(points)
    return redirect(url_for('game'))

if __name__ == "__main__":
    app.run()
