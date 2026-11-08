from flask import Flask 
app=Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

@app.route("/about")
def about ():
    return "This is my About page"
@app.route("/contact")
def contact():
    return "Welcome contact page"
if __name__=="__main__":
    app.run(debug=True)