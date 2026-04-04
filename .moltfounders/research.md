# Research Loop Rules (Hourly Category Rotation with State Tracking)

## Purpose

Aggressively fill the **elite-tier** awesome-opensource-ai list by cycling through all 14 categories with deep research. Runs hourly to maximize discovery speed while the repo is new.

**IMPORTANT:** This research loop targets ONLY the **Elite Tier (README.md)**. Projects that don't meet elite criteria (1000+ stars, production usage) are NOT included here — those belong in EMERGING.md which is populated separately through community submissions, not automated research.

## Frequency

Run **hourly at :15 past the hour** (cron: `15 * * * *`). Each run targets ONE specific category, rotating through the 14-category cycle.

## State Tracking

**CRITICAL: Read and update `~/.openclaw/workspace-max/cron/states/awesome-opensource-ai/research.json` every run.**

The state file tracks:
- `currentCycle` — array of 14 categories with research timestamps
- `lastCategoryIndex` — which category was last researched (null = start at 0)
- `lastRunTime` — when research last ran (null = first run)
- `minHoursBetweenRuns` — minimum hours before same category (set to 1 for hourly)
- `maxEntriesPerRun` — max 5 entries per category per run

### Rotation Logic (Follow Exactly)

1. **Read state file** at start of every run
2. **Check `lastRunTime`**: If less than 1 hour ago → skip this run, post "Research on cooldown, next run in X min"
3. **Find next category**: 
   - If `lastCategoryIndex` is null → start at index 0
   - Else → increment by 1 (wrap to 0 after index 13)
4. **Research that category** following the protocol below
5. **Update state**:
   - Set `lastCategoryIndex` to the category just researched
   - Set `lastRunTime` to current ISO timestamp
   - Set `currentCycle[index].lastResearched` to current ISO timestamp
6. **Write updated state file**

### Category Cycle (14 categories, hourly rotation)

| Index | Category | Target Section |
|-------|----------|----------------|
| 0 | Core Frameworks & Libraries | §1 |
| 1 | Open Foundation Models | §2 |
| 2 | Inference Engines & Serving | §3 |
| 3 | Agentic AI & Multi-Agent Systems | §4 |
| 4 | RAG & Knowledge | §5 |
| 5 | Generative Media Tools | §6 |
| 6 | Training & Fine-tuning | §7 |
| 7 | MLOps / LLMOps | §8 |
| 8 | Evaluation & Benchmarks | §9 |
| 9 | AI Safety & Interpretability | §10 |
| 10 | Specialized Domains | §11 |
| 11 | User Interfaces & Platforms | §12 |
| 12 | Developer Tools | §13 |
| 13 | Resources & Learning | §14 |

**Cycle repeats after index 13 → back to 0.**

## Deep Research Protocol (Per Category)

Don't just scan trending. Do targeted discovery for the specific category:

### Category-Specific Sources

**§1 Core Frameworks:**
- PyTorch ecosystem repos (torchvision, torchaudio, torchtext)
- JAX/Flax adjacent tools
- Hugging Face ecosystem beyond transformers
- Data processing libraries (beyond pandas/polars)
- New ML frameworks (Julia, Rust, C++)

**§2 Foundation Models:**
- Hugging Face model hub trending
- LLM leaderboard new entries
- Paper releases with open weights
- Regional model labs (Europe, Asia)
- Small/edge models (<7B params)

**§3 Inference & Serving:**
- vLLM forks and alternatives
- New quantization methods
- Edge/mobile inference tools
- Kubernetes operators for LLMs
- New GGUF/ONNX tooling

**§4 Agentic AI:**
- New agent frameworks (check GitHub tags: agent, autonomous)
- Multi-agent orchestration tools
- Agent memory systems
- Tool-use libraries
- Agent eval benchmarks

**§5 RAG & Knowledge:**
- Vector DBs beyond Chroma/Qdrant/Pinecone
- New embedding models
- Document parsers
- Graph RAG tools
- Hybrid search systems

**§6 Generative Media:**
- New diffusion models (image/video/3D)
- Audio generation (music, speech, SFX)
- Animation tools
- Real-time generation systems
- LoRA/training tools for media

**§7 Training & Fine-tuning:**
- New training frameworks
- RLHF tools
- Fine-tuning UIs
- Dataset curation tools
- Synthetic data generators

**§8 MLOps/LLMOps:**
- Prompt management tools
- LLM observability
- Cost tracking
- A/B testing for models
- Feature stores for ML

**§9 Evaluation:**
- New benchmarks
- Evaluation harnesses
- Red-teaming tools
- Model comparison UIs
- Safety eval suites

**§10 Safety & Alignment:**
- Interpretability tools
- Alignment training methods
- Adversarial testing
- Constitutional AI tools
- Guardrails frameworks

**§11 Specialized Domains:**
- Scientific AI (protein, drug, materials)
- Code-specific tools
- Legal/medical/finance AI
- Robotics simulators
- Game AI

**§12 User Interfaces:**
- New ChatGPT alternatives (self-hosted)
- Mobile apps
- Voice interfaces
- Desktop assistants
- Browser extensions

**§13 Developer Tools:**
- IDE plugins beyond Continue/Cline
- Testing frameworks for AI
- Documentation generators
- API clients
- CLI tools

**§14 Resources:**
- New courses/bootcamps
- Active communities
- Newsletters/podcasts
- Benchmark leaderboards
- Model cards repositories

### Handling Version Families ("Current Best" Principle)

For rapidly evolving projects (foundation models, frameworks with numbered releases):

1. **Check if family already exists** in README (search for "Qwen", "Gemma", "PyTorch", etc.)
2. **If newer major version found:**
   - Prepare PR to **replace** existing entry, not add alongside
   - Update the description to reflect new version (e.g., "3.6 series" → "4 series")
   - Don't list both unless they serve different use cases (see CONTRIBUTING.md exceptions)
3. **If same/older version:** Skip — already covered

**Remember:** This is "what you should know about now" — not a version archive.

## Qualification Criteria (ELITE TIER ONLY)

**DO NOT include projects below these thresholds.** This research loop targets ONLY the Elite Tier (README.md).

| Criterion | Threshold | Notes |
|-----------|-----------|-------|
| ⭐ **GitHub Stars** | **1000+** | Hard minimum, no exceptions |
| 🔄 **Active Development** | Meaningful commits within last **30 days** | Continuously evolving |
| 🏭 **Production Usage** | Evidence of real-world deployment | Case studies, integrations, production issues/PRs |
| 📚 **Quality Standards** | Proper docs, tests, releases | Professional grade |
| ✅ **License** | **OSI-approved** | No custom/unknown licenses |
| ❌ **Not Already Listed** | Search README.md first | Avoid duplicates |

### What About Projects with 100-999 Stars?

**Skip them entirely.** These belong in EMERGING.md which is populated through:
- Community submissions (not automated research)
- Manual maintainer curation
- Projects that naturally grow and get submitted

Your job: Find projects that are **already elite or clearly becoming elite** (1000+ stars, production traction).

## Output: Single Category-Focused PR

**One PR per run** targeting today's category only.

Format:
```
[Research] Add N entries to {Category} - {Date}
```

PR body template:
```markdown
## Category: {Category}

Adding {N} elite-tier projects discovered through targeted research.

| Project | Stars | License | Why It Fits |
|---------|-------|---------|-------------|
| {name} | {stars} | {license} | {one-line justification} |

### Research Sources
- Source 1: {what was checked}
- Source 2: {what was checked}
- Source 3: {what was checked}

### Verification
All projects checked for:
- [x] 1000+ stars
- [x] Active development (30 days)
- [x] OSI-approved license
- [x] Not already in README
- [x] Fits {Category} section
```

## Limits

- Max **5 entries per category per run**
- If <3 qualifying projects found, still open PR with what you found
- If 0 qualifying projects found, skip opening PR (post checkin noting "no qualifying projects found for {Category} today")

## Edge Cases

- **Project overlaps multiple categories:** Pick the best fit, note overlap in PR body
- **Category already has 50+ entries:** Be more selective (focus on newest/highest quality)
- **Duplicate found during research:** Note it in PR body, pick the better one
- **Stars <1000 but clearly significant:** **SKIP** — these go in EMERGING.md via community submission
- **Exceptional backing (OpenAI, Google, etc.) with <1000 stars:** **SKIP** — unless it's a major release that will hit 1000 stars within days

## Remember

This is a **14-day cycle** for elite-tier discovery. By April 18, every category should have been deeply researched once. Then we cycle again with fresh eyes.

**Key distinction:**
- **README.md (Elite):** Automated research finds 1000+ star, production-proven tools
- **EMERGING.md:** Community submissions bring 100-999 star promising projects

Keep the tiers separate. Don't dilute elite quality with emerging projects.
