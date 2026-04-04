# Research Loop Spec (Generic Category Rotation)

## Purpose

Deep research loop for finding elite-tier open-source AI projects. Cycles through categories systematically, maintaining state to track progress.

This spec is **schedule-agnostic** — implementers (cron jobs, manual runs, other agents) handle timing and state persistence.

## Core Logic

### Inputs (Provided by Runner)

| Input | Description |
|-------|-------------|
| `stateFile` | Path to JSON state file (runner manages location) |
| `minHoursBetweenRuns` | Cooldown between runs (runner sets this) |
| `maxEntriesPerRun` | Max entries to add per category (runner sets this) |
| `targetRepo` | GitHub repo to PR into (runner provides) |
| `targetBranch` | Branch for PRs (runner provides) |

### State File Format

Runner provides/maintains a state file with this structure:

```json
{
  "version": 1,
  "cycleStartDate": "2026-04-04",
  "lastRunTime": null,
  "lastCategoryIndex": null,
  "currentCycle": [
    {"index": 0, "name": "Core Frameworks & Libraries", "section": "§1", "lastResearched": null},
    {"index": 1, "name": "Open Foundation Models", "section": "§2", "lastResearched": null},
    {"index": 2, "name": "Inference Engines & Serving", "section": "§3", "lastResearched": null},
    {"index": 3, "name": "Agentic AI & Multi-Agent Systems", "section": "§4", "lastResearched": null},
    {"index": 4, "name": "RAG & Knowledge", "section": "§5", "lastResearched": null},
    {"index": 5, "name": "Generative Media Tools", "section": "§6", "lastResearched": null},
    {"index": 6, "name": "Training & Fine-tuning", "section": "§7", "lastResearched": null},
    {"index": 7, "name": "MLOps / LLMOps", "section": "§8", "lastResearched": null},
    {"index": 8, "name": "Evaluation & Benchmarks", "section": "§9", "lastResearched": null},
    {"index": 9, "name": "AI Safety & Interpretability", "section": "§10", "lastResearched": null},
    {"index": 10, "name": "Specialized Domains", "section": "§11", "lastResearched": null},
    {"index": 11, "name": "User Interfaces & Platforms", "section": "§12", "lastResearched": null},
    {"index": 12, "name": "Developer Tools", "section": "§13", "lastResearched": null},
    {"index": 13, "name": "Resources & Learning", "section": "§14", "lastResearched": null}
  ]
}
```

### Rotation Algorithm (Follow Exactly)

1. **Read state file** from path provided by runner
2. **Check `lastRunTime`**: If not null and less than `minHoursBetweenRuns` ago → skip this run, post "Research on cooldown, next run in X min"
3. **Find next category**: 
   - If `lastCategoryIndex` is null → use index 0
   - Else → increment by 1 (wrap 13→0)
4. **Research that ONE category** following the protocol below
5. **Update state file**:
   - Set `lastCategoryIndex` to the category just researched
   - Set `lastRunTime` to current ISO timestamp
   - Set `currentCycle[index].lastResearched` to current ISO timestamp
6. **Write updated state file** (runner manages persistence)

### Category Definitions

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

## Category-Specific Research Sources

**§1 Core Frameworks:**
- PyTorch ecosystem (torchvision, torchaudio, torchtext, torchao)
- JAX/Flax and XLA ecosystem
- Hugging Face libraries beyond transformers
- Data processing (pandas alternatives, polars, cuDF)
- New ML frameworks (Julia, Rust, C++, Zig)

**§2 Foundation Models:**
- Hugging Face model hub trending
- LLM leaderboard new entries (Open LLM Leaderboard, LMSYS)
- Paper releases with open weights
- Regional model labs (Europe, Asia, Middle East)
- Small/edge models (<7B params) with high quality

**§3 Inference & Serving:**
- vLLM forks and competitors
- New quantization methods (GGUF successors, HQQ variants)
- Edge/mobile inference optimizations
- Kubernetes operators for LLM serving
- WebAssembly/WASM inference

**§4 Agentic AI:**
- GitHub trending: `agent`, `autonomous`, `multi-agent`
- Agent framework releases (new competitors to LangGraph, AutoGen)
- Agent memory systems (vector + episodic + semantic)
- Tool-use libraries and function calling frameworks
- Agent evaluation benchmarks (SWE-bench variants)

**§5 RAG & Knowledge:**
- Vector DBs beyond top 5 (new entrants in search space)
- Embedding model releases (multimodal, long-context)
- Document parsers (PDF, DOCX, Excel, structured extraction)
- Graph RAG implementations (Neo4j, custom)
- Hybrid search (BM25 + vector + reranking)

**§6 Generative Media:**
- Diffusion model families (SD variants, FLUX successors)
- Video generation (consistency, length, quality improvements)
- Audio generation (music, speech, SFX, voice cloning)
- 3D generation (mesh, NeRF, Gaussian splatting)
- Real-time/streaming generation systems

**§7 Training & Fine-tuning:**
- Training framework releases (competitors to LLaMA-Factory, Axolotl)
- RLHF/RLAIF tools (new alignment methods)
- Synthetic data generation (distilabel competitors)
- Parameter-efficient methods (LoRA successors, DoRA variants)
- Distributed training optimizations

**§8 MLOps/LLMOps:**
- Prompt management and versioning
- LLM observability and tracing
- Cost tracking and optimization
- A/B testing frameworks for models
- Feature stores adapted for LLMs

**§9 Evaluation:**
- New benchmark suites (domain-specific, multilingual)
- Evaluation harnesses (competitors to lm-evaluation-harness)
- Red-teaming and safety evaluation tools
- Human evaluation platforms
- Automated eval metrics

**§10 Safety & Alignment:**
- Mechanistic interpretability tools
- Sparse autoencoders and feature extraction
- Constitutional AI and value alignment
- Adversarial robustness testing
- Guardrails and content filtering

**§11 Specialized Domains:**
- Scientific AI (protein folding, drug discovery, materials)
- Code-specific (type inference, refactoring, security analysis)
- Legal/medical/finance domain models
- Robotics simulators and environments
- Game AI and NPC behavior

**§12 User Interfaces:**
- New ChatGPT alternatives (self-hosted, privacy-focused)
- Mobile apps (iOS/Android native)
- Voice-first interfaces
- Desktop assistants (cross-platform)
- Browser extensions and web integrations

**§13 Developer Tools:**
- IDE plugins beyond top 5 (new VS Code/JetBrains extensions)
- Testing frameworks for AI applications
- Documentation generators from code
- API client tools for LLMs
- CLI productivity tools

**§14 Resources:**
- New courses and bootcamps (hands-on, project-based)
- Active communities (Discord, forums, local meetups)
- Newsletters and podcasts (weekly digests)
- New benchmark leaderboards
- Model cards and documentation repositories

## Qualification Criteria (Hard Thresholds)

**These are NON-NEGOTIABLE for Elite Tier inclusion:**

| Criterion | Minimum | Why |
|-----------|---------|-----|
| ⭐ GitHub Stars | **1000+** | Community validation |
| 🔄 Activity | Commits in last **30 days** | Alive and evolving |
| 🏭 Production | Evidence of real-world use | Case studies, integrations, prod issues |
| 📚 Quality | Docs, tests, releases | Professional grade |
| ✅ License | OSI-approved | Legal clarity |

**Projects below thresholds:** SKIP entirely. They may be candidates for separate Emerging list via community submission.

## "Current Best" Principle

For versioned families (PyTorch 2.x, Llama 3/4, Qwen 2.5/3.6):

1. **Check if family exists** in target README
2. **If newer major version found:**
   - Prepare PR to **REPLACE** existing entry
   - Update description for new version
   - Don't add alongside unless different use cases
3. **If same/older version:** Skip

This is "what you should know about now" — not a version archive.

## Output Format

One PR per run, category-focused:

```
[Research] Add N entries to {Category} - {Date}
```

PR body:
```markdown
## Category: {Category}

Adding {N} elite-tier projects.

| Project | Stars | License | Why It Fits |
|---------|-------|---------|-------------|
| {name} | {stars} | {license} | {brief} |

### Sources
- {source 1}
- {source 2}

### Verification
- [x] 1000+ stars
- [x] Active (30 days)
- [x] OSI license
- [x] Not already listed
```

## Limits

- Max entries per run: Use `maxEntriesPerRun` from runner (typically 5)
- If <3 found: Open PR anyway with what you found
- If 0 found: Skip PR, post "no qualifying projects for {Category}"

## Edge Cases

- **Multi-category fit:** Pick best fit, note overlap in PR
- **50+ entries in category:** Be selective, prioritize newest/best
- **Duplicate found:** Note in PR, pick better one
- **<1000 stars with big backing:** Still skip — quality > hype

## Cycle Completion

With 14 categories and typical hourly runs: full cycle completes in ~14 hours.

After completing index 13 (wrap to 0), the cycle repeats indefinitely.

## Notes for Implementers

- This spec is **timing-agnostic** — run hourly, daily, or on-demand
- State persistence is runner's responsibility
- Elite criteria are **hard floors** — no exceptions without maintainer override
- Emerging tier is out of scope — handled separately
