from flask import Flask, jsonify, request, render_template
import json
from validators.rules import run_all_validations

app = Flask(__name__)

# Load sample deals data
def load_deals():
    with open('data/sample_deals.json') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate_deals():
    data = request.get_json()
    results = []

    for deal in data:
        errors = run_all_validations(deal)
        if errors:
            results.append({'deal_id': deal['id'], 'status': 'Invalid', 'errors': errors})
        else:
            results.append({'deal_id': deal['id'], 'status': 'Valid'})

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)