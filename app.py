import streamlit as st

# ----------------------------
# Title Section
# ----------------------------
st.set_page_config(page_title="AI Expert System", page_icon="🧠", layout="centered")

st.title("🧠 AI Expert System Prototype")
st.subheader("Medical Diagnosis using Rule-Based Inference with Uncertainty")

st.write("""
This prototype demonstrates how an **Expert System** works.
It predicts diseases based on symptoms using a **rule-based knowledge base**
and handles **uncertainty using Certainty Factors (CF)**.
""")

st.divider()

# ----------------------------
# Step 1: User Input
# ----------------------------
st.header("Step 1: Enter Symptoms")

st.write("""
Each symptom is assigned a value between **0 and 1** representing its intensity.

Example:
- **0.0** → Symptom not present  
- **0.5** → Mild symptom  
- **1.0** → Strong symptom
""")

fever = st.slider("Fever", 0.0, 1.0, 0.0)
cough = st.slider("Cough", 0.0, 1.0, 0.0)
headache = st.slider("Headache", 0.0, 1.0, 0.0)
body_pain = st.slider("Body Pain", 0.0, 1.0, 0.0)

st.divider()

# ----------------------------
# Step 2: Knowledge Base
# ----------------------------
st.header("Step 2: Knowledge Base (Rules)")

st.write("""
The **knowledge base** contains expert rules that relate symptoms to diseases.

Example rules:
""")

st.code("""
Rule 1: IF Fever AND Cough → Flu (CF = 0.8)

Rule 2: IF Cough AND Headache → Cold (CF = 0.6)

Rule 3: IF Fever AND Body Pain → COVID (CF = 0.9)
""")

st.write("""
Each rule has a **certainty factor (CF)** representing confidence in that rule.
""")

st.divider()

# ----------------------------
# Step 3: Inference Engine
# ----------------------------
st.header("Step 3: Inference Engine")

st.write("""
The **Inference Engine** evaluates rules using the user inputs.

It combines:
- Symptom confidence
- Rule certainty factor

Formula used:
""")

st.code("Final CF = min(symptom values) × Rule CF")

# Calculate certainty values
flu_cf = min(fever, cough) * 0.8
cold_cf = min(cough, headache) * 0.6
covid_cf = min(fever, body_pain) * 0.9

results = {
    "Flu": flu_cf,
    "Cold": cold_cf,
    "COVID": covid_cf
}

st.divider()

# ----------------------------
# Step 4: Diagnosis
# ----------------------------
st.header("Step 4: Diagnosis")

if st.button("Run Diagnosis"):

    disease = max(results, key=results.get)
    confidence = results[disease]

    st.success(f"Most Probable Disease: **{disease}**")
    st.write(f"Confidence Level: **{confidence*100:.2f}%**")

    st.divider()

    # ----------------------------
    # Step 5: Uncertainty Explanation
    # ----------------------------
    st.header("Step 5: Handling Uncertainty")

    st.write("""
This system handles uncertainty using **Certainty Factors**.

Process:
1. Symptoms are entered with confidence values (0–1)
2. Each rule has a certainty factor
3. The inference engine multiplies these values
4. The disease with the highest confidence is selected
""")

    st.divider()

    # ----------------------------
    # Step 6: Visualization
    # ----------------------------
    st.header("Step 6: Probability Visualization")

    st.bar_chart(results)

    st.write("""
The bar chart shows the **probability of each disease** calculated by the expert system.
""")

st.divider()

# ----------------------------
# Footer
# ----------------------------
st.info("""
This prototype demonstrates how AI Expert Systems perform reasoning with uncertainty
using rule-based inference and certainty factors.
""")