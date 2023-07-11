from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    marks = db.relationship('Mark', backref='student', lazy=True)

    def __repr__(self):
        return f'{self.first_name}, {self.last_name}, {self.group}, {self.email}'


class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject = db.Column(db.String(80), nullable=False)
    mark = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.name}'