#!/bin/bash
# This script outputs the JSON definition for the 'get_tabs' tool.
cat <<'EOF'
[
  {
    "name": "get_tabs",
    "description": "Gets the title and URL of all open tabs in Safari.",
    "parameters": {
      "type": "OBJECT",
      "properties": {}
    }
  }
]
EOF
