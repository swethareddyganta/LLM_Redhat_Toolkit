# app.py
import streamlit as st
from prompt_engine import generate_prompt
from models.openai_runner import query_openai
from models.mistral_runner import query_mistral
from detectors.regex_detector import detect_vulnerability_regex
from detectors.classifier import detect_vulnerability_classification
from scorer.scorer import compute_risk
import pandas as pd
import time

st.set_page_config(page_title="🛡️ AI Red Teaming Toolkit", layout="wide")

# In-memory history store
if "history" not in st.session_state:
    st.session_state.history = []

# --- Sidebar ---
st.sidebar.title("🧪 Red Team Prompt Config")
model_choice = st.sidebar.selectbox("Choose LLM", ["OpenAI GPT-3.5", "Mistral 7B"])
prompt_type = st.sidebar.selectbox("Attack Type", ["injection", "jailbreak"])
use_custom = st.sidebar.checkbox("Use Custom Prompt")

if use_custom:
    user_prompt = st.sidebar.text_area("✍️ Enter Custom Prompt", height=200)
else:
    user_prompt = generate_prompt(prompt_type)

if st.sidebar.button("Run Red Team Test"):
    with st.spinner("Querying model and analyzing response..."):
        if model_choice == "OpenAI GPT-3.5":
            response = query_openai(user_prompt, model="gpt-3.5-turbo")
        else:
            response = query_mistral(user_prompt)

        # Get classifier and regex analysis
        clf_result = detect_vulnerability_classification(response)
        clf_label = clf_result["label"]
        clf_score = clf_result["score"]
        clf_all = clf_result["scores"]

        regex_flag = detect_vulnerability_regex(response)
        risk = compute_risk(regex_flag, clf_label, clf_score)

        result = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "prompt": user_prompt,
            "model": model_choice,
            "response": response,
            "risk": risk,
            "regex": regex_flag,
            "clf_label": clf_label,
            "clf_score": clf_score,
            "clf_all": clf_all
        }
        st.session_state.history.append(result)

# --- Main UI ---
st.title("🛡️ AI Red Teaming Toolkit")
st.markdown("### 🔍 Model Vulnerability Test")

if st.session_state.history:
    latest = st.session_state.history[-1]

    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("📨 Prompt Sent")
        st.code(latest["prompt"], language="markdown")

        st.subheader("🧠 Model Response")
        st.code(latest["response"])

    with col2:
        st.metric("⚠️ Risk Level", latest["risk"])
        st.metric("Regex Flag", str(latest["regex"]))
        st.metric("Classifier", f"{latest['clf_label']} ({latest['clf_score']:.2f})")

        st.subheader("🔬 Classifier Probabilities")
        st.bar_chart(latest.get("clf_all", {}))

st.markdown("---")
st.subheader("📜 Test History")
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    columns_to_show = ["timestamp", "model", "risk", "clf_label", "clf_score"]
    st.dataframe(df[columns_to_show])
else:
    st.info("No test history yet. Run a test to see results here.")