from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Aniket Puranik',
        'title': 'Am I a Billionare?',
        'content': 'Do I need to become this?',
        'date_posted': 'Sept 19, 2024'
    },
    {
        'author': 'Aniket Puranik',
        'title': 'How I became Billionare?',
        'content': 'Target acheived of becoming a billionare before 30',
        'date_posted': 'Sept 20, 2024'
    }
]


@app.route("/")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
