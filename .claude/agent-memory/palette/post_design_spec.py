"""Post Palette design spec to Linear MY-25. Run from any directory."""
import os, sys, json, urllib.request
from pathlib import Path

# Load .env from project root
for candidate in [Path(r"A:\oh-my-agent-startup\.env"), Path(r"A:\oh-my-agent-startup") / ".env"]:
    if candidate.is_file():
        with open(candidate, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, _, v = line.partition("=")
                k = k.strip(); v = v.strip().strip("\"'")
                if k not in os.environ:
                    os.environ[k] = v
        break

api_key = os.environ.get("LINEAR_API_KEY", "")
if not api_key:
    print("ERROR: LINEAR_API_KEY not set", file=sys.stderr)
    sys.exit(1)

spec = open(r"A:\oh-my-agent-startup\.claude\agent-memory\palette\design_spec_body.txt", encoding="utf-8").read()

mutation = """mutation($input: CommentCreateInput!) {
  commentCreate(input: $input) {
    success
    comment { id }
  }
}"""

payload = json.dumps({
    "query": mutation,
    "variables": {"input": {"issueId": "71461ae1-1f57-488c-b4cf-8a14266d1f7d", "body": spec}}
}).encode("utf-8")

req = urllib.request.Request(
    "https://api.linear.app/graphql",
    data=payload,
    headers={"Authorization": api_key, "Content-Type": "application/json"},
)
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read().decode("utf-8"))
    if "errors" in result:
        print("GraphQL errors:", json.dumps(result["errors"], indent=2), file=sys.stderr)
        sys.exit(1)
    print("Comment posted:", json.dumps(result["data"], indent=2))
