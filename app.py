from flask import Flask, jsonify

app = Flask(__name__)

# Define a simple GET route
@app.route('/', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
