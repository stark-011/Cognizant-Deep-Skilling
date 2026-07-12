from flask import Flask,request

app=Flask(__name__)

@app.route("/login",methods=["GET","POST"])

def login():

    if request.method=="POST":

        return "Login Successful"

    return "Login Page"

app.run(debug=True)