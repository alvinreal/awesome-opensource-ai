# PR Review Rules

## When to Run

On every PR review loop cycle, scan all open pull requests.

## Trusted Agent Identity

- Any PR authored by GitHub user `alvinreal` is an **agent PR**.
- Any other PR is a **community PR**.

## Processing Order

1. Process all **agent PRs** first
2. Then process **community PRs**

## Global Rules

- Skip all draft PRs
- Reopened PRs are treated as fresh
- Community PRs already labeled `agent:reviewed` are skipped until new activity arrives
- Agent PRs are re-evaluated every run

## Agent PR Path

### Auto-merge eligibility

An agent PR may be auto-merged only if all are true:

- authored by `alvinreal`
- touches **`README.md` only**
- stays within **one category only**
- is **non-structural**
- passes all required validation

Structural changes include heading changes, category renames, section/order/layout changes, and formatting convention changes.

### Required checks before merge

Run all of these before merging:

1. `python3 tools/validate_awesome.py --skip-remote`
2. Direct GitHub API verification for stars, activity, license, and other factual claims
3. `python3 tools/validate_awesome.py` when credentials are available

If any required validation fails, merge is blocked.

### Fixable issues

One fix attempt is allowed for clearly fixable issues only:

- formatting
- placement/category adjustment
- wording cleanup
- badge/entry format fixes
- validator-fix issues
- simple merge conflict resolution

If still failing after one fix attempt, close the PR with a short specific reason.

### Conflict handling

- Community PR with conflicts: skip
- Agent PR with conflicts: if otherwise eligible, attempt one safe resolution and re-validate

### Temporary infrastructure failure

If required checks fail because of temporary infrastructure problems:

- leave the agent PR open
- comment once on first temporary failure
- retry on later runs
- after **3** temporary infra failures, add `needs-human`, comment once that automation is paused, and stop touching that PR automatically
- resume automation for that PR only after meaningful human activity (for example: new commit, rebase, edit, or comment)

### Outcomes for agent PRs

- **Eligible and valid:** merge silently
- **Valid but outside auto-merge scope:** leave open and apply `needs-human`
- **Mixed-scope PR** (safe + forbidden changes): close
- **Two open agent PRs for same category:** keep oldest, close newer
- **Broken PR being replaced:** close with explicit explanation

## Community PR Path

### Review requirements

Review community PRs against `CONTRIBUTING.md` and the current `README.md` state.
Verify factual claims via GitHub API rather than trusting the PR description.

### Outcomes for community PRs

- **Valid:** leave a clear review comment and apply `agent:reviewed`, `agent:approved`, and `needs-human`
- **Needs changes:** leave a clear review comment and apply `agent:changes-requested`
- **Mechanically invalid:** close with a specific reason and apply `agent:rejected`

Community PRs are never auto-merged.

### Overlap rules

- If an agent PR and community PR overlap, the agent PR takes priority operationally
- While unresolved, leave the community PR open with `needs-human`
- If the agent PR merges first and the community PR becomes redundant, close it with an explicit note that the change already merged via another PR

### Label maintenance

- If a community PR gets new commits or other meaningful new activity, clear outdated agent review labels before re-reviewing it
- Remove outdated failure or escalation labels automatically when the PR state becomes valid again
