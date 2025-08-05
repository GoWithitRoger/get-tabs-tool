<div align="left">
<img src="icon.svg" alt="Get Tabs Tool Icon" width="80" height="80">
</div>

# Get Tabs Tool - README.md

A command-line tool for macOS that retrieves the titles and URLs of all open tabs in Safari. It can be used as a standalone script or integrated as a local tool into AI assistants like the Gemini CLI.


## How It Works
This tool relies on **AppleScript** to communicate directly with the Safari application on your Mac. A Python script executes a small AppleScript file (`get_tabs.applescript`) which asks Safari for its open tabs and returns the information.

Because AppleScript is a macOS-specific technology, this tool will **only run on macOS**.


## Requirements

- **macOS** with Safari installed.
- **Python** >= 3.12
- [**uv**](https://github.com/astral-sh/uv) (for easy execution with managed dependencies).


## Standalone Usage (Command Line)
You can use this tool directly in your terminal to get a quick JSON list of your open tabs.

1. Navigate to the project directory:
    
        cd /path/to/get-tabs-tool
      
2. Run the tool using `uv`:
    
        uv run get_tabs_tool.py
      
The script will print a JSON array of your open Safari tabs to the terminal.

#### Example Output:
    
    [
      {
        "title": "Google",
        "url": "https://www.google.com/"
      },
      {
        "title": "Gemini CLI Documentation",
        "url": "https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/index.md"
      }
    ]
      
## Gemini CLI Integration
To use this as a local tool within the Gemini CLI, you need to configure the CLI to discover and call the script.

### Step 1: Create Helper Scripts
The Gemini CLI needs two small shell scripts to understand how to find and run your tool. Create the following two files inside your `get-tabs-tool` project directory.

**File 1: `discover_tools.sh`** (This script tells Gemini what the tool is called and what it does.)
    
    #!/bin/bash
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
    
**File 2: `call_tool.sh`** (This script tells Gemini how to execute the tool when it's needed.)
     
    #!/bin/bash
    TOOL_NAME=$1
    SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
    
    if [ "$TOOL_NAME" == "get_tabs" ]; then
      (cd "$SCRIPT_DIR" && uv run get_tabs_tool.py)
    else
      echo "Error: Unknown tool '$TOOL_NAME'" >&2
      exit 1
    fi
       
### Step 2: Make Scripts Executable
In your terminal, navigate to the `get-tabs-tool` directory and run the following command to make the helper scripts runnable:
    
    chmod +x discover_tools.sh call_tool.sh
       
### Step 3: Configure Gemini CLI `settings.json`
Finally, edit your Gemini CLI `settings.json` file to tell it about your new scripts. You will need to add the `toolDiscoveryCommand` and `toolCallCommand` keys, pointing to the absolute paths of the scripts you just created.
    
    {
      "theme": "Default",
      "selectedAuthType": "oauth-personal",
      "contextFileName": "GEMINI.md",
      "preferredEditor": "vscode",
      "toolDiscoveryCommand": "/Users/your_username/Projects/get-tabs-tool/discover_tools.sh",
      "toolCallCommand": "/Users/your_username/Projects/get-tabs-tool/call_tool.sh",
      "mcpServers": {
        "...": "..."
      }
    }
       
**Important:** Replace `/Users/your_username/` with the actual path to your home directory.

After saving `settings.json`, restart the Gemini CLI. It will now have the `get_tabs` tool available.


## Important: macOS Permissions
The first time you run this tool (either standalone or via Gemini), macOS will likely ask for permission for your terminal application (e.g., `Terminal.app`, `iTerm.app`) to control Safari. **You must approve this request for the tool to work.**

If you miss the pop-up or deny it, you can grant permission manually:

1. Open **System Settings**.
2. Go to **Privacy & Security > Automation**.
3. Find your terminal application in the list.
4. Ensure the checkbox for **Safari** is enabled.


## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.


## License
This project is licensed under the MIT License.