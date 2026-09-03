# Double-Check Protocol Framework

## Universal Framework for Every Workspace

This protocol is designed to be copied and used in ANY workspace. It provides a standardized verification process that ensures code quality and correctness.

## How to Use This Framework

1. Copy this file to your workspace's `.roo/guardrails/` directory
2. Adapt the verification commands to your project's toolchain
3. Run all 5 passes before marking any task complete
4. Generate the double-check report for each task

## Double-Check Passes

### Pass 1: Code Correctness Check

**What to verify:**
- [ ] All code compiles/runs without syntax errors
- [ ] All functions/methods return expected types
- [ ] All edge cases are handled (null, empty, boundary values)
- [ ] Error handling is comprehensive
- [ ] No infinite loops or recursion without termination

**Verification Commands (adapt to your project):**
```bash
# JavaScript/TypeScript
node --check filename.js
tsc --noEmit

# Python
python -m py_compile filename.py
mypy filename.py

# Rust
cargo check

# Go
go build ./...

# Java
javac filename.java
```

### Pass 2: Style & Convention Check

**What to verify:**
- [ ] Code follows project style guide
- [ ] Naming conventions are consistent
- [ ] Comments are clear and necessary
- [ ] No dead code or commented-out code
- [ ] Import order follows project conventions

**Verification Commands (adapt to your project):**
```bash
# JavaScript/TypeScript
npm run lint
prettier --check .

# Python
ruff check .
black --check .

# Rust
cargo clippy

# Go
golangci-lint run
```

### Pass 3: Integration Check

**What to verify:**
- [ ] Changes don't break existing functionality
- [ ] New code integrates with existing modules
- [ ] API contracts are maintained
- [ ] Database migrations are backward-compatible
- [ ] Configuration changes are documented

**Verification Commands (adapt to your project):**
```bash
# JavaScript/TypeScript
npm test
npm run test:integration

# Python
pytest
pytest --integration

# Rust
cargo test

# Go
go test ./...
```

### Pass 4: Documentation Check

**What to verify:**
- [ ] Public APIs are documented
- [ ] Complex logic has explanatory comments
- [ ] README is updated (if needed)
- [ ] CHANGELOG is updated (if needed)
- [ ] Example usage is provided (if applicable)

### Pass 5: Security Check

**What to verify:**
- [ ] No hardcoded secrets or credentials
- [ ] Input validation is present
- [ ] SQL injection prevention (if applicable)
- [ ] XSS prevention (if applicable)
- [ ] Authentication/authorization checks

**Verification Commands (adapt to your project):**
```bash
# JavaScript/TypeScript
npm audit
snyk test

# Python
safety check
bandit -r .

# Rust
cargo audit

# Go
govulncheck ./...
```

## Double-Check Report Template

After completing all passes, output:

```
═══════════════════════════════════════
DOUBLE-CHECK REPORT
═══════════════════════════════════════

Task: [Brief task description]
Date: [Current date/time]
Workspace: [Workspace path]

PASS 1 - Code Correctness:
  [x] Syntax errors: NONE
  [x] Type errors: NONE
  [x] Edge cases: HANDLED
  [x] Error handling: COMPREHENSIVE
  [x] Infinite loops: NONE
  STATUS: ✅ PASSED

PASS 2 - Style & Convention:
  [x] Style guide: FOLLOWED
  [x] Naming conventions: CONSISTENT
  [x] Comments: ADEQUATE
  [x] Dead code: NONE
  [x] Import order: CORRECT
  STATUS: ✅ PASSED

PASS 3 - Integration:
  [x] Existing tests: PASSING
  [x] New integration: WORKING
  [x] API contracts: MAINTAINED
  [x] Database: COMPATIBLE
  [x] Configuration: DOCUMENTED
  STATUS: ✅ PASSED

PASS 4 - Documentation:
  [x] API docs: PRESENT
  [x] Comments: ADEQUATE
  [x] README: UPDATED
  [x] CHANGELOG: UPDATED
  [x] Examples: PROVIDED
  STATUS: ✅ PASSED

PASS 5 - Security:
  [x] Secrets: NONE HARDCODED
  [x] Input validation: PRESENT
  [x] SQL injection: PREVENTED
  [x] XSS: PREVENTED
  [x] Auth checks: PRESENT
  STATUS: ✅ PASSED

═══════════════════════════════════════
OVERALL STATUS: ✅ ALL PASSES COMPLETE
═══════════════════════════════════════
```

## Failure Handling

If ANY check fails:
1. **STOP** - Do not mark task complete
2. **IDENTIFY** - Which pass failed and what specific check
3. **FIX** - Address the failure
4. **RE-RUN** - Execute the failed pass again
5. **VERIFY** - Confirm the fix works
6. **CONTINUE** - Proceed to next pass

## Mandatory Requirements

- ❌ NEVER claim task complete without running all 5 passes
- ❌ NEVER skip a pass because "it should be fine"
- ❌ NEVER assume documentation is correct without checking
- ❌ NEVER assume security is handled without verifying

- ✅ ALWAYS run actual verification commands
- ✅ ALWAYS show command output
- ✅ ALWAYS complete the double-check report
- ✅ ALWAYS fix failures before proceeding

## Customization Guide

To adapt this framework to your workspace:

1. **Identify your language/toolchain**: Replace verification commands with project-specific ones
2. **Add project-specific checks**: Include checks for your framework's conventions
3. **Configure security tools**: Set up security scanning tools for your stack
4. **Update documentation checks**: Align with your project's documentation standards
5. **Test the framework**: Run a sample task to verify all checks work
