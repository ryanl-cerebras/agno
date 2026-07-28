"""
File Tools
==========

Demonstrates file tools for reading from and writing to files.
The agent can create files and read their contents using the local file system.
"""

from pathlib import Path

from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.file import FileTools

# ---------------------------------------------------------------------------
# Create Agents
# ---------------------------------------------------------------------------

# Example 1: Read and write files
agent = Agent(
    model=OpenAIResponses(id="gpt-5.5"),
    tools=[FileTools(base_dir=Path("tmp/file_tools"), save_file=True)],
    markdown=True,
)

# Example 2: Read large files
large_file_agent = Agent(
    model=OpenAIResponses(id="gpt-5.5"),
    tools=[
        FileTools(
            base_dir=Path("tmp/file_tools"),
            save_file=True,
            max_file_length=2000000,  # 2M chars (~500k tokens)
            max_file_lines=40000,
        )
    ],
    markdown=True,
)

# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Write a file and then read it back
    agent.print_response(
        "Write a short poem about programming to a file named poem.txt, then read it back to me.",
        stream=True,
    )
