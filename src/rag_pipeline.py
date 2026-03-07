from src.router import route_query
from src.csv_retriever import retrieve_sales_info
from src.doc_retriever import retrieve_docs
from src.keyword_retriever import keyword_search
from src.combine import combine_context
from src.llm import generate_answer


def answer_query(query):

    sources = route_query(query)

    contexts = []

    if "csv" in sources:
        contexts.append(retrieve_sales_info(query))

    if "documents" in sources:
        contexts.append(retrieve_docs(query))

    if "keyword" in sources:
        contexts.append(keyword_search(query))

    context = combine_context(contexts)

    answer = generate_answer(query, context)

    return answer