def classify_query(query: str) -> str:
    q = query.lower()

    if "where" in q or "file" in q:
        return "file_search"

    if "function" in q or "implemented" in q:
        return "function_search"

    if "how" in q or "explain" in q:
        return "explanation"

    if "dependency" in q or "package" in q:
        return "dependency"

    return "general"