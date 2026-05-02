# OSAI CI Health Report - 2026-05-03

## Summary

**Status:** ✅ CI PASSING

**Run Date:** May 3, 2026 at 00:08 UTC (Europe/Amsterdam)
**Repository:** alvinreal/awesome-opensource-ai (main branch)

## CI Status Check

**Latest GitHub Actions Run:**
- **Status:** ✅ Success
- **Run Date:** May 2, 2026 at 22:08 UTC
- **Workflow:** Validate awesome lists
- **Conclusion:** All checks passed

## CI Run History (main branch, last 5)
| Run # | Status | Commit | Time |
|-------|--------|--------|------|
| 651 | ✅ success | Remove stale repos | 2026-05-02 22:08 UTC |
| 650 | ❌ failure | Fix markdown syntax | 2026-05-02 22:05 UTC |
| 648 | ❌ failure | Add AutoGPT, BabyAGI, SuperAGI | 2026-05-02 21:17 UTC |
| 647 | ❌ failure | Add Annoy | 2026-05-02 20:19 UTC |
| 646 | ✅ success | Add xLLM and Mooncake | 2026-05-02 19:20 UTC |

## Issues Found and Fixed

### 1. Stale Repository: SuperAGI
- **Repository:** TransformerOptimus/SuperAGI
- **Issue:** Last pushed 2025-01-22 (100+ days ago, exceeds 183-day limit)
- **Action:** Removed from Multi-Agent Orchestration section
- **Stars:** 17,500 (met elite-tier threshold but inactive)

### 2. Stale Repository: Annoy (Spotify)
- **Repository:** spotify/annoy
- **Issue:** Last pushed 2025-10-29 (185 days ago, exceeds 183-day limit)
- **Action:** Removed from Vector Databases section
- **Stars:** 14,230 (met elite-tier threshold but inactive)

### 3. Markdown Syntax Error
- **Issue:** Missing blank line before "#### Embedding Models" subsection
- **Location:** Line 521 in README.md
- **Action:** Added blank line to fix structural validation

## Validation Results (Current)
```
== Structural checks ==
ok

== Remote GitHub checks ==
ok

Summary: 0 error(s), 0 warning(s)
```

## Actions Taken

1. ✅ Fixed markdown syntax (added missing blank line)
2. ✅ Removed stale repo: SuperAGI (inactive 100+ days)
3. ✅ Removed stale repo: Annoy (inactive 185 days)
4. ✅ Verified CI passes after fixes

## Summary Stats

- **Total entries processed:** 3
- **Stale repos removed:** 2 (SuperAGI, Annoy)
- **Markdown fixes:** 1 (blank line before subsection)
- **Entries remaining:** All current entries are active and within thresholds
- **Max entries per run limit:** 5 (not reached - 3 fixes applied)

## Notes

- AutoGPT and BabyAGI remain in the list (both active within 183 days)
- xLLM and Mooncake (added in run 646) remain active and compliant
- The list maintains 100% CI compliance after fixes
