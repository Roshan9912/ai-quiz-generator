from urllib.parse import urlparse

def validate_wikipedia_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
        return (
            parsed.scheme in ["http", "https"]
            and "wikipedia.org/wiki/" in parsed.netloc + parsed.path
        )
    except:
        return False

def normalize_quiz_output(llm_output):
    """
    Normalize different LLM quiz formats into a list of questions
    """
    if isinstance(llm_output, list):
        return llm_output

    if isinstance(llm_output, dict):
        if "quiz" in llm_output:
            if isinstance(llm_output["quiz"], list):
                return llm_output["quiz"]
            if isinstance(llm_output["quiz"], dict):
                return llm_output["quiz"].get("questions", [])

        if "questions" in llm_output:
            return llm_output["questions"]

    return []
