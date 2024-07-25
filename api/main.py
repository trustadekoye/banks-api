from flask import Flask, jsonify, abort

app = Flask(__name__)

banks = [
    {"id": 1, "name": "Access Bank,", "code": "044"},
    {"id": 2, "name": "First Bank of Nigeria", "code": "011"},
    {"id": 3, "name": "Guaranty Trust Bank", "code": "058"}
]

@app.route("/", methods=["GET"])
def get_banks():
    return jsonify(banks)

@app.route("/banks/<int:bank_id>", methods=["GET"])
def get_bank(bank_id):
    bank = next((bank for bank in banks if bank["id"] == bank_id), None)
    if bank is None:
        abort(404, description="Bank not found")
    return jsonify(bank)

if __name__ == "__main__":
    app.run(debug=True)
    