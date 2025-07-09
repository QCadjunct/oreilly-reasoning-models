#!/usr/bin/env python3
"""
Robust test of Ollama with both Python client and direct requests
"""
import ollama
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
OLLAMA_URLS = [
    'http://localhost:11434',
    'http://172.30.79.213:11434'
]

MODEL_NAME = 'deepseek-r1:14b'

def test_direct_requests():
    """Test using direct HTTP requests (more reliable)"""
    print("🔍 Testing direct HTTP requests...")
    
    for url in OLLAMA_URLS:
        print(f"   Trying: {url}")
        try:
            # Test connection
            response = requests.get(f"{url}/api/tags", timeout=5)
            if response.status_code == 200:
                models_data = response.json()
                models = models_data.get('models', [])
                model_names = [model.get('name', 'unnamed') for model in models]
                
                print(f"   ✅ Connected! Found {len(models)} models")
                
                if MODEL_NAME in model_names:
                    print(f"   ✅ {MODEL_NAME} available")
                    return url
                else:
                    print(f"   ❌ {MODEL_NAME} not in: {model_names[:3]}...")
            else:
                print(f"   ❌ HTTP {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    return None

def test_direct_generate(base_url):
    """Test generate using direct HTTP"""
    print(f"\n🧪 Testing direct generate call...")
    
    payload = {
        "model": MODEL_NAME,
        "prompt": "Hello! What's 2+2? Give a brief answer.",
        "stream": False
    }
    
    try:
        response = requests.post(f"{base_url}/api/generate", json=payload, timeout=30)
        if response.status_code == 200:
            result = response.json()
            answer = result.get('response', 'No response')
            print(f"✅ DeepSeek says: {answer}")
            return True
        else:
            print(f"❌ Generate failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_ollama_client(base_url):
    """Test the Ollama Python client"""
    print(f"\n🔍 Testing Ollama Python client...")
    
    try:
        client = ollama.Client(host=base_url)
        
        # Try different methods to check models
        try:
            # Method 1: list()
            models = client.list()
            print(f"   ✅ client.list() worked")
            return client
        except Exception as e1:
            print(f"   ❌ client.list() failed: {e1}")
            
            try:
                # Method 2: Try a direct generate call
                response = client.generate(
                    model=MODEL_NAME,
                    prompt="Hi",
                    stream=False
                )
                print(f"   ✅ client.generate() worked")
                return client
            except Exception as e2:
                print(f"   ❌ client.generate() failed: {e2}")
                return None
                
    except Exception as e:
        print(f"   ❌ Client creation failed: {e}")
        return None

def test_ollama_generate(client):
    """Test generate with Ollama client"""
    print(f"\n🧪 Testing Ollama client generate...")
    
    try:
        response = client.generate(
            model=MODEL_NAME,
            prompt="What's the capital of France? Brief answer please.",
            stream=False
        )
        
        answer = response.get('response', 'No response')
        print(f"✅ Ollama client says: {answer}")
        return True
        
    except Exception as e:
        print(f"❌ Ollama generate error: {e}")
        return False

def main():
    print("🚀 Robust Ollama Test")
    print("=" * 50)
    
    # Test 1: Direct HTTP requests (most reliable)
    working_url = test_direct_requests()
    
    if not working_url:
        print("\n❌ No working Ollama connection found")
        return
    
    print(f"\n✅ Working URL found: {working_url}")
    
    # Test 2: Direct HTTP generate
    if test_direct_generate(working_url):
        print("✅ Direct HTTP generate works")
    else:
        print("❌ Direct HTTP generate failed")
        return
    
    # Test 3: Ollama Python client
    client = test_ollama_client(working_url)
    
    if client:
        print("✅ Ollama Python client connected")
        
        # Test 4: Ollama client generate
        if test_ollama_generate(client):
            print("✅ Ollama client generate works")
        else:
            print("⚠️  Ollama client connected but generate failed")
    else:
        print("⚠️  Ollama Python client failed, but direct HTTP works")
    
    print(f"\n🎉 Summary:")
    print(f"   Working URL: {working_url}")
    print(f"   Direct HTTP: ✅ Working")
    print(f"   Ollama Client: {'✅ Working' if client else '❌ Failed'}")
    
    # Create .env file
    env_content = f"""# Ollama Configuration
OLLAMA_URL={working_url}
OLLAMA_MODEL={MODEL_NAME}

# API Endpoints
OLLAMA_GENERATE_ENDPOINT={working_url}/api/generate
OLLAMA_CHAT_ENDPOINT={working_url}/api/chat
OLLAMA_TAGS_ENDPOINT={working_url}/api/tags

# Settings
OLLAMA_TIMEOUT=30
OLLAMA_STREAM=true
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print(f"✅ Created .env file with working configuration")

if __name__ == "__main__":
    main()