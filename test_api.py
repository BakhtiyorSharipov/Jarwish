from google import genai
import json

try:
    with open('config/api_keys.json', 'r') as f:
        config = json.load(f)
        api_key = config['gemini_api_key']
    
    client = genai.Client(api_key=api_key)
    print("✅ API key is valid!")
    print(f"API key starts with: {api_key[:10]}...")
    
except FileNotFoundError:
    print("❌ config/api_keys.json not found!")
except KeyError:
    print("❌ 'gemini_api_key' not found in config file!")
except Exception as e:
    print(f"❌ Error: {e}")