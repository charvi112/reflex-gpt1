import requests

def get_llm_response(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"  # Ollama's local endpoint
    payload = {
        "model": "llama3",  # or mistral, gemma, etc. (must match what you've pulled in Ollama)
        "prompt": prompt,
        "stream": False  # important! if True, it returns a streaming response
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response received from Ollama.")
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
