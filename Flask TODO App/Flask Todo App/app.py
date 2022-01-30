from msilib.schema import CheckBox
from flask import Flask, redirect, render_template, request, url_for
#importing sqlalchemy for database configrations
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import desc

app = Flask(__name__)
# making cofigration for database
app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///todo.db" #this is goted from flask sqlalchemy database configration   "https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
db = SQLAlchemy(app)

#creating class for database "https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application"
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    # date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    # or
    complete = db.Column(db.Boolean)
    # date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())


    # def __init__(self, title, complete=False):
    #     self.title = title
    #     self.complete = complete    

    # it will define what we want to show in the database like str method in django
    def __repr__(self) -> str:
        return f"{self.sno} {self.title} {self.desc} {self.complete} {self.date_created}"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    #getting value from the foem and creating a dynamic todo in the table.
    if request.method == "POST":
        add_todo = request.form['add_todo']
        disription = request.form['discription']
        todo = Todo(title=add_todo, desc=disription, complete=False)
        db.session.add(todo)
        db.session.commit()

        #this is to clear the form after submitting. Because if this is not written then each and every time form loads, the privios data will be submitted.
        return redirect("/")

    # Adding Todo in database. it will manually add all todo in database on load the page.
    # todo = Todo(title="1st todo", desc="wake up early", complete=False)
    # db.session.add(todo)
    # db.session.commit()

    # Displaying all the todos here but there is different language "Jinja2" the extention we have installed
    allTodos = Todo.query.all()
    # Deletign all the records 
    # db.session.query(Todo).delete()
    # db.session.commit()
    # print("todo is deleted")
    # print(allTodos)

    # Same like django context we will pass a variable to template for jinja2
    return render_template("index.html", allTodos = allTodos)

    # Here we have imported render_template to render index.html page 
    # return render_template("index.html")
    # print Hello word on front page 
    # return "<p>Hello, World!</p>"

# This is to understand app.route "Note /products in app.route"  // This is to create multipal end points.
@app.route("/delete/<int:sno>")
def delete(sno): 
    # Deleting Todos
    todo = Todo.query.get(sno)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno): 
    # Updating Todos
    todo = Todo.query.get(sno)
    if request.method == "POST":
        add_todo = request.form['add_todo']
        discription = request.form['discription']
        todo = Todo.query.get(sno)
        todo.title = add_todo
        todo.desc = discription
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    return render_template('update.html', todo = todo)


# This is to run our app & note that do not use it torun your app in production.
if __name__ == "__main__":
    app.run(debug=True)
    # if you want to change the port to run it
    # app.run(debug=True, port=8000)