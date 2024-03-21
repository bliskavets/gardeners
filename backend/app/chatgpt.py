import openai

client = openai.OpenAI(    
    api_key="secret",
)

def get_completion_text(prompt, temperature=0.7, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    completion = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature
    )
    return completion.choices[0].message.content

