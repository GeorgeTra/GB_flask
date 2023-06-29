from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def get_base():
    return render_template('base.html')


@app.route('/clothes/')
def get_clothes():
    return render_template('clothes.html')


@app.route('/shoes/')
def get_shoes():
    return render_template('shoes.html')


@app.route('/jacket/')
def get_jacket():
    return render_template('jacket.html')


if __name__ == '__main__':
    app.run(debug=True)