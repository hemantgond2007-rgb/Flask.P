from flask import Flask,render_template,request,url_for
app=Flask(__name__)
@app.route("/")
def home():
    is_loged_in=True
    return render_template("index.html",is_loged_in=is_loged_in)


if(__name__=="__main__"):
    app.run(debug=True,port=5001)