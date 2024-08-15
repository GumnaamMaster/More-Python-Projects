from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_email
from sqlalchemy.sql import func
from werkzeug import secure_filename

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Kakran@123@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://qugifwiuywziwc:8061a4280a81b4b32e755d993c1b079ba16abd467d889c009619d6369c9f610a@ec2-54-243-147-162.compute-1.amazonaws.com:5432/d4sgge99vieo3v?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
    """Somehow by importing db from virtual session table got created in database."""
    # all that was due to that db.Model the Model module.
    # now 'map error' occured coz we were just sending plane strings (as they say) to the database but database didn't recognize
    # it coz its database and database understand database objects 'models what they say', this Data class is inherting shits
    # from db.Model and that db.Model is acting or controlling this class so Data class is inherited + acted and that's why
    # this Data class is containig database models as they just created the table in pytnon session due to inherited db.Model
    # that's why they created a Data object passed it with email and height which initializes the object in __init__ method
    # and those attributes then become database models as they were passed to Data and then that session.add method now can add
    # database models to the database by having data 'the object of Data class' so that n number of arguments can be added to the
    # database in real time.
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    email_cus = db.Column(db.String(120), unique = True)
    height_cus = db.Column(db.Integer)

    def __init__(self, email_cus, height_cus):
        self.email_cus = email_cus
        self.height_cus = height_cus


@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/success.html") --> yeah this shit ain't working. showing "method not allowed" error.
# @app.route("/success") ---> and yeah...  even this is not working as well coz in index.html the success.html has "method = POST"
# and python decorators /*"@app.route("/shitsinside")" <-- these methods"*/ implicitly declare them as GET so u must declare
# them explicitly as POST like below.... in order to make them work.

@app.route("/success", methods = ['POST'])
def success():
    global file
    if request.method == 'POST':
        file = request.files["file"]
        file.save(secure_filename("uploaded_"+file.filename))
        with open("uploaded_"+file.filename,"a") as f:
            f.write("This was added later!")
        print(file)
        print(type(file))
        return render_template("index.html", btn = "download.html") # after clicking on submit and getting this btn with no missing
                    # they get btn which says download.html hence it will go to the templates folder where it founds the page and after
                    # that this page will point to the download function which lets the user to download by returning the file and not
                    # another web page as done earlier all the time.

@app.route("/download")
def download():
    return send_file("uploaded_"+file.filename, attachment_filename = "yourfile.csv", as_attachment = True)

# not showing any error for invalid email id, also no email is sent for invalid ids.
if __name__ == "__main__":
    app.debug = True
    app.run()
