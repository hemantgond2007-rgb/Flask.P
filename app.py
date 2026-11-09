from flask import Flask,render_template,request,url_for
app=Flask(__name__)
@app.route("/")
def home():
    course=["Python","Java","C++","Html","SQL"]
    student={
        "name":"Hemant",
        "course":"Flask",
        "city":"Maharajgnaj"
    }
    return render_template("index.html",course=course,student=student)
if(__name__=="__main__"):
    app.run(debug=True,port=5002)