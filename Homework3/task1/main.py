from flask import Flask, render_template
from Homework3.task1.models import db, Student, Mark

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return "hello"


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("fill-student")
def fill_student():
    count = 5
    for i in range(1, count + 1):
        student = Student(first_name=f"Firstname{i}", last_name=f"Lastname{i}", group=f"Group{i}",
                          email=f"{i}@gmail.com")
        db.session.add(student)
    db.session.commit()
    print('данные добавлены')


@app.cli.command("fill-mark")
def fill_mark():
    count = 5
    for i in range(1, count + 1):
        mark = Mark(student_id=i, mark=f"{i}", subject=f"Subject{i}")
        db.session.add(mark)
    db.session.commit()
    print('данные добавлены')


@app.route('/students')
def all_students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)


if __name__ == "__main__":
    app.run(debug=True)



