# oh-my-agent-startup launcher (Windows PowerShell)
# Usage: .\scripts\launch.ps1 "Build a fitness tracking SaaS dashboard"

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$Mission
)

$env:CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS = "1"

Write-Host "Starting AI Startup with mission: $Mission"
Write-Host "PM (Compass) will orchestrate the team..."
Write-Host ""

claude --agent compass -p $Mission --allowedTools "Read,Write,Edit,Bash,Glob,Grep,Agent,WebSearch,WebFetch"
