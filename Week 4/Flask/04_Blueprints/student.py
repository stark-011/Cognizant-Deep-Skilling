from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")

def home():

    data=["Barani","John","Arun"]

    return render_template(

        "home.html",

        students=data

    )

app.run(debug=True)