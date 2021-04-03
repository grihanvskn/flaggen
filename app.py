from flask import Flask, render_template, request
from markupsafe import escape
import flaggen


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('genpg.html')


@app.route('/about/')
@app.route('/about/<username>')
def about(username='me'):
    return f'All about {escape(username)}'

@app.route('/', methods=['GET', 'POST'])
def template():
    if request.form['contact'] == "triv":
        flaggen.tricoleurv("red", "white", "green")

if __name__ == '__main__':
    app.run()
