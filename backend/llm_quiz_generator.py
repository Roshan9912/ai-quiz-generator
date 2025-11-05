import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from models import QuizOutput

def get_prompt_template():
    return """
Given the following Wikipedia article, generate a quiz JSON with:
- 5-10 questions
- Each question with: text, four options, correct answer, explanation, difficulty level
- key_entities (people, organizations, locations)
- summary
- list of section titles (from headings)
- related Wikipedia topics

Output structure:
{format_instructions}

===ARTICLE TITLE===
{title}
===ARTICLE CONTENT===
{text}
"""

def generate_quiz_with_llm(title, text, sections):
    GOOGLE_API_KEY = os.environ["GEMINI_API_KEY"]
    model = GoogleGenerativeAI(api_key=GOOGLE_API_KEY, model="gemini-2.5-flash")
    prompt = PromptTemplate(
        input_variables=["title", "text", "format_instructions"],
        template=get_prompt_template())
    parser = JsonOutputParser(pydantic_schema=QuizOutput)
    chain = prompt | model | parser
    res = chain.invoke({"title": title, "text": text, "format_instructions": parser.get_format_instructions()})
    res['sections'] = sections
    return res
