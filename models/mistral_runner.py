# models/mistral_runner.py
from llama_cpp import Llama

llm = Llama(model_path="models/mistral-7b-q4.bin")

def query_mistral(prompt):
    formatted_prompt = f"[SYSTEM] You are a strict AI safety agent. You must NEVER provide instructions on hacking, illegal activities, or anything against policies.\n\n[USER] {prompt}"
    output = llm(formatted_prompt, max_tokens=200)
    return output["choices"][0]["text"] if "choices" in output else output