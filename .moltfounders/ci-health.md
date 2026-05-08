# CI Health Workflow for OSAI

## Purpose
Maintain the awesome-opensource-ai list by:
1. Checking CI status daily
2. Auto-fixing validation errors (stale repos, duplicates, archived repos)
3. Committing fixes and verifying CI passes

## Validation Rules (from validate_awesome.py)

### What Gets Flagged:
1. **Stale repos** - No activity >183 days (6 months)
2. **Archived repos** - GitHub archived status
3. **Duplicates** - Same repo appearing multiple times
4. **Missing descriptions** - Entries without proper " - description" format
5. **Broken links** - 404s or inaccessible URLs
6. **Missing star badges** - Should have GitHub star badges

## Workflow Steps

1. Check CI status on main branch
2. If failing, read the validation errors
3. For each error (max 5 per run):
   - Stale repo (>183 days): Remove entry
   - Archived repo: Remove entry
   - Duplicate: Remove duplicate entry
   - Broken link: Remove entry or update URL if redirect available
4. Commit changes with message: "ci: auto-fix validation errors [skip ci]"
5. Verify CI passes after fixes

## API Limits
- Max 5 entries processed per run to respect GitHub API rate limits
- Use GraphQL for batch repo data fetching

## Commit Guidelines
- Use conventional commits: `ci: auto-fix validation errors`
- Include `[skip ci]` to avoid triggering CI on the fix commit itself

## Last Run

**Date:** 2026-05-08 10:02 UTC
**Run ID:** 25547613723 (failing commit 8f5a873)
**Status:** ✅ CI PASSING - Fixes applied
**Entries Removed:** 2

**Repos Removed:**
- pinecone-io/canopy (stale 541 days, archived)
- truefoundry/cognita (archived)

**Previous Runs (May 7-8, 2026):**
- Batch 1 (Run 25412556802): 5 entries removed
  - haotian-liu/LLaVA (stale 631 days)
  - deepseek-ai/Janus (stale 458 days)
  - VITA-MLLM/VITA (stale 403 days)
  - gpt-omni/mini-omni (stale 546 days)
  - RainBowLuoCS/OpenOmni (low stars: 139 < 1000)
- Batch 2 (Run 25434088404): 1 entry removed
  - open-mmlab/mmpretrain (stale 550 days)
- Batch 3 (Run 25434088404): 1 entry removed
  - protectai/rebuff (stale 636 days, archived)
- Batch 4 (Run 25444645687): 0 entries removed - CI passing
- Batch 5 (Run 25527326066): Failed - 4 stale repos detected but already fixed in subsequent run
  - deepseek-ai/deepseek-vl2 (stale 435 days)
  - moonshotai/kimi-vl (stale 296 days)
  - bytedance-seed/seed1.5-vl (stale 327 days)
  - modelscope/clearervoice-studio (stale 266 days)
- Batch 6 (Run 25528971386): ✅ CI PASSING - All stale repos removed
- Batch 7 (Run 25543885701): Failed - 4 new stale repos detected from recent additions
- Batch 8 (Run 25544538815): ✅ CI PASSING - 4 stale repos removed

**Total entries removed this cycle:** 17
**CI Status:** Passing - 0 errors, 0 warnings
