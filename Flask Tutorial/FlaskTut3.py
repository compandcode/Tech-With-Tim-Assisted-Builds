from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta #For sessions.
#from sql_alchemy import SQLAlchemy
#Focussing on Bootstrap and Template Inheritance.

app = Flask(__name__)
app.secret_key = "DUMMY" #Secret key for encryption. In reality it needs to be secure..
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://users.sqlite3'
app.permanent_session_lifetime = timedelta(days=7) #Sets the 'Permenant Session' lifetime to 7 days and then delete it after.

#db = SQLAlchemy(app)

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
        session.permenant = True #Sets it to the Constant's value.
        flash("Login Successful")
        #Get the information and send the user to the user's page.
        user = request.form["nm"] #Dictionary key from the form.
        session["user"] = user #Basic data for session, as a dictionary key and value.
        return redirect(url_for("user"))
    else:
        if "user" in session: #If they've signed in.
            flash("Already Logged In !!")
            return redirect(url_for("user")) #Take them to their page 
        return render_template("login.html") #Means we didn't click the submit button.

@app.route("/user", methods=["POST","GET"])
def user():
    email = None

    if "user" in session: #If the user is logged in (there's a session?):
        user = session["user"] #Store the user in a variable.
        
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("email saved!!")
        else:
            if "email" in session:
                email = session["email"] #Gets the email from the session instead.
       
        #Display it to the user.
        return render_template("user.html", email=email)
    else: #If there's no session (no user).
        flash("You Are Not Logged In!!")
        return redirect(url_for("login"))


@app.route("/logout") #Takes them back to the login page.
def logout():
    if "user" in session:  # If the user is logged in (there's a session?):
        user = session["user"]  # Store the user in a variable.
        flash(f"{user} Logged Out Successfully", category="info")
    session.pop("user", None) #Removes session data.
    session.pop("email", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True) #Means the server doesn't have to be rerun each time a page is changed.
