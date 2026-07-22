# Get Tabs Tool

A small macOS command-line utility that returns the titles and URLs of open Safari tabs as JSON. It
uses AppleScript through a short Python wrapper and can also be called from local automation tools.

This is a best-effort hobby project built for a specific macOS workflow. It may need adjustment as
Safari, macOS permissions, or third-party assistant integrations change.

## Requirements

- macOS with Safari
- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/)

## Usage

```bash
git clone https://github.com/GoWithitRoger/get-tabs-tool.git
cd get-tabs-tool
uv run get_tabs_tool.py
```

Example output:

```json
[
  {
    "title": "Example",
    "url": "https://example.com/"
  }
]
```

The first run may prompt your terminal application for permission to control Safari. If needed,
review the setting under **System Settings → Privacy & Security → Automation**.

## Gemini CLI helper scripts

The repository includes `discover_tools.sh` and `call_tool.sh` for the older Gemini CLI local-tool
interface. Point Gemini's `toolDiscoveryCommand` and `toolCallCommand` settings at those files and
make them executable:

```bash
chmod +x discover_tools.sh call_tool.sh
```

That integration is kept as a convenience and may change with Gemini CLI releases. The standalone
Python command does not depend on Gemini.

## Development

The parser tests do not open Safari and can run on any platform:

```bash
python -m unittest discover -s tests
```

## License

MIT. See [LICENSE](LICENSE).
