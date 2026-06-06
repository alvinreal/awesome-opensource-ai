# Contributing to Awesome Open Source AI

Thank you for helping improve this curated list.

Awesome Open Source AI is a curated list of open-source projects for people building with AI. The goal is to help readers find useful models, libraries, tools, infrastructure, datasets, and learning resources without sorting through a directory dump.

---

## Curation Philosophy

Projects do not need a minimum number of GitHub stars to be included. Stars can be useful context, but they are only one signal. A smaller project may belong here if it is useful, well-maintained, technically interesting, clearly documented, or important to a specific part of the AI ecosystem.

Good entries should have a clear reason to exist. They should help people build, study, run, evaluate, or understand AI systems.

Prefer projects with:

- Open-source licenses
- Working code or usable artifacts
- Clear documentation or examples
- Active maintenance or obvious ongoing relevance
- Concrete usefulness for AI builders, researchers, operators, or learners
- A meaningful distinction from similar projects

Avoid projects with:

- Shallow demos or thin wrappers
- Abandoned repositories with no current value
- Hype-heavy descriptions
- Unclear licensing
- SEO-bait or keyword-only “AI” positioning
- General-purpose infrastructure that is only weakly related to AI
- Low-effort generated boilerplate

This list is curated, not exhaustive. Inclusion is based on maintainer judgment, practical usefulness, technical quality, and relevance to open-source AI.

---

## Current, Not Historical

The AI ecosystem changes quickly. Prefer current, useful representatives over keeping old entries by default.

When a newer version or better-maintained project clearly replaces an older one, update or replace the entry instead of accumulating stale alternatives.

Use this test:

> Would someone using this list today benefit from seeing both entries, or only the current best representative?

Keep multiple related entries only when they serve meaningfully different use cases.

---

## Submission Guidelines

Before submitting a project:

1. Check for duplicates in `README.md`.
2. Choose the most specific category and subsection.
3. Confirm the project is meaningfully related to AI.
4. Confirm the license is open source and easy to find.
5. Write a factual one-sentence description.
6. Avoid marketing claims unless they are concrete and verifiable.
7. Run the validator locally:

```bash
python3 tools/validate_awesome.py --skip-remote
```

If you have a `GITHUB_TOKEN`, you can also run GitHub-backed validation:

```bash
GITHUB_TOKEN=... python3 tools/validate_awesome.py
```

---

## Entry Format

Use this format for GitHub projects:

```md
- [Project Name](https://github.com/owner/repo) - Factual one-sentence description. ![GitHub stars](https://img.shields.io/github/stars/owner/repo?style=social)
```

Use plain links for non-GitHub resources when a star badge does not apply.

Good description:

> High-performance vector search engine built in Rust with hybrid filtering and cloud-native deployment support.

Bad description:

> Revolutionary next-generation AI-powered vector database disrupting the industry with bleeding-edge performance.

---

## Pull Request Checklist

Please include the following in your PR description:

```md
## Project

- Name:
- URL:
- Category:

## Why it belongs

Briefly explain what the project helps people build, study, run, evaluate, or understand.

## Quality signals

- License:
- Maintenance status:
- Documentation/examples:
- Distinction from similar projects:
```

GitHub stars may be mentioned as context, but they are not required.

---

## Category Guidance

Use the existing categories in `README.md` as the source of truth. Add a new subsection only when the project does not fit any existing subsection and the new grouping would help future readers.

Each entry should be useful to someone browsing that category. Do not add projects only because they mention AI somewhere in the README.

---

## Maintainer Judgment

Maintainers may:

- Accept small or newer projects when they are useful, well-made, or technically interesting
- Reject popular projects that are off-topic, shallow, abandoned, or mostly hype
- Edit descriptions for accuracy and tone
- Move entries between sections
- Remove entries that become stale, misleading, or no longer useful

Meeting the checklist guarantees consideration, not acceptance.

---

## Questions

Open an issue if you are unsure where a project belongs or whether it fits the list.

---

*Quality standard: maintained, documented, useful, and relevant to open-source AI.*
