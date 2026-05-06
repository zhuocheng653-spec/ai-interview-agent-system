def ask_question(topic="Redis"):
    questions = {
        "Redis": "Redis 为什么快？",
        "MySQL": "MySQL 如何保证事务一致性？",
        "Algorithm": "请讲一下快速排序的原理"
    }
    return questions.get(topic, "请自我介绍")
