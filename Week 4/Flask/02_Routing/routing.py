from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/about")
def about():
    return "About Page"

@app.route("/student/<name>")
def student(name):
    return f"Hello {name}"

@app.route("/marks/<int:mark>")
def marks(mark):
    return f"Marks : {mark}"

if __name__=="__main__":
    app.run(debug=True)