from fastapi import FastAPI

app = FastAPI()

courses = [
    {"id":1,"name":"Python"},
    {"id":2,"name":"Java"}
]

@app.get("/courses")
def get_courses():
    return courses

@app.get("/courses/{id}")
def get_course(id:int):

    for c in courses:

        if c["id"]==id:

            return c

    return {"message":"Course Not Found"}