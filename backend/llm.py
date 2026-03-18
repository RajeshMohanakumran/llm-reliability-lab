from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def get_llm_response(name1, name2, mode="naive"):
    try:
        if mode == "naive":
            prompt = f"Calculate FLAMES for {name1} and {name2}"

        else:
            prompt = f"""
You are a strict algorithm executor.

Task: Compute FLAMES for two names.

Names: {name1}, {name2}

Steps:
1. Remove common letters
2. Count remaining letters
3. Perform FLAMES elimination step-by-step

Return ONLY final result word (Friends, Love, etc.)
Do NOT explain.
Do NOT guess.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"