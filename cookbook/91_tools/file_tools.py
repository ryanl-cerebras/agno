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

# Example 1: Read and write files (default)
agent = Agent(
    model=OpenAIResponses(id="gpt-5.5"),
    tools=[FileTools(base_dir=Path("tmp/file_tools"))],
    markdown=True,
)

# Example 2: Write-only mode (disable read_file)
write_only_agent = Agent(
    model=OpenAIResponses(id="gpt-5.5"),
    tools=[FileTools(base_dir=Path("tmp/file_tools"), read_file=False)],
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
