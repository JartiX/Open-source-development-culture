from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def handle_log():
    log_data = request.get_json()
    if log_data:
        print("Received log data:", log_data)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "No data received"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
