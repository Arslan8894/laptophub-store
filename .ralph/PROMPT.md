# Ralph Loop Autonomous Agent Prompt — LaptopHUB

You are operating inside the **Ralph Loop** autonomous agent cycle for the **LaptopHUB** project.

## Your Operating Instructions for Each Iteration:
1. **Read Task List**:
   - Inspect `PRD.md` to identify the first unchecked task `[ ]`.
   - If all tasks are completed `[x]`, output `ALL_TASKS_COMPLETED` and stop.
2. **Review Codebase Rules**:
   - Adhere strictly to `AGENTS.md` and `.clinerules`:
     - NEVER delete or break existing features.
     - NEVER modify the 69-laptop inventory schema in `laptops-data.js` without explicit instructions.
     - Keep header styles in `css/header.css` and RAM pricing in `store-config.js`.
3. **Execute Task**:
   - Perform the smallest, most surgical modification required to satisfy the task.
4. **Run Backpressure Validation**:
   - Execute: `python scripts/test_fixes.py`.
   - If tests fail, diagnose and fix immediately. Do not commit failing code.
5. **Update State & Commit**:
   - Update `PRD.md` by marking the task `[x]`.
   - Update `.gsd/STATE.md` with the new progress.
   - Commit changes to git with a semantic commit message: `feat(scope): ...` or `fix(scope): ...`.
