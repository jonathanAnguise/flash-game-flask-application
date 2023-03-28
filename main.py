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



#Create DB if does not exist TO COMMENT
#with app.app_context():
#     db.create_all()
#     new_word = Words(word="toto", word_translation="titi")
#     db.session.add(new_word)
#     db.session.commit()

with app.app_context():
    posts = Words.query.all()
       
@app.route('/')
def run_game():
    # return index template with a random word from the db from posts list 
    return render_template("index.html", word=posts[randint(0, len(posts)-1)])
#
#
###WTForm
#class CreatePostForm(FlaskForm):
#    title = StringField("Blog Post Title", validators=[DataRequired()])
#    subtitle = StringField("Subtitle", validators=[DataRequired()])
#    author = StringField("Your Name", validators=[DataRequired()])
#    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
#    body = CKEditorField("Blog Content", validators=[DataRequired()])
#    # body = StringField("Blog Content", validators=[DataRequired()])
#    submit = SubmitField("Submit Post")
#
#posts = BlogPost.query.all()
#
#
#
#
#@app.route("/post/<int:index>")
#def show_post(index):
#    requested_post = None
#    for blog_post in posts:
#        if blog_post.id == index:
#            requested_post = blog_post
#            print(requested_post)
#    return render_template("post.html", post=requested_post)
#
#
#@app.route("/about")
#def about():
#    return render_template("about.html")
#
#
#@app.route("/contact")
#def contact():
#    return render_template("contact.html")
#
#
#@app.route("/new-post", methods=['GET', 'POST'])
#def create_new_post():
#    form = CreatePostForm()
#    if form.validate_on_submit():
#        new_post = BlogPost(
#            title=form.title.data,
#            subtitle=form.subtitle.data,
#            date=datetime.datetime.now(),
#            body=form.body.data,
#            author=form.author.data,
#            img_url=form.img_url.data
#        )
#        db.session.add(new_post)
#        db.session.commit()
#    return render_template("make-post.html", form=form, is_a_new_post=True)
#
#
#@app.route("/edit-post/<post_id>")
#def edit_post():
#    if form.validate_on_submit():
#        new_post = BlogPost(
#            title=form.title.data,
#            subtitle=form.subtitle.data,
#            date=datetime.datetime.now(),
#            body=form.body.data,
#            author=form.author.data,
#            img_url=form.img_url.data
#        )
#        db.session.add(new_post)
#        db.session.commit()
#    return render_template("make-post.html", form=form, is_a_new_post=False, post_name="tobeUpdate")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
