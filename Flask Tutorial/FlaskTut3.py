from flask import Flask, redirect, url_for, render_template
#Focussing on Bootstrap and Template Inheritance.

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("new.html") #Nav bar stays because it's inherited.

if __name__ == "__main__":
    app.run(debug=True) #Means the server doesn't have to be rerun each time a page is changed.
