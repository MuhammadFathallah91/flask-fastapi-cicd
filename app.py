from flask import Flask
from fastapi import FastAPI
from mangum import Mangum

flask_app = Flask(__name__)
fastapi_app = FastAPI()

@flask_app.route("/")
def hello_flask():
    return "Hello from Flask!"

@fastapi_app.get("/fastapi")
async def hello_fastapi():
    return {"message": "Hello from FastAPI!"}

# Wrap FastAPI with Mangum to run on WSGI server
handler = Mangum(fastapi_app)

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000)
