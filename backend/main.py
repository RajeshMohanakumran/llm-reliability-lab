from fastapi import FastAPI
from flames import calculate_flames
from llm import get_llm_response
from evaluator import evaluate

app = FastAPI(title="LLM Reliability Lab")


@app.get("/")
def home():
    return {"message": "API running 🚀"}


@app.get("/predict")
def predict(name1: str, name2: str):

    actual = calculate_flames(name1, name2)

    llm_naive = get_llm_response(name1, name2, "naive")
    llm_structured = get_llm_response(name1, name2, "structured")

    eval_naive = evaluate(llm_naive, actual)
    eval_structured = evaluate(llm_structured, actual)

    return {
        "actual_result": actual,
        "naive_llm": eval_naive,
        "structured_llm": eval_structured
    }