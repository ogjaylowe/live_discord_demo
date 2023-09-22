from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to store JSON objects received via POST requests
data_store = []

@app.route('/get-data', methods=['GET'])
def get_data():
    return jsonify(data_store)

@app.route('/post-data', methods=['POST'])
def post_data():
    try:
        # Get JSON data from the request body
        request_data = request.get_json()
        
        if not request_data:
            return jsonify({"error": "No JSON data provided in the request body"}), 400

        # Store the received JSON data
        data_store.append(request_data)
        
        return jsonify({"message": "Data received and stored successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
