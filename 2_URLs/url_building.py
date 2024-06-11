from flask import Flask,redirect,url_for
import time

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome, to HomePage</h1>"

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1>Congratz {sname.title()}, you have passed with {marks} </h1>"

@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1>Sorry {sname.title()}, you failed with {marks}</h1>"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<30:
        time.sleep(1)
        # redirect user to fail
        return redirect(url_for("failed",sname=name,marks=num))
    else :
        time.sleep(1)
        # redirect user to pass
        return redirect(url_for("passed",sname=name,marks=num))



if __name__=="__main__":
    app.run(debug=True)
 
