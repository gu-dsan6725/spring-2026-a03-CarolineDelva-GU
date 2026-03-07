import os

DOC_PATH = "../data/unstructured"


def retrieve_docs(query):

    results = []

    for file in os.listdir(DOC_PATH):

        with open(os.path.join(DOC_PATH, file)) as f:
            text = f.read()

            if any(word in text.lower() for word in query.lower().split()):

                results.append(text[:500])

    return "\n\n".join(results[:3])