from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tributes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model
class Tribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=True)
    message = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html', year=datetime.now().year)

@app.route('/military_bio')
def military_bio():
    return render_template('military_bio.html')

# Routes
@app.route('/tribute_wall', methods=['GET', 'POST'])
def tribute_wall():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form.get('date')  # Optional
        message = request.form['message']
        author = request.form['author']
        new_tribute = Tribute(name=name, date=date, message=message, author=author)
        db.session.add(new_tribute)
        db.session.commit()
        return redirect(url_for('tribute_wall'))
    
    tributes = Tribute.query.order_by(Tribute.timestamp.desc()).all()
    year = datetime.now().year
    return render_template('tribute_wall.html', tributes=tributes, year=year)

if __name__ == '__main__':
    app.run(debug=True)
