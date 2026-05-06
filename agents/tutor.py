from openai import OpenAI

client = OpenAI()

def improve_answer(answer):
    prompt = f"""
请给出一个更标准、更适合面试的回答：

{answer}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
