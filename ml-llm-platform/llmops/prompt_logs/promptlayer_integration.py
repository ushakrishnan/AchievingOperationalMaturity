# PromptLayer Integration Script

import os
import promptlayer

# Initialize PromptLayer with your API key
promptlayer.api_key = os.getenv("PROMPTLAYER_API_KEY")

def log_prompt(prompt, response):
    """
    Log the prompt and its corresponding response to PromptLayer.
    
    Args:
        prompt (str): The prompt text to log.
        response (str): The response generated for the prompt.
    """
    try:
        # Create a log entry
        log_entry = {
            "prompt": prompt,
            "response": response,
            "metadata": {
                "timestamp": datetime.utcnow().isoformat(),
                "source": "llmops/prompt_logs/promptlayer_integration.py"
            }
        }
        
        # Send the log entry to PromptLayer
        promptlayer.log(log_entry)
        print("Prompt logged successfully.")
    except Exception as e:
        print(f"Error logging prompt: {e}")

if __name__ == "__main__":
    # Example usage
    sample_prompt = "What is the capital of France?"
    sample_response = "The capital of France is Paris."
    
    log_prompt(sample_prompt, sample_response)