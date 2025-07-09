import ollama

# Test both URLs
urls = ['http://localhost:11434', 'http://127.0.0.1:11434']

for url in urls:
    try:
        client = ollama.Client(host=url)
        models = client.list()
        print(f"✅ {url} - Works! Found {len(models.get('models', []))} models")
        working_url = url
        break
    except Exception as e:
        print(f"❌ {url} - Failed: {e}")

# Use the working URL
client = ollama.Client(host=working_url)
print(f"🤖 Using: {working_url}")