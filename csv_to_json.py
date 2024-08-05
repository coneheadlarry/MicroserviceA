from flask import Flask, request, jsonify
import csv
import io

app = Flask(__name__)


@app.route('/convert', methods=['POST'])
def convert_csv_to_json():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file and file.filename.endswith('.csv'):
            csv_file = file.read().decode('utf-8')
            csv_reader = csv.DictReader(io.StringIO(csv_file))
            data = [row for row in csv_reader]

            response = jsonify(data)
            response.headers['Content-Type'] = 'application/json'
            return response, 200

        return jsonify({'error': 'Invalid file format'}), 400
    except Exception as e:
        return jsonify({'error': 'An internal error occurred'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
