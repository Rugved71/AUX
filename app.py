# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello, Flask server is running!"

# Example API route
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(debug=True)