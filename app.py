from flask import Flask,render_template,request,url_for
app=Flask(__name__)
@app.route("/")
def jinja_filter():
    first_name="Hemant"
    last_name="Gond"
    age=20
    course="Flask"
    return render_template("index.html",first_name=first_name,last_name=last_name,age=age,course=course,)

if(__name__=="__main__"):
    app.run(debug=True)