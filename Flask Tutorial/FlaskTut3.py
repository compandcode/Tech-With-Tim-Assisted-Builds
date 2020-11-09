from flask import Flask, redirect, url_for, render_template, request
#Focussing on Bootstrap and Template Inheritance.

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("new.html") #Nav bar stays because it's inherited.

#HTTP GET (insecure) and Post Methods: Client Server.
@app.route("/login", methods=["POST","GET"]) #Methods we can use on the login page.
def login():
    if request.method == "POST":
        #Get the information and send the user to the user's page.
        user = request.form["nm"] #Dictionary key from the form.
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html") #Means we didn't click the submit button.

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True) #Means the server doesn't have to be rerun each time a page is changed.
