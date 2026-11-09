from flask import Flask,request,render_template


app=Flask(__name__)

@app.route("/")
def home():
    name="Hemant"
    course="Flask"
    status="Active"

    return  render_template("index.html",
                            name=name,
                            course=course,
                            status=status)

if __name__=="__main__":
    app.run(debug=True)  