from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/all")

def all_data():

    courses = requests.get(
        "http://localhost:8001/courses"
    ).json()

    students = requests.get(
        "http://localhost:8002/students"
    ).json()

    return {

        "courses":courses,

        "students":students

    }