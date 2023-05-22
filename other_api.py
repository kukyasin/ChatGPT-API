import openai

# Set your OpenAI API key here
openai.api_key = 'api-key'

def chat_with_bot(message):
    response = openai.Completion.create(
        engine='curie',
        prompt=message,
        max_tokens=1,
        temperature=0.9,
        n=1,
        stop=None,
    )

    if len(response.choices) > 0:
        return response.choices[0].text.strip()
    else:
        return "Sorry, I couldn't generate a response."

# Get user input and interact with the chatbot
while True:
    user_input = input("User: ")
    response = chat_with_bot(user_input)
    print("Chatbot:", response)
