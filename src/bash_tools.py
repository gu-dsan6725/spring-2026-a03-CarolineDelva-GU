
import subprocess
import logging

import os

REPO_PATH = os.path.join(os.path.dirname(__file__), "..", "mcp-gateway-registry")


def run_command(command: str):

    logging.info(f"Executing command: {command}")

    result = subprocess.run(
        command,
        shell=True,
        cwd=REPO_PATH,
        capture_output=True,
        text=True,
        timeout=10
    )

    logging.info("Command finished")

    return result.stdout[:4000]

def select_tool(query_type: str, query: str):

    q = query.lower()

    if query_type == "file_search":

        if "fastapi" in q:
            return "grep -rn FastAPI ."

        if "cli" in q:
            return "grep -rn cli ."

        return "grep -rn 'app' ."

    if query_type == "function_search":
        return "grep -rn 'def ' ."

    if query_type == "explanation":
        return "grep -rn auth ."

    return "grep -rn FastAPI ."