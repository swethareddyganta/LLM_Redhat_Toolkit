# AI Red Teaming Toolkit — LLM Security Vulnerability Detector

## Overview

The AI Red Teaming Toolkit provides a systematic framework for testing the security and robustness of Large Language Models (LLMs) against adversarial attacks, such as prompt injection, jailbreaks, and behavior drift.

Designed for Red Teams, LLM operations teams, and Responsible AI units, it enables scalable, automated vulnerability discovery prior to model deployment.

## Key Features

- Attack prompt generation (prompt injection, jailbreak scenarios)  
- Risky output detection (regex matching and zero-shot classification)  
- Structured risk scoring (Low, Medium, High)  
- Real-time visualization through a Streamlit dashboard  
- Support for API-based models (OpenAI GPT-3.5) and local models (Mistral 7B via llama.cpp)  
- History tracking of attacks and risk outcomes  
- Docker packaging option for reproducibility  

## Methodology

The toolkit applies an automated evaluation pipeline:

1. **Prompt Attack Simulation**  
   Generate adversarial prompts using curated templates designed to elicit unauthorized behaviors.

2. **Model Querying**  
   Send the generated prompts to either an OpenAI API model (GPT-3.5) or a local Mistral 7B instance via llama.cpp.

3. **Response Analysis**  
   Analyze model responses using:
   - Regex patterns for immediate detection of explicit risk signals (e.g., passwords, hacking instructions)  
   - Zero-shot classification (via BART-based model) to categorize responses into Safe, Sensitive, Dangerous, or Harmful

4. **Risk Scoring**  
   Assign a risk level (Low, Medium, High) based on the combined analysis results.

5. **Visualization and Reporting**  
   Display attack vectors, model outputs, risk scores, and classification breakdowns in a live dashboard, with session-based history logging.

    ![architecture](https://github.com/user-attachments/assets/103afb2b-3bb2-453f-972b-fb77ec37aa23)

## Outputs Displayed

- Attack prompt text  
- Full model response  
- Regex-based risk detection flags  
- Classifier-predicted response category and confidence scores  
- Computed risk level (Low, Medium, High)  
- Historical session logs for review or export  

## Use Cases

- **Adversarial Red Teaming**: Stress-test models before public release.  
- **Continuous LLMops Security**: Integrate into model validation pipelines.  
- **Audit and Compliance Reporting**: Produce risk documentation for AI governance.  
- **Fine-tuning Monitoring**: Detect regression in model safety post-training.  

## Technology Stack

- OpenAI API (gpt-3.5-turbo)  
- Hugging Face Transformers (zero-shot classification)  
- Streamlit (dashboard and interaction layer)  
- Llama.cpp (for local Mistral 7B inference)  
- Python 3.10+  
- Docker (for optional containerization)

## Expected output:
<img width="1470" alt="Screenshot 2025-04-27 at 11 44 41 AM" src="https://github.com/user-attachments/assets/bda34402-c52f-4bd1-b40e-db47999d0f2c" />


