from flask import Flask, redirect, url_for, render_template, request, session
#Focussing on Bootstrap and Template Inheritance.

app = Flask(__name__)
app.secret_key = "DUMMY" #Secret key for encryption. In reality it needs to be secure..

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
        session["user"] = user #Basic data for session, as a dictionary key and value.
        return redirect(url_for("user"))
    else:
        if "user" in session: #If they've signed in.
            return redirect(url_for("user")) #Take them to their page 
        return render_template("login.html") #Means we didn't click the submit button.

@app.route("/user")
def user():
    if "user" in session: #If the user is logged in (there's a session?):
        user = session["user"] #Store the user in a variable.
        #Display it to the user.
        return f"<h1>{user}</h1>" #Shows the user their name in a H1 tag.
    else: #If there's no session (no user).
        return redirect(url_for("login"))


@app.route("/logout") #Takes them back to the login page.
def logout():
    session.pop("user", None) #Removes session data.
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True) #Means the server doesn't have to be rerun each time a page is changed.
