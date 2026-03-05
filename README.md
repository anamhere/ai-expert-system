# 🧠 AI Medical Expert System

A **rule-based AI Expert System** built using **Python and Streamlit** that predicts possible diseases based on symptoms using **certainty factor reasoning**.

This project demonstrates how **Artificial Intelligence expert systems** mimic human expert decision-making using a **knowledge base and inference engine**.

---

## 🚀 Live Demo

🌐 **Deployed App:**
https://ai-expert-system-anam.streamlit.app

---

## 📌 Features

* 🧠 Rule-based medical diagnosis
* 📊 Certainty factor reasoning for handling uncertainty
* 🎚 Interactive symptom input using sliders
* 📈 Disease probability visualization
* ⚙ Simple inference engine
* 🌐 Web interface built with Streamlit

---

## 🏥 Diseases Covered

The expert system predicts the following diseases:

* Flu
* Cold
* COVID

The diagnosis is based on symptom combinations and certainty factor rules.

---

## 📚 How the Expert System Works

The system consists of three main components:

### 1️⃣ Knowledge Base

The knowledge base stores rules provided by experts.

Example:

IF Fever AND Cough → Flu (CF = 0.8)
IF Cough AND Headache → Cold (CF = 0.6)
IF Fever AND Body Pain → COVID (CF = 0.9)

---

### 2️⃣ Inference Engine

The inference engine evaluates the rules using user-provided symptoms.

Formula used:

Final CF = min(symptom confidence) × Rule CF

The disease with the **highest certainty factor** is selected.

---

### 3️⃣ User Interface

Users input symptoms through sliders where:

* **0.0** → Symptom not present
* **0.5** → Mild symptom
* **1.0** → Strong symptom

The system then calculates probabilities and shows the most likely disease.

---

## 🛠 Technologies Used

* Python
* Streamlit
* Rule-Based AI
* Certainty Factor Model

---

## 📂 Project Structure

```
ai-expert-system
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶ How to Run Locally

1. Clone the repository

```
git clone https://github.com/anamhere/ai-expert-system.git
```

2. Navigate to the project folder

```
cd ai-expert-system
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the Streamlit app

```
streamlit run app.py
```

---

## ⚠ Disclaimer

This project is a **prototype for educational purposes only** and should not be used for real medical diagnosis.

Always consult a qualified healthcare professional for medical advice.

---

## 👩‍💻 Author

**Anam**

---

## ⭐ Contribution

Contributions, suggestions, and improvements are welcome.

If you like this project, please consider **starring the repository** ⭐ on GitHub.
