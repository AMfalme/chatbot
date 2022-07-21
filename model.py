import torch.nn as nn


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


class Student(db.):
    def __init__(self, name, DOB, study_year, faculty,reg_no, course, fee_balance, *args):
        super(Student, self).__init__(*args)
        self.name = name
        self.DOB = DOB
        self.faculty = faculty
        self.reg_no = reg_no
        self.course = course
        self.fee_balance = fee_balance
        self.study_year = study_year
        
        

