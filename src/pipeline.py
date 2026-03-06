from router import classify_query
from bash_tools import run_command
from bash_tools import select_tool
from llm import generate_answer


import logging
from router import classify_query
from bash_tools import select_tool, run_command
from llm import generate_answer

logging.basicConfig(level=logging.INFO)


def answer_question(question: str):

    logging.info(f"QUESTION: {question}")

    logging.info("Step 1: Classifying query")
    query_type = classify_query(question)
    logging.info(f"Query type: {query_type}")

    logging.info("Step 2: Selecting bash command")
    command = select_tool(query_type, question)
    logging.info(f"Command: {command}")

    logging.info("Step 3: Running bash command")
    context = run_command(command)
    logging.info(f"Context length: {len(context)} characters")

    logging.info("Step 4: Calling LLM")
    answer = generate_answer(question, context)

    logging.info("Step 5: Completed")

    return answer