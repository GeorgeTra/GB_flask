from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello!'


@app.route('/submit_email/', methods=['GET', 'POST'])
def submit_email():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Привет, {name}!'
    return render_template('form2.html')


if __name__ == '__main__':
    app.run()
