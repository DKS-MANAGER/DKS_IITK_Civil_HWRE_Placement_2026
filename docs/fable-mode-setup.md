# Fable-Mode Setup Guide for Roo Code

## Overview

Fable-mode is a skill/protocol from the [mrtooher/fable-mode](https://github.com/mrtooher/fable-mode) GitHub repository designed for AI coding assistants. It provides structured instructions for systematic code generation, verification, and quality assurance.

## Key Components

### 1. SKILL.md Content
The core protocol that defines how the AI should approach coding tasks:
- Stage-based execution with verification checkpoints
- Inline delegation for single-agent runtimes
- Mandatory verification before marking stages complete

### 2. Single-Agent Runtime Adaptation
For Roo Code (which runs in single-agent context):
- **Inline Execution**: Worker phases execute sequentially within the same context
- **Stage Map**: Output numbered stage map first
- **Terminal Verification**: Run actual verification commands (tests, diffs, linters)

### 3. Execution Guardrails
Safety mechanisms to prevent errors:
- Pre-flight checks before code changes
- Post-implementation verification
- Rollback procedures for failed changes

### 4. Double-Check Protocol
Mandatory verification passes:
- Code correctness verification
- Style and convention compliance
- Performance impact assessment

## Setup Instructions

### Step 1: Create Custom Instructions File
Create a file at `.roo/custom-instructions/fable-mode.md` with the SKILL.md content.

### Step 2: Configure Roo Code Settings
Add to your VS Code settings:
```json
{
  "roo.customInstructions": "./.roo/custom-instructions/fable-mode.md"
}
```

### Step 3: Create Guardrails Documentation
Create guardrails in `.roo/guardrails/` directory.

## Files to Create

1. `.roo/custom-instructions/fable-mode.md` - Main skill protocol
2. `.roo/guardrails/execution-guardrails.md` - Safety mechanisms
3. `.roo/guardrails/double-check.md` - Verification protocols
4. `.roo/modes/fable.md` - Custom mode definition (if needed)

## Next Steps

To create the actual configuration files, we need to:
1. Switch to code mode to create non-markdown files
2. Download or reference the SKILL.md content from the fable-mode repository
3. Create the necessary directory structure

Would you like me to proceed with creating the documentation files first, or should we switch to code mode to create the actual configuration files?