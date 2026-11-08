from flask import Flask 
app=Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

@app.route("/about")
def about ():
    return "This is my About page"
@app.route("/user/<name>")
def user(name):
    return  f"Hello {name}"
@app.route("/student/<name>/<course>")
def student(name,course):
    return f"{name} is Learnig {course}"
if __name__=="__main__":
    app.run(debug=True)