# 🩺 Medical Bot Assistant 💊

A **Medical Question-Answering  platform** using **Retrieval-Augmented Generation (RAG)**. This chatbot answers user questions by retrieving information from trusted medical documents, which are processed into vector representations and stored in a vector database for efficient semantic search. It generates concise responses through a simple chat interface, making medical knowledge more accessible and easier to understand.

---

## Features
- **Real-Time Triage** — Categorizes symptoms into three priority levels.
- **Streaming Interface** — Provides instant feedback with a word-by-word typing effect.
- **Safety First** — Includes automated "Red Flag" detection and emergency action steps.
- **High Performance** — Powered by the Meta Llama-3-8B-Instruct model via the Hugging Face Inference API.
---

## Tech Stack
- **Model** — Llama-3-8B-Instruct (Fine-tuned for medical context)
- **LangChain** — Orchestration framework for managing language model workflows and retrieval pipelines.
- **Language** — Python
- **Frontend** — Streamlit
- **Backend** — Hugging Face Inference API
- **Deployment** — Streamlit Cloud

## How It Works
- **System Prompting** — The model is initialized with a professional "Medical Triage" persona.
- **User Input** — The user describes symptoms (e.g., "I have a sharp pain in my chest").
- **Analysis** — The model evaluates the severity and generates a structured response.
- **Streaming** — Tokens are streamed from Hugging Face to the Streamlit UI for a fast, responsive user experience.

## ⚠️ Disclaimer
This project is for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a physician or other qualified health provider with any questions regarding a medical condition.
