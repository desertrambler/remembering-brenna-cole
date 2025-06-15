from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tributes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

# Model
class Tribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=True)
    message = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html', year=datetime.now().year)

@app.route('/military_bio')
def military_bio():
    return render_template('military_bio.html')

@app.route('/tribute_wall')
def tribute_wall():
    tributes = Tribute.query.order_by(Tribute.timestamp.desc()).all()
    year = datetime.now().year
    return render_template('tribute_wall.html', tributes=tributes, year=year)

@app.route('/add_tribute', methods=['POST'])
def add_tribute():
    name = request.form.get('name', 'Tribute')
    message = request.form['message']
    author = request.form['author']
    date = datetime.now()

    new_tribute = Tribute(name=name, message=message, author=author, date=date)
    db.session.add(new_tribute)
    db.session.commit()

    return render_template('tribute_partial.html', tribute=new_tribute)

if __name__ == '__main__':
    app.run(debug=True)
