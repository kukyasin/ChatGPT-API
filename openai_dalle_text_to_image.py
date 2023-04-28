import requests
import json

# Replace this with your OpenAI API key
openai_api_key = "your_openai_api_key"
api_url = "https://api.openai.com/v1/images/generations"

# Set up headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

# Define the text prompt you want to generate an image for
prompt = "ejderha yumurtası kırılmaya yakın içerisinde turuncu ışıklar çıkıyor"

# Set up the data for the API request
data = {
    "model": "image-alpha-001",
    "prompt": prompt,
    "num_images": 1,
    "size": "2048x2048",
    "response_format": "url"
}

# Send a POST request to the OpenAI API
response = requests.post(api_url, headers=headers, json=data)

# If the request is successful, print the image URL
if response.status_code == 200:
    image_url = response.json()["data"][0]["url"]
    print(f"Image URL: {image_url}")
# If there's an error, print the error code and error message
else:
    print(f"Error: API request failed. Error code: {response.status_code}, Error message: {response.text}")
