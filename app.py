from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Global variables to store processed data
global_data = {
    'numbers': [],
    'alphabets': [],
    'email': '',
    'name': '',
    'register_number': ''
}

@app.route('/bfhl', methods=['GET'])
def get_message():
    # Return the processed data for GET requests
    return jsonify(global_data)

@app.route('/bfhl', methods=['POST'])
def process_data():
    global global_data
    
    # Get data from the request
    data = request.json
    text_data = data.get('data', '')
    

    # Process the text data
    items = text_data.split(',')
    numbers = [item for item in items if item.isdigit()]
    alphabets = [item for item in items if item.isalpha()]

    # Sort the lists
    numbers.sort(key=int)
    alphabets.sort()

    global_data = {
        'numbers': numbers,
        'alphabets': alphabets,
        'email': 'mamlesh.va06@gmail.come',
        'name': 'Mamlesh VA',
        'register_number': '21BIT0101'
    }

    return jsonify(global_data)

if __name__ == '__main__':
    app.run(debug=True)
