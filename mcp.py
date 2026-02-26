import os
import requests
from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Quote Analytics MCP")

BASE_API_URL = "https://yourdomain.com/api/quoteDetails"
MAX_HOURS = 720  # guardrail


# ----------------------------
# Helper: Fetch Quotes
# ----------------------------
def fetch_quotes(hours: int):
    if hours <= 0 or hours > MAX_HOURS:
        raise ValueError(f"Hours must be between 1 and {MAX_HOURS}")

    response = requests.get(BASE_API_URL, params={"hours": hours}, timeout=10)
    response.raise_for_status()
    return response.json()
