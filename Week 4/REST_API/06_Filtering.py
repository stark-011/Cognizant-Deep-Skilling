@app.get("/students")

def filter(

department:str=None

):

    return {

        "Department":department

    }