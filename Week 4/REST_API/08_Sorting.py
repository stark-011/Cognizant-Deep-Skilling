@app.get("/students")

def sort(

order:str="asc"

):

    return {

        "Sort":order

    }