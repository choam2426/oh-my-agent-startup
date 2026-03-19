"""Run this script to post Palette's design spec comment to Linear issue MY-25."""
import sys
sys.path.insert(0, r"A:\oh-my-agent-startup\.claude\skills\linear-cli\scripts")

import os
from pathlib import Path

# Load .env
def load_dotenv():
    path = Path(r"A:\oh-my-agent-startup")
    for candidate in [path / ".env", path.parent / ".env"]:
        if candidate.is_file():
            with open(candidate, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, _, value = line.partition("=")
                    key = key.strip()
                    value = value.strip().strip("\"'")
                    if key not in os.environ:
                        os.environ[key] = value
            return

load_dotenv()

import json, urllib.request

API_URL = "https://api.linear.app/graphql"
api_key = os.environ.get("LINEAR_API_KEY", "")
if not api_key:
    print("ERROR: LINEAR_API_KEY not set")
    sys.exit(1)

body = open(r"A:\oh-my-agent-startup\.claude\agent-memory\palette\design_spec_body.txt", encoding="utf-8").read()

query = """mutation($input: CommentCreateInput!) {
  commentCreate(input: $input) {
    success
    comment { id body }
  }
}"""

variables = {"input": {"issueId": "71461ae1-1f57-488c-b4cf-8a14266d1f7d", "body": body}}
payload = json.dumps({"query": query, "variables": variables}).encode()
req = urllib.request.Request(
    API_URL,
    data=payload,
    headers={"Authorization": api_key, "Content-Type": "application/json"},
)
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read().decode())
    print(json.dumps(result, indent=2))
