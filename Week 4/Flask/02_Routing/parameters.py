from flask import request

@app.route("/search")

def search():

    name=request.args.get("name")

    return f"Searching {name}"