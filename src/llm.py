from transformers import pipeline

class LLM:
    def __init__(self, model_name="gpt2"):
        # Load the text-generation pipeline
        self.generator = pipeline("text-generation", model=model_name)

    def generate(self, prompt: str, max_length: int = 50, num_return_sequences: int = 1):
        try:
            # Generate text based on the prompt
            responses = self.generator(prompt, max_length=max_length, num_return_sequences=num_return_sequences)
            return [response["generated_text"] for response in responses]
        except Exception as e:
            raise RuntimeError(f"LLM Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    llm = LLM()
    print(llm.generate("Once upon a time", max_length=30))
