import requests

RAG_API_URL = "http://localhost:8000/ask"

def rag_search(query: str)->str:
    try:
        response = requests.post(
            RAG_API_URL,
            json = {"query": query, "top_k": 3},
            timeout = 15
        )
        data = response.json()
        answer = data["answer"]
        grounded = data["is_grounded"]

        if not grounded:
            return f"(Warning: answer may not be well-grounded in the documents) {answer}"
        return answer
    except Exception as e:
        return f"Error calling rag services: {e}"