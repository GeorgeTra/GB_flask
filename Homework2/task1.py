from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        return f'Вы ввели число {number}, его квадрат равен {number * number}.'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
