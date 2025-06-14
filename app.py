from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', year=datetime.now().year)

@app.route('/military_bio')
def military_bio():
    return render_template('military_bio.html')

@app.route('/tribute_wall')
def tribute_wall():
    return render_template('tribute_wall.html')

if __name__ == '__main__':
    app.run(debug=True)
