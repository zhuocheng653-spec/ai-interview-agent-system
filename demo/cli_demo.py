from core.orchestrator import run_round

def run_demo():
    print("=== AI 面试模拟系统 ===")

    topic = input("选择主题（Redis/MySQL/Algorithm）：")
    question = "请回答："

    print("\n问题：", question)
    answer = input("你的回答：")

    result = run_round(topic, answer)

    print("\n=== 评分 ===")
    print(result["score"])

    print("\n=== 优化答案 ===")
    print(result["improved_answer"])
