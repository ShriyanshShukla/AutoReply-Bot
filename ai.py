from openai import OpenAI

def ai(text):
    client = OpenAI(api_key="Put_Your_Key_here")

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person Shriyansh who speak hindi but can also speak english, you are from india. You analyze chat history and respond like Shriyansh. Don't be super positive be normal and little serious. Output should be the next chat response (text message only) and should not contain [anything in these brackets] and my name"},
        {"role": "user", "content": text}
    ]
)
    return (completion.choices[0].message.content)