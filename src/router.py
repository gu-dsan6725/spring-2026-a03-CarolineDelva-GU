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

def route_query(query: str):

    q = query.lower()

    sources = []

    if "sales" in q or "revenue" in q or "total" in q:
        sources.append("csv")

    if "product" in q or "review" in q or "describe" in q:
        sources.append("documents")

    if "find" in q or "mention" in q:
        sources.append("keyword")

    if not sources:
        sources = ["documents"]

    return sources