
import subprocess
import logging

REPO_PATH = "mcp-gateway-registry"


def run_command(command: str):

    logging.info(f"Executing command: {command}")

    result = subprocess.run(
        command,
        shell=True,
        cwd=REPO_PATH,
        capture_output=True,
        text=True
    )

    logging.info("Command finished")

    return result.stdout[:200]

def select_tool(query_type: str, query: str) -> str:

    if query_type == "file_search":
        return f"grep -rn '{query}' ."

    if query_type == "function_search":
        return f"grep -rn 'def ' ."

    if query_type == "dependency":
        return "cat cli/package.json"

    if query_type == "explanation":
        return "tree -L 2"

    return f"grep -rn '{query}' ."