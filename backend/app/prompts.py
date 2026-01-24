QUIZ_PROMPT = """
You are an educational quiz generator.

Based ONLY on the content below, generate 5–10 quiz questions.

Each question must include:
- question
- 4 options
- correct answer
- explanation
- difficulty (easy/medium/hard)

Content:
{content}

Respond strictly in JSON.
"""

RELATED_TOPICS_PROMPT = """
Suggest 5 related Wikipedia topics for further reading
based on the topic: {title}

Respond as JSON list.
"""
