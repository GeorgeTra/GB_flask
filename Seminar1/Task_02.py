from flask import Flask, render_template

app = Flask(__name__)


@app.route('/about1/')
def get_about():
    return render_template('about1.html')


@app.route('/contacts/')
def get_contacts():
    return render_template('contacts.html')


@app.route('/base/')
def get_base():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()