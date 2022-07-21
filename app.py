from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("index.html")


@app.post("/predict")
def predict():
    print(request.data)
    text = request.get_json().get("message")
    try:
        print("We are here")
        text = request.get_json().get("message")
    except Exception as e: 
        print('error occured: ',e)
    # TODO:check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
