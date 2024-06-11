from flask import Flask

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome to home page!</h1>"

# @app.route("/welcome/steve")
# def welcome_steve():
#     return f"<h1>hey steve, welcome to Webpage!</h1>"

# @app.route("/welcome/tony")
# def welcome_tony():
#     return f"<h1>hey tony, welcome to Webpage!</h1>"

# rather  than above method to write for all user or person we use dynamic way/url /
@app.route("/welcome/<name>")
def welcome_tony(name):
    return f"<h1>hey {name.title()}, welcome to Webpage!</h1>"



if __name__=="__main__":
    app.run(debug=True)

