from enum import unique
# from flask_sqlalchemy import SQLAlchemy
import torch.nn as nn

# db = SQLAlchemy(app)

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # no activation and no softmax at the end
        return out


# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     DOB = db.Column(db.DateTime(), nullable=False)
#     faculty = db.Column(db.String(80), nullable=False)
#     reg_no = db.Column(db.String(80), unique= True, nullable=False)
#     course = db.Column(db.String(80), nullable=False)
#     def __repr__(self):
#         return '<User %r>' % self.username

    
        
        

