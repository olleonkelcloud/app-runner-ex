from urllib.request import urlopen
from urllib.error import URLError
from flask import Flask, jsonify

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
        with urlopen('https://www.google.de') as response:
            content = response.read()
    except URLError as e:
        content = str(e)
    finally:
        return jsonify({
            "greeting": f"{content}"
        })

@app.route('/hellohello')
def hellohello():
    return jsonify({
        "greeting": "hellohello"
    })
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)