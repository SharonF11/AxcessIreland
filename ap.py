from flask import Flask, render_template, app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



#create a form class#
app = Flask(__name__)


#add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = "MY SECRET KEY"
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self): 
        return '<Name %r>' % self.name
        

class NameForm(FlaskForm):
    name = StringField("Pleae enter your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/index')
def index():
    return render_template("index.html")

# @app.route('/user')
# def user():
#     return render_template("user.html")

@app.route('/subscription')
def subscription():
    return render_template("subscription.html")

    #custom error pages 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route('/user', methods=['GET', 'POST'])
def user():
    name = None
    form = NameForm()
    #validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template("user.html",
        name = name,
        form = form)

if __name__ == '__main__':
    #app = create_app()
    app.run(debug=True)