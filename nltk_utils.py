import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

from nltk.chat.util import Chat, reflections

print(reflections)

stemmer = PorterStemmer()


def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence)


def stem(word):
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag



# def predict_responses():
    
#     root = Tk()
#     root.title("Chatbot")
#     def send():
#         send = "You -> "+e.get()
#         txt.insert(END, "n"+send)
#         user = e.get().lower()
#         if(user == "hello"):
#             txt.insert(END, "n" + "Bot -> Hi")
#         elif(user == "hi" or user == "hii" or user == "hiiii"):
#             txt.insert(END, "n" + "Bot -> Hello")
#         elif(e.get() == "how are you"):
#             txt.insert(END, "n" + "Bot -> fine! and you")
#         elif(user == "fine" or user == "i am good" or user == "i am doing good"):
#             txt.insert(END, "n" + "Bot -> Great! how can I help you.")
#         else:
#             txt.insert(END, "n" + "Bot -> Sorry! I dind't got you")
#         e.delete(0, END)
#     txt = Text(root)
#     txt.grid(row=0, column=0, columnspan=2)
#     e = Entry(root, width=100)
#     e.grid(row=1, column=0)
#     send = Button(root, text="Send", command=send).grid(row=1, column=1)
#     root.mainloop()