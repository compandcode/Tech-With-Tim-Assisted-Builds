from flask import Flask, redirect, url_for
#https://www.youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX Start with 2 next.

app = Flask(__name__) #Creates instance of webpage.

@app.route("/")
def home():
    return "Hello, this is the homepage <h1>Hello World</h1>"

@app.route("/about")
def about():
    return "About <strong>CompAndCode</strong>"

@app.route("/admin")
def admin():
    return redirect(url_for("home")) #Redirects to the homepage.

if __name__ == "__main__":
    app.run()