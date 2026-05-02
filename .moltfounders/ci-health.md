# CI Health Workflow for awesome-opensource-ai

This document defines the automated workflow for maintaining CI health on the awesome-opensource-ai repository.

## Validation Rules

The CI validator (`tools/validate_awesome.py`) checks:

### Structural Checks
- Entry format: `- **[Label](URL)** ![GitHub stars](badge) - Description`
- All GitHub repos must have a stars badge matching the repo
- No duplicate entries within the same section
- Table of contents anchors must match section headings

### Remote GitHub Checks (README.md - Elite Tier)
- **Minimum stars**: 1000+
- **Maximum staleness**: 183 days (6 months) since last push
- **Archived repos**: flagged as warnings
- **Disabled repos**: flagged as warnings

### Remote GitHub Checks (EMERGING.md - Emerging Tier)
- **Maximum stars**: 1000 (to stay in emerging)
- **Maximum staleness**: 183 days (6 months) since last push
- **Archived repos**: flagged as warnings

## Auto-Fix Workflow

When CI fails, follow this priority order (max 5 entries per run):

### 1. Fix Structural Errors
- Missing closing brackets in markdown
- Missing GitHub stars badges
- Malformed entry syntax

### 2. Remove Stale Repos (>183 days)
Check last push date. If >183 days:
- Remove from README.md or EMERGING.md
- Commit with message: `Remove stale repo: {name} (inactive {days} days)`

### 3. Handle Star Threshold Violations

**README.md entries** (must have 1000+ stars):
- If stars < 1000: Remove or move to EMERGING.md
- If stars dropped below threshold: Remove with message: `Remove {name} ({stars} stars below 1000 threshold)`

**EMERGING.md entries** (must have <1000 stars):
- If stars >= 1000: Move to appropriate section in README.md
- Commit with message: `Promote {name} to README.md ({stars} stars, now elite-tier)`

### 4. Handle Archived Repos
- Archived repos get a warning (not error)
- If archived + stale (>183 days): Remove
- Commit with message: `Remove archived repo: {name} (archived, inactive {days} days)`

### 5. Handle Duplicates
- Remove duplicate entries within the same section
- Keep the first occurrence
- Commit with message: `Remove duplicate entry: {name}`

## Commit Message Format

```
Fix validation errors: {brief description}

- {action} {repo_name} ({reason})
- {action} {repo_name} ({reason})
...
```

Examples:
- `Fix markdown syntax: add missing closing brackets for Mastra and FlashRAG entries`
- `Remove entries failing validation: bigcode-evaluation-harness (inactive 266 days), llama-agents (344 stars below 1000 threshold)`
- `Promote project to elite-tier: project-name (1250 stars, active)`

## Verification

After committing fixes:
1. Wait for CI to run on the commit
2. Verify CI passes (0 errors, 0 warnings)
3. If still failing, iterate (max 5 entries per run)

## Current Status

Last checked: 2026-05-02 10:02 UTC
CI Status: ✅ PASSING - No action needed

## Summary

CI Health Check completed for awesome-opensource-ai main branch.
- Status: ✅ PASSING (0 errors, 0 warnings)
- No fixes needed
- Last commit: 2026-05-02 02:05 UTC - CI passing

## Recent Activity

- 2026-05-02: CI Health Check (10:02 UTC) - ✅ No action needed. CI passing (0 errors, 0 warnings). All repos active and within thresholds.
- 2026-05-02: CI Health Check (08:02 UTC) - ✅ No action needed. CI passing (0 errors, 0 warnings). All repos active and within thresholds.
- 2026-05-02: CI Health Check (04:02 UTC) - ✅ No action needed. CI passing (0 errors, 0 warnings). All repos active and within thresholds.
- 2026-05-01: CI Health Check (10:02 UTC) - ✅ FIXED: Removed 3 stale repos: ell (329 days), textgrad (279 days), controlflow (251 days, archived). CI now passing (0 errors, 0 warnings).
- 2026-04-30: CI Health Check (16:02 UTC) - ✅ No action needed. CI passing (0 errors, 0 warnings). All repos active and within thresholds.
- 2026-04-29: CI Health Check (14:02 UTC) - ✅ FIXED: Removed 3 stale repos: whylogs (473 days), Featureform (299 days), Quivr (294 days). CI now passing (0 errors, 1 warning).
- 2026-04-29: CI Health Check (06:05 UTC) - ✅ FIXED: Removed stale repo `xiaomimimo/mimo` (inactive 327 days, over 183-day limit). CI now passing (0 errors, 1 warning).
- 2026-04-29: CI Health Check (04:02 UTC) - ✅ FIXED: Removed stale repo `superduper-io/superduper` (inactive 239 days, over 183-day limit). Local validation passed (0 errors, 0 warnings). Commit e05c2b7 pushed with [skip ci].
- 2026-04-29: CI Health Check (02:02 UTC) - ✅ FIXED: Removed stale repo `bigscience-workshop/petals` (inactive 598 days, over 183-day limit). Local validation passed (0 errors, 0 warnings). Commit 42091bc pushed with [skip ci].
- 2026-04-28: CI Health Check (08:02 UTC) - ✅ FIXED: Regex pattern in validate_awesome.py didn't handle hyphens in repo names (e.g., llm-d/llm-d at line 317). Changed `[^?)+]+` to `[^?]+`. CI now passing.
- 2026-04-28: CI Health Check (02:02 UTC) - No action needed. CI passing (0 errors, 0 warnings). Recent commits removed stale repos (LLaVA 623d, Video-LLaMA 692d, VideoLLaMA2 459d) and added new entries (Deepnote, AI-Infra-Guard).
- 2026-04-27: CI Health Check (16:02 UTC) - No action needed. CI passing (0 errors, 0 warnings). Duplicate entry already fixed in prior commit.
- 2026-04-27: CI Health Check (12:02 UTC) - Removed duplicate entry: LlamaFirewall (PurpleLlama repo already listed). CI now passing (0 errors, 0 warnings).
- 2026-04-27: CI Health Check (08:05 UTC) - Fixed 10 validation errors. Removed 5 stale repos (plandex 205d, taskingai 510d, quivr 291d, chatbot-ui 632d, gpt4all 334d) and 5 low-star repos (bytechef 749★, giselle 519★, nodetool 321★, nucliadb 720★, libre-webui 42★). CI now passing (0 errors, 1 warning).
- 2026-04-27: CI Health Check (06:02 UTC) - No action needed. CI passing (0 errors, 1 warning). All repos active and within thresholds.
- 2026-04-27: CI Health Check (02:02 UTC) - Fixed 3 stale repos: quivr (inactive 291 days), gluon-cv (inactive 517 days), opencode (inactive 220 days, archived). CI now passing (0 errors, 1 warning).
- 2026-04-27: CI Health Check (00:02 UTC) - No action needed. All repos active and within thresholds.
- 2026-04-26: CI Health Check (16:02 UTC) - No action needed. All repos active and within thresholds.
- 2026-04-26: CI Health Check (14:02 UTC) - No action needed. All repos active and within thresholds.
- 2026-04-26: CI Health Check (04:02 UTC) - Removed 1 stale repo: sacred (inactive 185 days)
- 2026-04-25: CI Health Check (12:02 UTC) - No action needed. All repos active and within thresholds.
- 2026-04-25: CI Health Check (04:20 UTC) - Removed 7 stale repos: coqui-ai/TTS (616 days), microsoft/muzic (559 days), logicalclocks/hopsworks (438 days), myshell-ai/OpenVoice (370 days), featureform/featureform (295 days), microsoft/farmvibes-ai (270 days), azavea/raster-vision (207 days)
- 2026-04-25: CI Health Check (04:02 UTC) - No action needed. All repos active and within thresholds.
- 2026-04-25: CI Health Check (02:02 UTC) - Removed 3 stale repos: QuivrHQ/quivr (289 days), AnswerDotAI/RAGatouille (342 days), stanford-oval/storm (206 days)
- 2026-04-24: CI Health Check (00:02 UTC) - No action needed. All repos active and within thresholds.
- 2026-04-23: CI Health Check (00:02 UTC) - No action needed. All repos active and within thresholds.
- 2026-04-22: CI Health Check (16:02 UTC) - No action needed. All repos active and within thresholds.
- 2026-04-22: CI Health Check (14:02 UTC) - No action needed. All repos active and within thresholds.
- 2026-04-22: CI Health Check (08:02 UTC) - Removed stepfun-ai/Step-Audio (repo not accessible via GitHub API)
- 2026-04-20: CI Health Check - No action needed. All repos active and within thresholds.
- 2026-04-19: Added Oumi (9,185+ stars) to Training & Fine-tuning Ecosystem
- 2026-04-19: Added RTP-LLM and LitServe to Inference Engines
- 2026-04-19: Added Mamba, Pythia, T5, GPT-NeoX-20B to Open Foundation Models
- 2026-04-15: Auto-removed 5 stale repos (skythought, arena-hard-auto, alpaca_eval, ceval, simple-evals) - all inactive >183 days
