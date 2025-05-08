import os

import google.generativeai as genai

# Configure the Google Generative AI client with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel(
    model_name=os.getenv("MODEL_NAME", "gemini-pro"),
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 200,
        "top_p": 1.0,
    }
)

# Create a content generation
response = model.generate_content(
    contents=[
        "Provide me with only the code for a simple python function that sums two numbers."
    ]
)

# Print the response text
print(response.text)
