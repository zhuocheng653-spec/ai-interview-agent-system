# AI Interview Agent System (RAG Enhanced)

一个基于 **多 Agent + RAG（检索增强生成）** 的后端面试训练系统，模拟大厂面试流程，提供动态追问、评分反馈与知识增强。

---

## 🚀 项目亮点（核心卖点）

* ✅ 多 Agent 协作（面试官 / 评估 / 教学 / 规划）
* ✅ RAG 知识增强（Embedding + 向量检索）
* ✅ 动态追问（模拟真实面试）
* ✅ 工程结构清晰（非简单 Demo）

---

## 🧠 项目背景

传统刷题/八股存在：

* 无反馈
* 无体系
* 无法模拟真实面试

本项目通过 AI Agent + RAG 构建一个“强化学习闭环”：

> 提问 → 回答 → 评估 → 知识补全 → 路径优化

---

## 🏗️ 系统架构

```
User
  ↓
Interviewer Agent（提问）
  ↓
Evaluator Agent（评分）
  ↓
Retriever（RAG检索）
  ↓
Tutor Agent（知识增强生成）
  ↓
Planner Agent（调整学习路径）
```

---

## 🔍 RAG 机制（重点）

系统引入检索增强生成（RAG）：

1. 将面试知识（Redis / MySQL 等）写入知识库
2. 使用 embedding 转换为向量
3. 用户回答时进行语义检索
4. 将相关知识注入 Prompt

👉 提升回答质量与专业度

---

## 📁 项目结构

```
ai-interview-agent-system/
│
├── agents/
│   ├── interviewer.py
│   ├── evaluator.py
│   ├── tutor.py        # ✅ RAG增强
│   └── planner.py
│
├── core/
│   ├── orchestrator.py
│   └── router.py
│
├── rag/                # ✅ 新增模块
│   ├── embedder.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── knowledge_base.txt
│
├── memory/
├── demo/
│   └── cli_demo.py
│
├── main.py
└── requirements.txt
```

---

## 💻 快速运行

### 1️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

### 2️⃣ 配置 API Key

```bash
export OPENAI_API_KEY=your_key
```

### 3️⃣ 运行

```bash
python main.py
```

---

## 📊 示例效果

```
Q: MySQL 如何保证事务一致性？

A: redo log + binlog

系统输出：
- 评分：7/10
- 问题：缺少两阶段提交
- 优化答案：完整结构化回答
```

---

## 🛠️ 技术栈

* Python
* OpenAI API
* Numpy（向量计算）
* RAG（Embedding + 检索）

---

## 📈 技术总结

> 本项目通过 embedding + 向量检索实现 RAG，将面试知识结构化存储。在回答阶段进行语义召回，并将上下文注入 Prompt，从而提升回答的准确性和深度。

---


---

## ⭐ 后续优化方向

* 引入向量数据库（FAISS）
* 多轮对话记忆（Memory）
* Web UI（可视化面试系统）

---

如果这个项目对你有帮助，欢迎 Star ⭐

