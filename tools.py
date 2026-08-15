import re
import wikipedia
from rag_tool import rag_search

def calculate( expression: str )->str:
    if not re.fullmatch(r"[0-9+\-*/().\s]+", expression ):
        return "Error: Invalid characters in the expression!!"
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"

def wiki_search(query: str)-> str:
    try:
        return wikipedia.summary(query, sentences = 3)
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for '{query}'"
    except Exception as e:
        return f"Error: {e}"

TOOLS = {
    "calculate": calculate,
    "wikipedia": wiki_search,
    "rag_search": rag_search
}
