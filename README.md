# ase-2026-replication-package

Replication package for a Python mutation-testing study using
[Multiplex](https://github.com/LLM-Mutation/multiplex), for the ASE 2026 Tool
Demonstration. 

Prerequisites: [`uv`](https://astral.sh/uv), `git`, and an LLM endpoint (default:
Ollama serving `gpt-oss:20b`).

```bash
git submodule update --init PySnooper multiplex

# run one config end-to-end
scripts/run-config.sh --list
scripts/run-config.sh config-PySnooper-utils-format-exception-L91-basic.yml

# run everything
scripts/run-all.sh
```

