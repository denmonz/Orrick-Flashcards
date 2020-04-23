from flask import *
from Main import main
from flask_cors import CORS, cross_origin
from json import *
from Main2 import main2

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)

@app.route('/q')
@cross_origin()
def question():
    response = jsonify(main("apple.docx"))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/a')
def answer():
    data ={
    "section1": [
        {
            "question": "first q?",
            "answer": "first a."
        },
        {
            "question": "second q?",
            "answer": "second a."
        },
        {
            "question": "third q?",
            "answer": "third a."
        }
    ]}

    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True)
