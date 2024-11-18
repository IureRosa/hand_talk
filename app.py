from flask import Flask, request, jsonify
from api.handler import generate_image

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()

        required_fields = ["person", "instrument", "environment", "style"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        image = generate_image(data)

        return jsonify({"image": image}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
