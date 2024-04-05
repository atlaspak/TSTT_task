import os
from flask import Flask
from data_manager import DataManager
from api_handler import APIHandler

app = Flask(__name__, static_folder='client/build', static_url_path='')

# API initialization
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, 'input.json')
data_manager = DataManager(input_file_path)
api_handler = APIHandler(data_manager)

# Route registration
app.add_url_rule('/api/items', view_func=api_handler.get_items)
app.add_url_rule('/api/summary', view_func=api_handler.get_summary)

if __name__ == '__main__':
    app.run(debug=True)