"""
Direct Linear comment post — imports linear_cli internals to avoid subprocess.
Execute: python A:\oh-my-agent-startup\.claude\agent-memory\palette\execute_post.py
"""
import sys
sys.path.insert(0, r"A:\oh-my-agent-startup\.claude\skills\linear-cli\scripts")

# Monkey-patch sys.argv so linear_cli's argparse does not interfere
sys.argv = ["linear_cli.py"]

import linear_cli as lc

# Load API key from .env
lc.load_dotenv()
api_key = lc.get_api_key()

spec = open(r"A:\oh-my-agent-startup\.claude\agent-memory\palette\design_spec_body.txt", encoding="utf-8").read()

query = """mutation($input: CommentCreateInput!) {
  commentCreate(input: $input) {
    success
    comment { id body createdAt url user { name } }
  }
}"""

result = lc.graphql_request(
    query,
    {"input": {"issueId": "71461ae1-1f57-488c-b4cf-8a14266d1f7d", "body": spec}},
    api_key,
)
lc.handle(result)
