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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)