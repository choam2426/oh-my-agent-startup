#!/bin/bash
# oh-my-agent-startup launcher
# Usage: ./scripts/launch.sh "Build a fitness tracking SaaS dashboard"

set -e

MISSION="${1:?Usage: ./scripts/launch.sh \"<mission description>\"}"

export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

echo "🚀 Starting AI Startup with mission: $MISSION"
echo "📋 PM (Compass) will orchestrate the team..."
echo ""

claude --agent compass -p "$MISSION" \
  --allowedTools "Read,Write,Edit,Bash,Glob,Grep,Agent,WebSearch,WebFetch"
