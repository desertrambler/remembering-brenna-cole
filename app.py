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
    tribute = '''
    One day my border collie, Jasper, and I were walking through the neighborhood, as we often do. 
    We came across a young lady walking her golden retriever and the dogs did what dogs do. 
    This was, of course, Brenna and Daisy. 
    Over the next few years, Jasper and I would cross paths with Daisy and Brenna many more times. 
    It was extraordinary and a little crazy how good of friends Jasper and Daisy became. 
    There were times they would get uncontrollably excited to see each other and it was definitely the high point of their days. 
    Brenna and I would chat while the dogs were meeting and we found we had a great deal in common. 
    Brenna was a true rising star in the cyber operations world. 
    I had a particular understanding of how extraordinary her accomplishments were because I’m a retired USAF officer with some time in cyber operations. 
    I also found out we were both from Iowa. 
    Around last spring Jasper and I quit walking where we would see Brenna and Daisy. 
    Jasper turned 15 this summer it became just a little too far for him. 
    So, we hadn’t seen Brenna or Daisy since sometime before then. 
    The week of Christmas my wife and daughter, who had also met Brenna and Daisy a time or two while dog walking, told me of a memorial picture on a utility pole on Broadway. 
    I couldn’t believe it. 
    Hearing of her passing left me with a profound sense of sadness and loss. 
    I never knew Brenna other than passing on the street, but every time we met and chatted I left smiling. 
    I’m confident others can relate. I can only count myself lucky to have met and gotten to know Brenna. 
    May she rest in peace.
    '''
    return render_template('tribute_wall.html')

if __name__ == '__main__':
    app.run(debug=True)
