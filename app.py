from flask import Flask 
from uuid import UUID

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

@app.route("/user/<int:id>")
def user(id):
    return f"User id :{id}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"Amount is  :{amount}"

@app.route("/user/<string:name>")
def name(name):
    return f" Welcome {name} to this flask tutorial"

@app.route("/files/<path:file_path>")
def file_path(file_path):
    return file_path
@app.route("/student/<uuid:user_id>")
def student(user_id):
    return str(user_id)

if __name__=="__main__":
    app.run(debug=True)