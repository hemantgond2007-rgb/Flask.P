from flask import Flask,request


app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Home page"

@app.route("/search")
def search():
    name=request.args.get("name","Guest")
    course=request.args.get("course","Unknown")
    return f"Hello {name} you are learning {course}"

if __name__=="__main__":
    app.run(debug=True)  