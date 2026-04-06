# Operations Setup

Suggested unattended setup for `alvinreal/awesome-opensource-ai`.

This repo uses two loops only:

1. research loop
2. PR review loop

## Research Loop

Recommended schedule: hourly.

```bash
openclaw cron add \
  --name "OSAI Research Loop" \
  --schedule "15 * * * *" \
  --agent max \
  --message "Run research loop per .moltfounders/research.md.

State file: ~/.openclaw/workspace-max/states/cron/awesome-opensource-ai/research.json
Target repo: alvinreal/awesome-opensource-ai
Target branch: main
Min hours between runs: 1
Max entries per run: 5

Research exactly ONE category per run.
Open at most ONE PR per run.
Only create auto-merge-eligible PRs: README.md only, single-category only, non-structural changes only.
If 0 qualifying projects are found, open no PR and advance rotation.
If PR creation fails technically, record partial failure in state and retry that same category next run.
Update state file per spec after the run." \
  --delivery announce \
  --channel telegram \
  --to 1953698775
```

## PR Review Loop

Recommended schedule: 10:20 and 16:20 daily.

```bash
openclaw cron add \
  --name "OSAI PR Review Loop" \
  --schedule "20 10,16 * * *" \
  --agent max \
  --message "Run PR review loop. Read .moltfounders/pr-review.md and scan all open PRs in alvinreal/awesome-opensource-ai.

Trusted agent account: alvinreal.

For each PR:
1. Process agent PRs first, then community PRs.
2. Agent PRs authored by alvinreal may be auto-merged only if they are README.md-only, single-category, non-structural, and fully validated.
3. Community PRs are never auto-merged.
4. Skip all draft PRs.
5. Community PRs with conflicts: skip.
6. Agent PRs with conflicts: if otherwise eligible, attempt one safe conflict resolution, re-validate, then merge; otherwise close with reason.
7. Always verify facts via GitHub API and run required validation before merging an agent PR.
8. Temporary infra failure: leave agent PR open and retry later; after 3 retries, label needs-human and pause automation.
9. Valid community PRs: comment + label for human attention.
10. Mechanically invalid community PRs: close with specific reason." \
  --delivery announce \
  --channel telegram \
  --to 1953698775
```
