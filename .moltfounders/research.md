# Research Loop Spec (Generic Category Rotation)

## Purpose

Deep research loop for finding elite-tier open-source AI projects. It cycles through categories systematically and keeps state across runs.

This spec is **schedule-agnostic** — implementers (cron jobs, manual runs, other agents) handle timing and persistence.

## Clean Start Requirement

Before doing any research, edits, branch creation, or PR work, the runner/agent must start from a clean, current base:

1. Check out `main`
2. Sync to the latest remote state (`origin/main`)
3. If the local branch is dirty or diverged, reset to the latest `origin/main` before proceeding
4. Only then create or switch to the working branch for the current PR

## Inputs (Provided by Runner)

| Input | Description |
|-------|-------------|
| `stateFile` | Path to JSON state file |
| `minHoursBetweenRuns` | Cooldown between runs |
| `maxEntriesPerRun` | Max entries to change per category |
| `targetRepo` | GitHub repo to PR into |
| `targetBranch` | Branch for PRs |

## State File Format

```json
{
  "version": 1,
  "cycleStartDate": "2026-04-04",
  "lastRunTime": null,
  "lastCategoryIndex": null,
  "lastCategoryName": null,
  "lastOutcome": null,
  "lastError": null,
  "currentCycle": [
    {"index": 0, "name": "Core Frameworks & Libraries", "section": "§1", "lastResearched": null},
    {"index": 1, "name": "Open Foundation Models", "section": "§2", "lastResearched": null},
    {"index": 2, "name": "Inference Engines & Serving", "section": "§3", "lastResearched": null},
    {"index": 3, "name": "Agentic AI & Multi-Agent Systems", "section": "§4", "lastResearched": null},
    {"index": 4, "name": "RAG & Knowledge", "section": "§5", "lastResearched": null},
    {"index": 5, "name": "Generative Media Tools", "section": "§6", "lastResearched": null},
    {"index": 6, "name": "Training & Fine-tuning Ecosystem", "section": "§7", "lastResearched": null},
    {"index": 7, "name": "MLOps / LLMOps & Production", "section": "§8", "lastResearched": null},
    {"index": 8, "name": "Evaluation, Benchmarks & Datasets", "section": "§9", "lastResearched": null},
    {"index": 9, "name": "AI Safety, Alignment & Interpretability", "section": "§10", "lastResearched": null},
    {"index": 10, "name": "Specialized Domains", "section": "§11", "lastResearched": null},
    {"index": 11, "name": "User Interfaces & Self-hosted Platforms", "section": "§12", "lastResearched": null},
    {"index": 12, "name": "Developer Tools & Integrations", "section": "§13", "lastResearched": null},
    {"index": 13, "name": "Resources & Learning", "section": "§14", "lastResearched": null}
  ]
}
```

## Rotation Algorithm

1. Read state file
2. If `lastRunTime` is less than `minHoursBetweenRuns` ago, skip the run
3. Choose next category by stable numeric index, wrapping `13 → 0`
4. Research that **one** category only
5. Open **at most one PR** in the run
6. Update state:
   - On successful completion or intentional skip (`no qualifying projects`, `blocked by existing agent PR`) → set `lastCategoryIndex`, `lastCategoryName`, `lastRunTime`, `lastOutcome`, and `currentCycle[index].lastResearched`
   - On technical PR-creation failure → record `lastOutcome` and `lastError`, but do **not** advance the category

## Category Definitions

| Index | Category | Description |
|-------|----------|-------------|
| 0 | Core Frameworks & Libraries | Deep learning frameworks, data processing, foundational ML libraries |
| 1 | Open Foundation Models | Pretrained language, multimodal, speech, video models with open weights |
| 2 | Inference Engines & Serving | Inference runtimes, serving systems, optimization tools |
| 3 | Agentic AI & Multi-Agent Systems | Agent frameworks, multi-agent orchestration, autonomous tools |
| 4 | RAG & Knowledge | Vector DBs, embedding models, retrieval systems, document processing |
| 5 | Generative Media Tools | Image, video, audio, 3D generation models and applications |
| 6 | Training & Fine-tuning Ecosystem | Training frameworks, RLHF, synthetic data, distributed training |
| 7 | MLOps / LLMOps & Production | Experiment tracking, deployment, monitoring, guardrails |
| 8 | Evaluation, Benchmarks & Datasets | Benchmark suites, evaluation frameworks, high-quality datasets |
| 9 | AI Safety, Alignment & Interpretability | Alignment tools, interpretability, adversarial testing, red-teaming |
| 10 | Specialized Domains | Computer vision, robotics, scientific AI, domain-specific tools |
| 11 | User Interfaces & Self-hosted Platforms | Chat UIs, desktop apps, self-hosted platforms, voice interfaces |
| 12 | Developer Tools & Integrations | IDE plugins, testing frameworks, CLI tools, API clients |
| 13 | Resources & Learning | Courses, communities, newsletters, benchmark leaderboards |

## Qualification Criteria (Hard Thresholds)

| Criterion | Minimum | Why |
|-----------|---------|-----|
| ⭐ GitHub Stars | **1000+** | Community validation |
| 🔄 Activity | Commits in last **6 months** | Alive and evolving |
| 🏭 Production | Evidence of real-world use | Case studies, integrations, production issues |
| 📚 Quality | Docs, tests, releases | Professional grade |
| ✅ License | OSI-approved | Legal clarity |

Projects below thresholds are skipped.

## Output Rules

- At most **one PR per run**
- PRs must be **single-category only**
- PRs must touch **`README.md` only**
- PRs must be **non-structural** (entry add/remove/update only)
- If a candidate is ambiguous, skip it
- If an open agent PR already exists for the category, do not open another PR; advance rotation
- If an open community PR already proposes the same exact item, skip that item but continue evaluating the category
- If 0 qualifying projects are found, open no PR and advance rotation
- If 1-2 qualifying projects are found, a PR may still be opened
- If PR creation fails technically, record partial failure and retry the same category next run

## Current Best Principle

For versioned families, replace superseded entries rather than accumulating outdated versions unless both versions are clearly still worth listing.

## Validation Before Opening a PR

Before opening any PR generated from this loop:

1. Run `python3 tools/validate_awesome.py --skip-remote`
2. If GitHub auth is available, also run `python3 tools/validate_awesome.py`
3. If any required validation reports errors, do not open the PR

## Notes for Implementers

- State persistence is runner responsibility
- Emerging tier is out of scope here
- The research loop should create only PRs eligible for the automated merge path
