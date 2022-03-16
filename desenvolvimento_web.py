
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')

def api():
    return jsonify({'site': 'meu site'})

if __name__ == '__main__':
    app.run(debug=True)
