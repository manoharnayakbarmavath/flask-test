from flask import Flask, jsonify

app = Flask(__name__)

# Define a simple GET route
@app.route('/', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)
