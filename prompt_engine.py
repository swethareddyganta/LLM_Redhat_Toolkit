# prompt_engine.py
import random

def load_prompts(file_path):
    with open(file_path, 'r') as f:
        prompts = f.read().split('\n\n')
    return [p.strip() for p in prompts if p.strip()]

def generate_prompt(prompt_type):
    file_map = {
        "injection": "prompts/injection.txt",
        "jailbreak": "prompts/jailbreak.txt"
    }
    prompts = load_prompts(file_map[prompt_type])
    return random.choice(prompts)