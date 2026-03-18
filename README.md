# 🔥 LLM Reliability Lab

> Can LLMs handle simple logic correctly?

---

## 🚀 Overview

Large Language Models are powerful…  
but are they *reliable*?

This project explores how LLMs behave on **deterministic problems** by comparing their output with actual algorithmic logic.

---

## 🧠 What This Project Does

Given an input (e.g., two names for FLAMES):

- 🤖 LLM generates a response  
- ✅ Python computes the correct result  
- ⚖️ System compares both  
- 📊 Shows whether the LLM is right or wrong  

---

## 🔬 Experiment

We test LLM performance using:

### ❌ Naive Prompt
- Simple instruction  
- High chance of incorrect output  

### ⚡ Prompt Engineered
- Step-by-step structured prompt  
- Improved accuracy  

### ✅ Ground Truth
- Python-based deterministic logic  
- Always correct  

---

## 📊 Key Insight

> LLMs can sound confident… even when they are wrong.

Prompt engineering helps —  
but **does not guarantee correctness**.

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **LLM:** Groq (LLaMA3)  
- **Language:** Python  

---

## ⚙️ How It Works

1. User enters input  
2. LLM predicts result  
3. Python calculates actual result  
4. System compares both  

---

## 🧪 Example

| Source              | Result     | Correct |
|--------------------|-----------|--------|
| Python Logic        | Marriage  | ✅     |
| Naive LLM           | Love      | ❌     |
| Prompt Engineered   | Marriage  | ✅     |

---

## 🧠 Why This Matters

Most projects:
- Use LLMs blindly  

This project:
- Evaluates LLM behavior  
- Detects hallucinations  
- Demonstrates hybrid AI design  

---

## 🔥 Key Learning

> LLMs are probabilistic, not deterministic.

Best approach:
👉 Combine **LLM + rule-based systems**

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
cd backend
uvicorn main:app --reload
cd ../frontend
streamlit run app.py