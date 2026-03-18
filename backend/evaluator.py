def evaluate(llm_output, actual_output):
    llm_clean = llm_output.lower().strip()
    actual_clean = actual_output.lower().strip()

    return {
        "llm_result": llm_output,
        "actual_result": actual_output,
        "is_correct": llm_clean == actual_clean
    }