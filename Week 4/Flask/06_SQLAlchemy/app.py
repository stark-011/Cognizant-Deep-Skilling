from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///college.db"

db=SQLAlchemy(app)

class Student(db.Model):

    id=db.Column(

        db.Integer,

        primary_key=True

    )

    name=db.Column(

        db.String(100)

    )

    age=db.Column(

        db.Integer

    )

with app.app_context():

    db.create_all()

app.run(debug=True)