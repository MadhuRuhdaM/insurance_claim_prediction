from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Rule-based prediction function
def predict_claim_risk(age, gender, policy_type, medical_history, previous_claim):
    score = 0

    # Age-based risk
    if age < 25:
        score += 1   
    elif 25 <= age <= 40:
        score += 2  
    elif 41 <= age <= 60:
        score += 3  
    else: 
        score += 4   # above 60

    # Gender impact
    if gender.lower() == "male":
        score += 2   
    elif gender.lower() == "female":
        score += 1   

    # Policy type impact
    if policy_type.lower() == "premium":
        score += 2   
    elif policy_type.lower() == "basic":
        score += 1  

    # Medical history impact
    if medical_history.lower() == "yes":
        score += 3  
    else:
        score += 1   

    # Previous claim impact
    if previous_claim == 1:
        score += 3   
    else:
        score += 1    

    # Risk categories
    if score <= 6:
        return "Low"
    elif 7 <= score <= 10:
        return "Medium"
    else:
        return "High"

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
    previous_claim = int(data.get("previous_claim", 0))  # 0 = no, 1 = yes

    risk_level = predict_claim_risk(age, gender, policy_type, medical_history, previous_claim)

    return jsonify({"likelihood": risk_level})

if __name__ == "__main__":
    app.run(debug=True)