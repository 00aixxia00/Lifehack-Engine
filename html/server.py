from flask import Flask, request, jsonify
from flask import render_template
import queryhandler as handle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This part handles the post requests from the indexhtml,
# It opens the information from the questionbar and sents it towards
# the queryhandler
@app.route('/posthandler', methods=['POST'])
def handlerhandler():
    if request.method == 'POST':
        text = request.form.get('questionbar')
        result = handle.query_handler(text)
        #result = ("test")
        return result
    else:
        return 'ERROR'

# This part redirects you to the index html page when you load the server
@app.route('/')
def testpage():
    return render_template('index.html')

# This part runs the flask server as soon as this file is opened
if __name__ == "__main__":
    app.run(debug=True)
