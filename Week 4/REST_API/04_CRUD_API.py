from fastapi import FastAPI

app=FastAPI()

students=[]

@app.get("/students")

def get_students():

    return students

@app.post("/students")

def add(student:dict):

    students.append(student)

    return student

@app.put("/students/{id}")

def update(id:int,student:dict):

    students[id]=student

    return student

@app.delete("/students/{id}")

def delete(id:int):

    students.pop(id)

    return {

        "Deleted":id

    }