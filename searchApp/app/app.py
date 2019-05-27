import json
from stackapi import StackAPI
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/json", methods=['GET'])
def getData():
    SITE = StackAPI('lifehacks')
    SITE.page_size = 100
    SITE.max_pages = 100

    questions = SITE.fetch('questions')
    items = questions.get('items')
    question_list = []
    for n in range(len(items)):
        question = {'question_id': items[n].get("question_id"),
                    'title': items[n].get("title"), }
        question_list.append(question)

    return json.dumps(question_list)


if __name__=='__main__':
    app.run(debug=True)
