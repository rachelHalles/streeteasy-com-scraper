thonimport json

class Exporter:
    def export_to_json(self, data, filename):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data exported to {filename}")