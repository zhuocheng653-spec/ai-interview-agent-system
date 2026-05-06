from agents.interviewer import ask_question
from agents.evaluator import evaluate_answer
from agents.tutor import improve_answer

def run_round(topic, user_answer):
    question = ask_question(topic)

    eval_result = evaluate_answer(user_answer)
    improved = improve_answer(user_answer)

    return {
        "question": question,
        "score": eval_result,
        "improved_answer": improved
    }
