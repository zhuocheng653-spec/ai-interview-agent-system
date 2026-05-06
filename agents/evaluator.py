from openai import OpenAI

client = OpenAI()

def evaluate_answer(answer):
    prompt = f"""
你是大厂面试官，请评价候选人回答：

{answer}

输出 JSON：
{{
  "score": 0-10,
  "problems": ["问题1"],
  "suggestions": ["建议1"]
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
