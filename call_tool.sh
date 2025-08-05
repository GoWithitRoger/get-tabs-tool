#!/bin/bash
# This script executes a tool based on the name passed as the first argument.

# The name of the tool to run, e.g., "get_tabs"
TOOL_NAME=$1

# The directory where this script is located.
# This ensures we can run 'uv' from the correct project directory.
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

if [ "$TOOL_NAME" == "get_tabs" ]; then
  # Change to the tool's directory and execute it with 'uv'.
  # The output (the JSON of tabs) will be captured from stdout by Gemini CLI.
  (cd "$SCRIPT_DIR" && uv run get_tabs_tool.py)
else
  # Handle the case where an unknown tool is requested.
  echo "Error: Unknown tool '$TOOL_NAME'" >&2
  exit 1
fi