import os

DOC_PATH = "../data/unstructured"


def keyword_search(query):

    results = []

    for file in os.listdir(DOC_PATH):

        with open(os.path.join(DOC_PATH, file)) as f:
            lines = f.readlines()

            for line in lines:
                if query.lower() in line.lower():
                    results.append(line)

    return "\n".join(results[:20])