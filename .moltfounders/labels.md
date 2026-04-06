# Labels

Canonical GitHub labels used by agents in this repository.

## Canonical Labels

| Label | Color | Description |
|-------|-------|-------------|
| `agent:reviewed` | `#0075ca` | Community PR was reviewed by the agent |
| `agent:approved` | `#0e8a16` | Community PR passed automated review and awaits human decision |
| `agent:changes-requested` | `#e4e669` | PR needs changes before it can proceed |
| `agent:rejected` | `#b60205` | PR was rejected by the automation flow |
| `needs-human` | `#e11d48` | Human attention is required because the agent cannot or should not resolve it automatically |

## Setup

Agents should ensure all labels above exist in the repo before executing loops.
If a label is missing, create it with the specified color and description via the GitHub API before proceeding.
