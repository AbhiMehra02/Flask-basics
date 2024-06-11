from flask import Flask, render_template,url_for
from employees import employees_data

# create the flask app
app=Flask(__name__)

# Home Page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")

# about page
@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template(
        "evaluate.html",
        title="Evaluate",
        number=num
    )

@app.route("/employees")
def employees():
    return render_template(
        "employees.html",
        title="Employees",
        emps=employees_data
    )


@app.route("/employees/managers")
def managers():
    return render_template(
        "managers.html",
         title="Managers",
         emps=employees_data
    )

# start the app
if __name__=="__main__":
    app.run(debug=True)

