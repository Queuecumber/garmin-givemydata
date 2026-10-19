#!/usr/bin/env python3
"""Entry point for Garmin MCP server over streamable HTTP.

Transport/host/port are env-driven so the stdio entrypoint stays untouched:
  MCP_TRANSPORT  "streamable-http" (default) | "stdio"
  MCP_HOST       bind address (default 0.0.0.0)
  MCP_PORT       port (default 8000)
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from garmin_mcp.server import mcp

if __name__ == "__main__":
    transport = os.environ.get("MCP_TRANSPORT", "streamable-http")
    if transport != "stdio":
        mcp.settings.host = os.environ.get("MCP_HOST", "0.0.0.0")
        mcp.settings.port = int(os.environ.get("MCP_PORT", "8000"))
    mcp.run(transport=transport)
