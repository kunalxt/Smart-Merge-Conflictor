import requests

def ai_resolve(head_content, incoming_content):
    prompt = f"""You are a helpful AI that merges Git conflict code.

HEAD version:
{head_content}

INCOMING version:
{incoming_content}

Merge the two versions intelligently into one final version. Keep all necessary logic from both. Do not include conflict markers or any explanations—only output the final merged code.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        result = response.json()
        return result["response"]
    except Exception as e:
        return f"Error during AI merge: {e}"
