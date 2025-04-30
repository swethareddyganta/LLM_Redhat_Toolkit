# run_red_team.py
import argparse
from prompt_engine import generate_prompt
from models.openai_runner import query_openai
from detectors.regex_detector import detect_vulnerability_regex
from detectors.classifier import detect_vulnerability_classification
from scorer.scorer import compute_risk

def main(model, prompt_type):
    prompt = generate_prompt(prompt_type)
    print(f"\n🔍 Testing prompt: {prompt}\n")
    response = query_openai(prompt)
    print(f"📨 Response:\n{response}\n")

    regex_flag = detect_vulnerability_regex(response)
    clf_label, clf_score = detect_vulnerability_classification(response)
    risk = compute_risk(regex_flag, clf_label, clf_score)

    print(f"⚠️ Risk Level: {risk}")
    print(f"🔍 Classifier: {clf_label} ({clf_score:.2f})")
    print(f"🔍 Regex Detected: {regex_flag}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="openai", help="Model to use")
    parser.add_argument("--prompt_type", default="injection", help="Prompt type")
    args = parser.parse_args()
    main(args.model, args.prompt_type)