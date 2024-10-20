from transformers import pipeline

class USCISChatbot:
    def __init__(self, context):
        HUGGINGFACE_TOKEN = "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"
        # Store the manual content as context
        self.context = context
        self.model = pipeline(
            "text-generation",
            model="meta-llama/llama-3.1-8b-instruct", 
            max_length=256,
        )

    def answer_query(self, query):
        """Generates an answer based on the query using the context."""
        prompt = f"Context: {self.context}\nQuestion: {query}\nAnswer:"
           # Generate a response using the pipeline
        response = self.model(prompt)[0]["generated_text"]
        return response.replace(prompt, "").strip()
