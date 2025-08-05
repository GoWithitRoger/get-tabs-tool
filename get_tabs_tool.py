#!/usr/bin/env python
# get_tabs_tool.py

from __future__ import annotations

import subprocess
import os
import json
import sys
from typing import TypedDict, Union


class TabData(TypedDict):
    """Type definition for tab data structure."""

    title: str
    url: str


ErrorResponse = dict[str, Union[str, int]]


def parse_tab_line(line: str) -> TabData | None:
    """Parse a single tab line from AppleScript output.

    Args:
        line: A string in the format "title|||url"

    Returns:
        TabData dictionary if line is valid, None otherwise
    """
    if "|||" in line:  #
        title, url = line.split("|||", 1)  #
        return {"title": title, "url": url}  #
    return None


def fetch_safari_tabs() -> list[TabData]:
    """
    Retrieve list of open browser tabs by running an AppleScript.

    Returns:
        A list of TabData dictionaries.

    Raises:
        subprocess.CalledProcessError: If the AppleScript execution fails.
        FileNotFoundError: If the AppleScript file cannot be found.
    """
    # The script finds 'get_tabs.applescript' in the same directory.
    script_path = os.path.join(os.path.dirname(__file__), "get_tabs.applescript")

    if not os.path.exists(script_path):
        raise FileNotFoundError(f"AppleScript not found at: {script_path}")

    # The script runs 'osascript' to get the tab data.
    result = subprocess.run(
        ["osascript", script_path], capture_output=True, text=True, check=True
    )

    tabs: list[TabData] = []
    # The script parses the stdout from the AppleScript, which is a list of
    # tabs separated by newlines.
    for tab_line in result.stdout.strip().split("\n"):
        if tab_data := parse_tab_line(tab_line):
            tabs.append(tab_data)

    return tabs


if __name__ == "__main__":
    try:
        tabs_data = fetch_safari_tabs()
        # Print the final JSON data to standard output
        print(json.dumps(tabs_data, indent=2))

    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        # On error, create a JSON error message
        error_output: ErrorResponse = {"error": type(e).__name__, "message": str(e)}
        if hasattr(e, "stderr"):
            error_output["stderr"] = e.stderr

        # Print the error to standard error and exit
        print(json.dumps(error_output), file=sys.stderr)
        sys.exit(1)
