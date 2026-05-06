from openai import OpenAI
from rag.retriever import retrieve

client = OpenAI()

def improve_answer(answer):
    context = retrieve(answer)

    prompt = f"""
你是高级面试官，请结合知识库优化回答：

【候选人回答】
{answer}

【参考知识】
{context}

请输出更专业的面试回答
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
