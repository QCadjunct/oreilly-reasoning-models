#!/usr/bin/env python3
"""
Test script for connecting to Ollama running in WSL2 from Windows
"""
import socket
import subprocess
import requests
import json
import os

def get_wsl_ip():
    """Get the IP address of WSL2 from Windows"""
    try:
        # Method 1: Using hostname command
        result = subprocess.run(['wsl', 'hostname', '-I'], capture_output=True, text=True)
        if result.returncode == 0:
            ip = result.stdout.strip().split()[0]  # Get first IP
            return ip
    except:
        pass
    
    return None

def test_ollama_urls():
    """Test various URLs to connect to Ollama"""
    
    # Get WSL IP
    wsl_ip = get_wsl_ip()
    print(f"🔍 Detected WSL2 IP: {wsl_ip}")
    
    # URLs to test
    test_urls = [
        'http://localhost:11434',           # Windows localhost (if port forwarded)
        'http://127.0.0.1:11434',           # Windows loopback
    ]
    
    if wsl_ip:
        test_urls.insert(0, f'http://{wsl_ip}:11434')  # WSL2 IP (most likely to work)
    
    working_urls = []
    
    for url in test_urls:
        print(f"\n🔍 Testing: {url}")
        try:
            response = requests.get(f"{url}/api/tags", timeout=3)
            if response.status_code == 200:
                print(f"✅ SUCCESS! Connected to {url}")
                models = response.json()
                print(f"   Found {len(models.get('models', []))} models")
                working_urls.append(url)
            else:
                print(f"❌ HTTP {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"❌ Connection refused")
        except requests.exceptions.Timeout:
            print(f"❌ Timeout")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    return working_urls

def test_deepseek_chat(base_url):
    """Test a simple chat with DeepSeek-R1"""
    print(f"\n🧪 Testing DeepSeek-R1:14b chat on {base_url}")
    
    payload = {
        "model": "deepseek-r1:14b",
        "prompt": "Hello! Please just respond with 'Hi there!' and nothing else.",
        "stream": False
    }
    
    try:
        response = requests.post(f"{base_url}/api/generate", json=payload, timeout=30)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ DeepSeek Response: {result.get('response', 'No response')}")
            return True
        else:
            print(f"❌ Generate failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error testing chat: {e}")
        return False

def create_env_file(working_url):
    """Create .env file with working URL"""
    env_content = f"""# Ollama Configuration
OLLAMA_URL={working_url}
OLLAMA_MODEL=deepseek-r1:14b

# API Endpoints  
OLLAMA_GENERATE_ENDPOINT={working_url}/api/generate
OLLAMA_CHAT_ENDPOINT={working_url}/api/chat
OLLAMA_TAGS_ENDPOINT={working_url}/api/tags

# Optional: Timeout settings (in seconds)
OLLAMA_TIMEOUT=30
OLLAMA_STREAM=true
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print(f"✅ Created .env file with working URL: {working_url}")

def main():
    print("🚀 Windows to WSL2 Ollama Connection Test")
    print("=" * 50)
    
    # Test URLs
    working_urls = test_ollama_urls()
    
    if working_urls:
        best_url = working_urls[0]
        print(f"\n✅ Found {len(working_urls)} working URL(s)")
        print(f"🎯 Using: {best_url}")
        
        # Test DeepSeek chat
        if test_deepseek_chat(best_url):
            # Create .env file
            create_env_file(best_url)
            
            print(f"\n🎉 SUCCESS! Everything is working!")
            print(f"Your .env file has been created with the correct URL.")
        else:
            print(f"\n⚠️  Connection works but DeepSeek-R1 test failed")
    else:
        print(f"\n❌ Could not connect to Ollama in WSL2")
        print(f"Make sure Ollama is running in WSL2: wsl ollama serve")

if __name__ == "__main__":
    main()