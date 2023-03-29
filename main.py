from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from random import randint


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class Words(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String, unique=True, nullable=False)
    word_translation = db.Column(db.String, unique=False, nullable=False)


@app.route("/get-words", methods=['GET'])
def get_word():
    with app.app_context():
        posts = Words.query.all()
    word=posts[randint(0, len(posts)-1)]
    answer = { "word" : word.word,
        "word_translation" : word.word_translation
    }
    return answer


@app.route('/')
def run_game():
    # return index template with a random word from the db from posts list 
    return render_template("index.html", word=get_word())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

