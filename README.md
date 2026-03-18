# 🔥 LLM Reliability Lab

A project to evaluate how reliable LLMs are on deterministic tasks.

## 🚀 Features
- Compare LLM vs actual logic
- Prompt engineering evaluation
- Detect hallucinations
- FLAMES-based experiment

## 🧠 Tech Stack
- FastAPI
- Streamlit
- Groq (LLM)

## ⚙️ How It Works
1. User input → names
2. LLM generates result
3. Python computes actual result
4. System compares both

## 🎯 Key Insight
LLMs can sound confident but fail at simple logical tasks.

## ▶️ Run Locally
```bash
pip install -r requirements.txt
cd backend
uvicorn main:app --reload
cd ../frontend
streamlit run app.py