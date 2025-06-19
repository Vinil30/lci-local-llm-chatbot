# LCI Local LLM Chatbot

This repository contains the implementation of a lightweight, fully local conversational AI developed as part of the **Local Conversational Intelligence (LCI) assignment**.  
The chatbot uses HuggingFace Transformers and small-scale open-access models to run offline on CPU, with simple memory-based multi-turn dialogue support.

---

## 🎯 Objective

Build a **minimal local chatbot** without relying on external APIs or GPUs.  
Focus: load, run, and chat with an open LLM using only CPU — suitable for constrained systems.

---

## 🚀 Features

- 🧠 **Local Model Inference** using HuggingFace
- 🗨️ **Multi-turn Memory** (remembers last N turns)
- 🖥️ **Offline Execution** (no internet needed after model download)
- 🧩 **Plug-n-Play Model Support** (`phi-1_5`, `distilgpt2`, etc.)
- 🎥 **Demo Video Included** (check `demo_video.mp4`)

---

## 🗂️ Project Structure

lci-local-llm-chatbot/
├── interface.py # Main chatbot interface (CLI)
├── model_loader.py # Loads selected HF model/tokenizer
├── chat_memory.py # Manages memory of last N chat turns
├── requirements.txt # Python dependencies
├── demo_video.mp4 # Video demo for LCI submission
└── README.md # Project documentation


## ⚙️ Setup Instructions

### 1. Clone the Repo:
```bash
git clone https://github.com/yourusername/lci-local-llm-chatbot.git
cd lci-local-llm-chatbot
pip install -r requirements.txt
python interface.py
Chatbot started. Type /exit to quit.
User: what is the capital of France?
Bot: The capital of France is Paris.


Model Used
microsoft/phi-1_5

Lightweight 1.3B parameter transformer
Works well for basic Q&A and instruction following
Runs smoothly on CPU with ~2.8GB RAM usage

Cleanup Tip
rm -rf ~/.cache/huggingface/hub
