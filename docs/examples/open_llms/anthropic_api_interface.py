import os

from anthropic import Anthropic

# Initialize the Anthropic client with API key
client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# Create a message completion
response = client.messages.create(
    model=os.getenv("MODEL_NAME", "claude-3-5-sonnet-20240620"),
    messages=[
        {
            "role": "user",
            "content": "Provide me with only the code for a simple python function that sums two numbers.",
        },
    ],
    temperature=0.7,
    max_tokens=200,
    stream=False,
)

# Print the response content
print(response.content[0].text)
