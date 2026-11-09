from flask import Flask ,render_template,request,redirect,url_for
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def login():
    name=""
    if request.method=="POST":
        name=request.form.get("username")
        return redirect(url_for("home",name=name))
    return render_template("login.html",name=name)
@app.route("/home/<name>")
def home(name):
    return render_template("index.html",name=name)
if(__name__=="__main__"):
    app.run(debug=True,port=5001)