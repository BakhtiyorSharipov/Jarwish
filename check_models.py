from google import genai
import json
import asyncio

with open('config/api_keys.json', 'r') as f:
    api_key = json.load(f)['gemini_api_key']

client = genai.Client(api_key=api_key)

print("Checking available models that might support audio...\n")

async def test_model(model_name):
    print(f"Testing: {model_name}")
    try:
        # Try to connect to the live API
        async with client.aio.live.connect(model=model_name) as session:
            print(f"✅ {model_name} - WORKS!")
            return True
    except Exception as e:
        err_str = str(e)
        if "not found" in err_str.lower() or "1008" in err_str:
            print(f"❌ {model_name} - Not found or doesn't support live API")
        elif "API key" in err_str:
            print(f"⚠️ {model_name} - API key issue")
        else:
            print(f"⚠️ {model_name} - {err_str[:80]}")
        return False

async def main():
    models = [
        "gemini-2.0-flash-exp",
        "models/gemini-2.0-flash-exp",
        "gemini-2.5-flash-native-audio-preview-12-2025",
        "models/gemini-2.5-flash-native-audio-preview-12-2025",
        "gemini-1.5-pro",
        "models/gemini-1.5-pro",
        "gemini-2.0-flash",
        "models/gemini-2.0-flash",
        "gemini-1.5-flash",
        "models/gemini-1.5-flash",
    ]
    
    print("Testing models for live API support...\n")
    for model in models:
        await test_model(model)

asyncio.run(main())