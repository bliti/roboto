#roboto_server.py
#simple flask server to serve TwiML

from flask import Flask


app = Flask(__name__)


@app.route('/answer', methods=['POST'])
def answer():
    with open('script.xml', 'r') as f:
        response = f.read()
    return response
    

@app.route('/call', methods=['GET'])
def call():
    pass
    
    
if __name__== "__main__":
    app.run(debug=True)