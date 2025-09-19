
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def predict_claim_risk(age, gender, policy_type, medical_history, previous_claim, premium_amount):
    score = 0

    if age < 25:
        score += 1
    elif 25 <= age <= 40:
        score += 2
    elif 41 <= age <= 60:
        score += 3
    else:
        score += 4

    if gender.lower() == "male":
        score += 2
    elif gender.lower() == "female":
        score += 1

    if policy_type.lower() == "premium":
        score += 2
    elif policy_type.lower() == "basic":
        score += 1

    if medical_history.lower() == "yes":
        score += 3
    else:
        score += 1

    if previous_claim == 1:
        score += 3
    else:
        score += 1

    if premium_amount < 5000:
        score += 1
    elif 5000 <= premium_amount <= 20000:
        score += 2
    else:
        score += 3

    if score <= 7:
        return "Low"
    elif 8 <= score <= 12:
        return "Medium"
    else:
        return "High"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_ajax", methods=["POST"])
def predict_ajax():
    data = request.get_json()
    age = int(data.get("age", 0))
    gender = data.get("gender", "")
    policy_type = data.get("policy_type", "")
    medical_history = data.get("medical_history", "")
    previous_claim = int(data.get("previous_claim", 0))
    premium_amount = int(data.get("premium_amount", 0))
    risk_level = predict_claim_risk(age, gender, policy_type, medical_history, previous_claim, premium_amount)
    return jsonify({"likelihood": risk_level})

if __name__ == "__main__":
    app.run(debug=True)