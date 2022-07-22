from crypt import methods
from unicodedata import name
from flask import Flask, render_template, request, jsonify, redirect, url_for
from chat import get_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

date_format = '%Y-%m-%d'

db = SQLAlchemy(app)

class Student(db.Model):
    FACULTY_TYPES = [
        ('admin', 'Admin'),
        ('regular-user', 'Regular user')
    ]
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    DOB = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    faculty = db.Column(ChoiceTypes(FACULTY_TYPES), nullable=False)
    reg_no = db.Column(db.String(80), unique= True, nullable=False)
    course = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

    

@app.get("/")
def index_get():
    return render_template("registration.html")


@app.post("/register")
def register():
    data = request.get_json()
    username = data["names"]
    email = data["email"]
    DOB = data["DOB"]
    faculty = data["faculty"]
    reg_no = data["reg_no"]
    course = data["course"]
    
    try:
        date_obj = datetime.strptime(DOB, date_format)
        print(date_obj)
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
    
    new_student = Student(
        username = username,
        email=email,
        # DOB=date_obj,
        faculty=faculty,
        reg_no=reg_no,
        course=course,
        )
    db.session.add(new_student)
    db.session.commit()
    return redirect('/chat')
   
    
    
@app.get("/chat")
def chat():
    return render_template('index.html')
    
@app.post("/predict")
def predict():
    try:
        text = request.get_json().get("message")
    except Exception as e: 
        print('error occured: ',e)
    # TODO:check if text is valid
    response = get_response(text)
    print(response)
    message = {"answer": response}
    return jsonify(message)


@app.get("/report")
def report():
    data = {'Task' : 'Hours per Day', 'FOBE' : 5, 'ENGINEERING' : 11, 'FAMECO' : 2, 'CIT' : 2, 'MEDICINE' : 2, 'FOST' : 7}
    #print(data)
    return render_template('pie-chart.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
