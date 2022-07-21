import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# root = Tk()
# root.title("Chatbot")


with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Anne"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    return "Okay, kindly tell more ..."


# def predict_responses():
    
#     send = "You -> "+e.get()
#     txt.insert(END, "n"+send)
#     user = e.get().lower()
#     if(user == "hello"):
#         txt.insert(END, "n" + "Bot -> Hi")
#     elif(user == "hi" or user == "hii" or user == "hiiii"):
#         txt.insert(END, "n" + "Bot -> Hello")
#     elif(e.get() == "how are you"):
#         txt.insert(END, "n" + "Bot -> fine! and you")
#     elif(user == "fine" or user == "i am good" or user == "i am doing good"):
#         txt.insert(END, "n" + "Bot -> Great! how can I help you.")
#     else:
#         txt.insert(END, "n" + "Bot -> Sorry! I dind't got you")
#     e.delete(0, END)
# txt = Text(root)
# txt.grid(row=0, column=0, columnspan=2)
# e = Entry(root, width=100)
# e.grid(row=1, column=0)
# send = Button(root, text="Send", command=send).grid(row=1, column=1)
# root.mainloop()

# def newChat():
#     chat = Chat(pairs, reflections)


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)

