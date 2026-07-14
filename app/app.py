# ==========================================================
# Customer Churn Prediction Web Application
# ==========================================================

from flask import Flask, render_template, request
import numpy as np
import joblib

# ==========================================================
# Create Flask App
# ==========================================================

app = Flask(__name__)

# ==========================================================
# Load Saved Model
# ==========================================================

try:
    model = joblib.load("../models/churn_prediction_model.pkl")
    scaler = joblib.load("../models/scaler.pkl")

    print("✅ Model Loaded Successfully")

except Exception as e:

    print("❌ Error Loading Model")
    print(e)


# ==========================================================
# Home Route
# ==========================================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================================
# Prediction Route
# ==========================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ===========================
        # Read User Inputs
        # ===========================

        credit_score = float(request.form["credit_score"])
        country = float(request.form["country"])
        gender = float(request.form["gender"])
        age = float(request.form["age"])
        tenure = float(request.form["tenure"])
        balance = float(request.form["balance"])
        products_number = float(request.form["products_number"])
        credit_card = float(request.form["credit_card"])
        active_member = float(request.form["active_member"])
        estimated_salary = float(request.form["estimated_salary"])

        # ===========================
        # Input Validation
        # ===========================

        if not (300 <= credit_score <= 900):
            return render_template(
                "index.html",
                error="Credit Score must be between 300 and 900."
            )

        if not (18 <= age <= 100):
            return render_template(
                "index.html",
                error="Age must be between 18 and 100."
            )

        if not (0 <= tenure <= 10):
            return render_template(
                "index.html",
                error="Tenure must be between 0 and 10."
            )

        if balance < 0:
            return render_template(
                "index.html",
                error="Balance cannot be negative."
            )

        if estimated_salary < 0:
            return render_template(
                "index.html",
                error="Estimated Salary cannot be negative."
            )

        # ===========================
        # Prepare Input
        # ===========================

        customer = np.array([[
            credit_score,
            country,
            gender,
            age,
            tenure,
            balance,
            products_number,
            credit_card,
            active_member,
            estimated_salary
        ]])

        # Scale Input
        customer = scaler.transform(customer)

        # ===========================
        # Prediction
        # ===========================

        prediction = model.predict(customer)[0]

        probability = model.predict_proba(customer)[0][1]
        probability = round(probability * 100, 2)

        # ===========================
        # Prediction Result
        # ===========================

        if prediction == 1:
            result = "⚠ Customer is likely to Churn"
        else:
            result = "✅ Customer is likely to Stay"

        # ===========================
        # Risk Level
        # ===========================

        if probability >= 80:

            risk = "Very High Risk"
            risk_color = "#b91c1c"

            recommendation = (
                "Immediately contact the customer, "
                "assign a relationship manager and "
                "offer premium retention benefits."
            )

        elif probability >= 60:

            risk = "High Risk"
            risk_color = "#dc2626"

            recommendation = (
                "Offer loyalty rewards, cashback offers "
                "and proactive customer support."
            )

        elif probability >= 40:

            risk = "Medium Risk"
            risk_color = "#f59e0b"

            recommendation = (
                "Provide personalized banking offers "
                "and increase customer engagement."
            )

        else:

            risk = "Low Risk"
            risk_color = "#16a34a"

            recommendation = (
                "Customer appears satisfied. "
                "Continue premium banking experience."
            )

        # ===========================
        # Render Result
        # ===========================

        return render_template(

            "index.html",

            prediction=result,

            probability=probability,

            risk=risk,

            risk_color=risk_color,

            recommendation=recommendation

        )

    except Exception as e:

        return render_template(

            "index.html",

            error=f"Unexpected Error: {e}"

        )


# ==========================================================
# Run Flask App
# ==========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )