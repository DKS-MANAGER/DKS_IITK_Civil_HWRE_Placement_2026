# Execution Guardrails for Fable Mode

## Purpose

These guardrails prevent common failure modes during code generation and modification tasks. They act as safety nets that catch issues before they propagate.

## Pre-Flight Guardrails

### G1: File Safety Check
**Before ANY file modification:**
- Confirm the file exists (for edits) or the directory exists (for new files)
- Check if the file is under version control
- Verify the file is not read-only or protected
- Read the current file contents before modifying

### G2: Dependency Check
**Before modifying any file:**
- List all files that import/require the target file
- Identify potential breaking changes
- Check for circular dependencies

### G3: Scope Check
**Before starting implementation:**
- Confirm the task scope matches the plan
- Verify no scope creep has occurred
- Ensure all affected files are in the plan

## In-Flight Guardrails

### G4: Incremental Verification
**After each file modification:**
- Confirm the write operation succeeded
- Run syntax check if available (e.g., `node --check`, `python -m py_compile`)
- Do NOT proceed to next file until current file is verified

### G5: State Tracking
**Maintain awareness of:**
- Files modified so far
- Files remaining to modify
- Current stage in the stage map
- Any errors encountered

### G6: Rollback Readiness
**Before each modification:**
- Note the original file content (or ensure it's in version control)
- Be prepared to revert if verification fails
- Keep a change log for potential rollback

## Post-Flight Guardrails

### G7: Comprehensive Verification
**After ALL modifications are complete:**
- Run the full test suite
- Run linting/formatting checks
- Run build commands
- Verify no regressions were introduced

### G8: Cleanup Check
**Before marking task complete:**
- Remove any temporary files created
- Verify no debug code was left in place
- Check for unused imports or variables
- Confirm no secrets or credentials were committed

## Failure Recovery

### If a Guardrail is Triggered:
1. **STOP** immediately
2. **ASSESS** what went wrong
3. **REPORT** the issue clearly
4. **FIX** or **ROLLBACK** as appropriate
5. **RE-VERIFY** before proceeding

### Common Failure Modes:
| Failure | Guardrail | Recovery |
|---------|-----------|----------|
| File not found | G1 | Re-read file list, verify path |
| Syntax error | G4 | Fix syntax, re-verify |
| Test failure | G7 | Fix code, re-run tests |
| Scope creep | G3 | Return to PLAN stage |
| Breaking change | G2 | Assess impact, modify approach |

## Verification Commands

Run these commands after implementation:

```bash
# Syntax check (adapt to your language)
node --check filename.js
python -m py_compile filename.py
cargo check

# Test suite
npm test
pytest
cargo test
go test ./...

# Linting
npm run lint
ruff check .
cargo clippy

# Build
npm run build
cargo build
go build ./...
```
