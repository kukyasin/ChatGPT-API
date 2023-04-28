import openai

openai.api_key = "your-api-key"

def generate_answer(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
    )
    answer = response.choices[0].text.strip()
    return answer

while True:
    question = input("Soru: ")
    prompt = f"Soru: {question}\nCevap:"
    answer = generate_answer(prompt)
    print(f"Cevap: {answer}")
