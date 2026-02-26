import os
import json
import requests
from typing import Optional, Literal
from mcp.server.aws_lambda import LambdaMCP

# ---------------------------------
# Config (env vars recommended)
# ---------------------------------
BASE_URL = os.environ.get("QUOTE_API_URL")
API_TOKEN = os.environ.get("API_TOKEN", "")
MAX_HOURS = 720
TIMEOUT = 5

# Reuse TCP connection across invocations
session = requests.Session()

mcp = LambdaMCP("Quote Analytics")


# ---------------------------------
# Core Fetch
# ---------------------------------
def fetch_quotes(hours: int):
    if not 1 <= hours <= MAX_HOURS:
        raise ValueError(f"hours must be between 1 and {MAX_HOURS}")

    r = session.get(
        BASE_URL,
        params={"hours": hours},
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()


# ---------------------------------
# Tool 1: Safe Raw Data
# ---------------------------------
@mcp.tool()
def get_quote_details(hours: int):
    data = fetch_quotes(hours)

    return {
        "total": len(data),
        "sample": data[:30]  # keep small for token safety
    }


# ---------------------------------
# Tool 2: Aggregation
# ---------------------------------
@mcp.tool()
def get_quote_metrics(
    hours: int,
    metric: Literal["count", "total_value", "average_value"],
    group_by: Optional[Literal["sales_rep", "region"]] = None,
):
    quotes = fetch_quotes(hours)
    if not quotes:
        return {"result": "No data"}

    def compute(items):
        if metric == "count":
            return len(items)

        values = [q.get("value", 0) for q in items]
        total = sum(values)
        return total if metric == "total_value" else total / len(values)

    if not group_by:
        return {metric: compute(quotes)}

    grouped = {}
    for q in quotes:
        key = q.get(group_by)
        if key:
            grouped.setdefault(key, []).append(q)

    return [{group_by: k, metric: compute(v)} for k, v in grouped.items()]


# ---------------------------------
# Lambda Entry Point
# ---------------------------------
def lambda_handler(event, context):
    return mcp.handle(event, context)
