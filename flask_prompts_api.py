from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/api/prompts', methods=['GET'])
def get_prompts():
    return send_from_directory(directory='.', path='prompts.json', mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
