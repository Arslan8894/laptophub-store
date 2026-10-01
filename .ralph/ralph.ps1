# ==============================================================================
# Ralph Loop PowerShell Runner for LaptopHUB (Windows)
# ==============================================================================
param (
    [int]$MaxIterations = 20,
    [string]$TaskFile = "PRD.md"
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  Starting Ralph Loop for LaptopHUB" -ForegroundColor Cyan
Write-Host "  Task Backlog: $TaskFile" -ForegroundColor Cyan
Write-Host "  Max Iterations: $MaxIterations" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

if (-not (Test-Path $TaskFile)) {
    Write-Error "Task file $TaskFile not found!"
    exit 1
}

# Run backpressure test before starting
Write-Host "`nRunning initial verification..." -ForegroundColor Yellow
python scripts/test_fixes.py
if ($LASTEXITCODE -ne 0) {
    Write-Error "Initial verification failed! Fix existing tests before running Ralph Loop."
    exit 1
}
Write-Host "Initial verification passed! Ready for autonomous iterations.`n" -ForegroundColor Green

# Count remaining tasks
$content = Get-Content $TaskFile -Raw
$pending = ([regex]::Matches($content, "\[ \] \*\*TASK-")).Count
Write-Host "Found $pending pending tasks in $TaskFile." -ForegroundColor White

if ($pending -eq 0) {
    Write-Host "All tasks already completed! Nothing to run." -ForegroundColor Green
    exit 0
}

Write-Host "Ralph Loop environment is initialized. Use the VSCode Ralph Loop extension or Antigravity Agent to drive iterations." -ForegroundColor Cyan
