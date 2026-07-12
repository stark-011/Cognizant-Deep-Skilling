from fastapi import FastAPI

app = FastAPI()

students = [
    {"id":1,"name":"Barani"},
    {"id":2,"name":"Arun"}
]

@app.get("/students")
def get_students():
    return students

@app.get("/students/{id}")
def student(id:int):

    for s in students:

        if s["id"]==id:

            return s

    return {"message":"Student Not Found"}