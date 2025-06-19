from transformers import pipeline

def load_model():
    return pipeline(
        "text-generation",
        model="microsoft/phi-1_5",
        framework="pt",
        device=-1,
        max_new_tokens=50,
        temperature=0.7,
        top_k=50,
        repetition_penalty=1.2
    )
