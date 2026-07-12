import os

DATABASE=os.getenv("DATABASE_URL")

SECRET=os.getenv("SECRET_KEY")

print(DATABASE)