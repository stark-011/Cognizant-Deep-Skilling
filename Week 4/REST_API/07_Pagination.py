@app.get("/students")

def page(

page:int=1,

limit:int=10

):

    return {

        "page":page,

        "limit":limit

    }