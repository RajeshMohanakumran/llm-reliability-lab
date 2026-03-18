import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="LLM Reliability Lab", page_icon="🔥")

st.title("🔥 LLM Reliability Lab")
st.caption("Testing LLM vs Actual Logic")

name1 = st.text_input("Enter Name 1")
name2 = st.text_input("Enter Name 2")

if st.button("Run Experiment"):

    if not name1 or not name2:
        st.warning("Please enter both names")
    else:
        with st.spinner("Running experiment..."):

            try:
                response = requests.get(API_URL, params={"name1": name1, "name2": name2})
                data = response.json()

                st.success("Experiment Completed ✅")

                # Actual
                st.subheader("✅ Ground Truth (Python)")
                st.write(data["actual_result"])

                # Naive
                st.subheader("🤖 Naive LLM")
                st.write(data["naive_llm"]["llm_result"])
                st.write("Correct:", data["naive_llm"]["is_correct"])

                # Structured
                st.subheader("⚡ Prompt Engineered LLM")
                st.write(data["structured_llm"]["llm_result"])
                st.write("Correct:", data["structured_llm"]["is_correct"])

            except Exception as e:
                st.error(f"Error: {e}")