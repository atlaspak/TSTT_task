import json

class DataManager:
    def __init__(self, input_file_path: str):
        self.file_path = input_file_path

    def get_data(self):
        with open(self.file_path) as json_file:
            data = json.load(json_file)
        return data

    def get_summary(self):
        data = self.get_data()
        total_scenarios = len(data)
        status_counts = {"pass": 0, "fail": 0, "busy": 0, "wait": 0}

        for item in data:
            for step in item['steps']:
                result = step['result']
                if result in status_counts:
                    status_counts[result] += 1

        summary = {
            "total_scenarios": total_scenarios,
            "statuses": status_counts
        }

        return summary
    