from email.headerregistry import ContentDispositionHeader
from imaplib import Response_code
from os import confstr_names

from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Flask App Runner Deployment",
        "status": "healthy"
    })

@app.route('/hello')
def hello():
    return jsonify({
        "greeting": "Hello, AWS App Runner!"
    })


@app.route('/test')
def test():
    try:
        res = requests.get('https://www.google.de')
        con = res.content
    except Exception as e:
        con = e
    finally:
        return jsonify({
            "greeting": f"{con}"
    })

@app.route('/hellohello')
def hellohello():
    return jsonify({
        "greeting": "hellohello"
    })
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)