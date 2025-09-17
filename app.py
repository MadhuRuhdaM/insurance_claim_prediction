from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Rule-based prediction function
def predict_claim_probability(age, gender, policy_type, medical_history, premium):
    score = 0
    if age > 50:
        score += 20
    if gender.lower() == "male":
        score += 10
    if policy_type.lower() == "premium":
        score += 30
    elif policy_type.lower() == "basic":
        score += 10
    if medical_history.lower() == "yes":
        score += 25
    if premium > 50000:
        score += 15
    return min(100, score)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# AJAX prediction route
@app.route("/predict_ajax", methods=["POST"])
def predict_ajax():
    data = request.get_json()

    age = int(data.get("age", 0))
    gender = data.get("gender", "")
    policy_type = data.get("policy_type", "")
    medical_history = data.get("medical_history", "")
    premium = float(data.get("premium", 0))

    probability = predict_claim_probability(age, gender, policy_type, medical_history, premium)

    return jsonify({"likelihood": probability})

if __name__ == "__main__":
    app.run(debug=True)
