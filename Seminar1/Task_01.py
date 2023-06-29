from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/sum/<int:num1>/<int:num2>/')
def summ(num1: int, num2: int) -> int:
    return f'{num1 + num2}'


@app.route('/text/<text_>/')
def get_len(text_: str) -> int:
    return f'<h1>{len(text_) = }</h1>'


@app.route('/hello/')
def html():
    return render_template('hello.html')


@app.route('/list/')
def html1():
    students = [{'first_name': 'George', 'last_name': 'Trakhtenberg', 'age': 40, 'average': 4},
                {'first_name': 'Ivan', 'last_name': 'Drago', 'age': 30, 'average': 3},
                {'first_name': 'Gregory', 'last_name': 'Tunberg', 'age': 20, 'average': 5},
                {'first_name': 'Agata', 'last_name': 'Travkina', 'age': 25, 'average': 4.5}]
    return render_template('list.html', students=students)


@app.route('/news/')
def get_news():
    news = [{'title': 'News1', 'text': 'text1', 'date': '23.06.23'},
            {'title': 'News2', 'text': 'text2', 'date': '24.06.23'},
            {'title': 'News3', 'text': 'text3', 'date': '25.06.23'},
            {'title': 'News4', 'text': 'text4', 'date': '26.06.23'},
            {'title': 'News5', 'text': 'text5', 'date': '27.06.23'}]
    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run()