document.getElementById("predictionForm").addEventListener("submit", async function(e) {
    e.preventDefault(); // prevent form from reloading page

    // Get form values
    const age = document.getElementById("age").value;
    const gender = document.getElementById("gender").value;
    const policy_type = document.getElementById("policy_type").value;
    const medical_history = document.getElementById("medical_history").value;
    const premium = document.getElementById("premium").value;

    // Validate all fields
    if (!age || !gender || !policy_type || !medical_history || !premium) {
        alert("Please fill all fields");
        return;
    }

    // Send data to Flask via AJAX
    const response = await fetch("/predict_ajax", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ age, gender, policy_type, medical_history, premium })
    });

    const data = await response.json();

    // Display result
    document.getElementById("result").innerText = `Claim Probability: ${data.likelihood}%`;
});
