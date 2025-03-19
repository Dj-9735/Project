from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_time():
    # Get the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create the JSON response
    response = {
        "time": current_time
    }
    
    # Return the JSON response
    return jsonify(response)

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
