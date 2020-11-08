from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) #Creates instance of webpage.

@app.route("/<name>") #Defines the landing page.
def home(name):
    return render_template("index.html",content=["King","CompAndCode"],r=2)

if __name__ == "__main__": #Always runs.
    app.run()