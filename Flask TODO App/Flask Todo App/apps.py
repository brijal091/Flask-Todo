from flask import Flask, render_template
#importing sqlalchemy for database configrations
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

app = Flask(__name__)
# making cofigration for database
app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///todo.db" #this is goted from flask sqlalchemy database configration   "https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    # Here we have imported render_template to render index.html page 
    return render_template("index.html")
    # print Hello word on front page 
    # return "<p>Hello, World!</p>"

# This is to understand app.route "Note /products in app.route"  // This is to create multipal end points.
@app.route("/products")
def product():
    return "This is Product page"


# This is to run our app & note that do not use it torun your app in production.
if __name__ == "__main__":
    app.run(debug=True)
    # if you want to change the port to run it
    # app.run(debug=True, port=8000)