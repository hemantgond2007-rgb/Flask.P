from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/result/<int:marks>")
def marks(marks):
    if marks>=90:
       return "Grade : A"
    elif marks>=80 and marks<90:
        return "Grade : B"
    elif marks<80 and marks>=70:
        return "Grade : C"
    elif marks>=50 and marks<70:
        return "Grade : D"
    elif marks<50:
            return "Fail"
if __name__=="__main__":
    app.run(debug=True,port=5005)