import requests # 🚨 This is not in requirements.txt!
import pandas
def fetch_data():
    # This will fail in the sandbox until the agent "Heals" it
    r = requests.get("https://api.github.com")
    return r.status_code

print(f"Status: {fetch_data()}")
