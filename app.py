from flask import Flask, send_from_directory, jsonify
import json

app = Flask(__name__, static_folder='client/build', static_url_path='')

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/items')
def get_items():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
