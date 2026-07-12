from flask import Flask

from student import student

app=Flask(__name__)

app.register_blueprint(student)

app.run(debug=True)