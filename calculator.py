import requests # 🚨 The agent needs to detect this is missing!

def get_math_fact():
    # This will fail in the sandbox because 'requests' is not installed
    response = requests.get("http://numbersapi.com/42/math")
    return response.text

print(get_math_fact())
