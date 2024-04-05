from flask import jsonify, views
from data_manager import DataManager

class APIHandler(views.MethodView):
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

    def get_items(self):
        data = self.data_manager.get_data()
        return jsonify(data)

    def get_summary(self):
        summary = self.data_manager.get_summary()
        return jsonify(summary)
