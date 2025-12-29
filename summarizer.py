from transformers import pipeline

# Load the summarization pipeline from Hugging Face
summarizer = pipeline("summarization")

def generate_summary(text):
    if not text or len(text.strip()) < 20:
        return "Not enough content to summarize."

    # Limit input size for transformer
    max_input = 1000
    text = text.strip().replace("\n", " ")
    text = text[:max_input]

    try:
        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Summary Error: {str(e)}"
