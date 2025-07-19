from flask import Flask, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)

@app.route('/api/prompts', methods=['GET'])
def get_prompts():
    return send_from_directory(directory='.', path='prompts.json', mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
