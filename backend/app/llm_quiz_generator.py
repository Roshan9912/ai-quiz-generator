import json
import re
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)

QUIZ_PROMPT = """
You are an educational quiz generator.

STRICT RULES:
- Use ONLY the given article text
- Generate 5–10 MCQs
- Each question MUST include:
  - question
  - options (4)
  - answer
  - difficulty (easy|medium|hard)
  - explanation

OUTPUT FORMAT:
Return ONLY a valid JSON array.
DO NOT include markdown.
DO NOT include explanation text.

ARTICLE:
{content}
"""

TOPIC_PROMPT = """
Suggest 5 related Wikipedia topics based on the article.

Return ONLY a JSON array of strings.

ARTICLE:
{content}
"""

def _safe_json_parse(text: str):
    """
    Extract and parse JSON safely from LLM output
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # try to extract JSON block
        match = re.search(r"(\[.*\])", text, re.DOTALL)
        if match:
            return json.loads(match.group(1))
        raise ValueError("LLM returned invalid JSON")

def generate_quiz(article_text: str):
    prompt = PromptTemplate.from_template(QUIZ_PROMPT)
    response = llm.invoke(prompt.format(content=article_text))
    return _safe_json_parse(response.content)

def generate_related_topics(article_text: str):
    prompt = PromptTemplate.from_template(TOPIC_PROMPT)
    response = llm.invoke(prompt.format(content=article_text))
    return _safe_json_parse(response.content)
