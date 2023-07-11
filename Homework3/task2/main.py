from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from Homework3.task2.forms import LoginForm, RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi, baby!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        print(email, password)
    ...
    return render_template('register.html', form=form)





