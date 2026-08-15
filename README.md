<div align="center">

<img src="assets/osai.png" alt="Awesome Open Source AI" width="120" />



# Awesome Open Source AI

Curated open-source artificial intelligence models, libraries, infrastructure, and developer tools.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

</div>

---
<div align="center">

**[Contributing](#contributing)**

</div>

## Contents

- [1. Core Frameworks & Libraries](#1-core-frameworks--libraries)
- [2. Model Codebases & Model Families](#2-model-codebases--model-families)
- [3. Inference Engines & Serving](#3-inference-engines--serving)
- [4. Agentic AI & Multi-Agent Systems](#4-agentic-ai--multi-agent-systems)
- [5. Retrieval-Augmented Generation (RAG) & Knowledge](#5-retrieval-augmented-generation-rag--knowledge)
- [6. Generative Media Tools](#6-generative-media-tools)
- [7. Training & Fine-tuning Ecosystem](#7-training--fine-tuning-ecosystem)
- [8. MLOps / LLMOps & Production](#8-mlops--llmops--production)
- [9. Evaluation, Benchmarks & Datasets](#9-evaluation-benchmarks--datasets)
- [10. AI Safety, Alignment & Interpretability](#10-ai-safety-alignment--interpretability)
- [11. Specialized Domains](#11-specialized-domains)
- [12. User Interfaces & Self-hosted Platforms](#12-user-interfaces--self-hosted-platforms)
- [13. Developer Tools & Integrations](#13-developer-tools--integrations)
- [14. Resources & Learning](#14-resources--learning)

---

## About this list

Awesome Open Source AI is a curated list of open-source projects for people building with AI.

The goal is to help readers find useful models, libraries, tools, infrastructure, datasets, and learning resources without sorting through a directory dump.

Projects do not need a minimum number of GitHub stars to be included. Stars can be useful context, but they are only one signal. A smaller project may belong here if it is useful, well-maintained, technically interesting, clearly documented, or important to a specific part of the AI ecosystem.

Good entries should have a clear reason to exist. They should help people build, study, run, evaluate, or understand AI systems.

---

## 1. Core Frameworks & Libraries

> Core libraries and frameworks used to build, train, and run AI and machine learning systems.

#### Deep Learning Frameworks

- [PyTorch](https://github.com/pytorch/pytorch) - Dynamic computation graphs, Pythonic API, dominant in research and production. The current standard for most frontier AI work. ![GitHub stars](https://img.shields.io/github/stars/pytorch/pytorch?style=social)
- [TensorFlow](https://github.com/tensorflow/tensorflow) - End-to-end platform with excellent production deployment, TPU support, and large-scale serving tools. ![GitHub stars](https://img.shields.io/github/stars/tensorflow/tensorflow?style=social)
- [JAX](https://github.com/jax-ml/jax) - High-performance numerical computing with composable transformations (JIT, vmap, grad). Rising favorite for research and scientific ML. ![GitHub stars](https://img.shields.io/github/stars/jax-ml/jax?style=social)
- [Flax](https://github.com/google/flax) - Neural network library for JAX, designed for flexibility. Apache-2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/google/flax?style=social)
- [dm-haiku](https://github.com/google-deepmind/dm-haiku) - JAX-based neural network library from Google DeepMind. Elegant functional API with state management, widely used in DeepMind's research. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/dm-haiku?style=social)
- [Equinox](https://github.com/patrick-kidger/equinox) - Elegant easy-to-use neural networks and scientific computing in JAX. Callable PyTrees with filtered transformations, seamless interoperability with the JAX ecosystem. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/patrick-kidger/equinox?style=social)
- [Diffrax](https://github.com/patrick-kidger/diffrax) - Numerical differential equation solvers in JAX. Autodifferentiable and GPU-capable ODE/SDE/CDE solvers for scientific machine learning and neural differential equations. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/patrick-kidger/diffrax?style=social)
- [vit-pytorch](https://github.com/lucidrains/vit-pytorch) - Comprehensive Vision Transformer (ViT) implementations in PyTorch. Reference implementations of all major vision transformer variants including ViT, DeiT, Swin, and more. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/lucidrains/vit-pytorch?style=social)
- [NumPyro](https://github.com/pyro-ppl/numpyro) - Probabilistic programming with NumPy powered by JAX for autograd and JIT compilation. Bayesian modeling and inference at scale. ![GitHub stars](https://img.shields.io/github/stars/pyro-ppl/numpyro?style=social)
- [Keras](https://github.com/keras-team/keras) - High-level, beginner-friendly API that now runs on multiple backends (TensorFlow, JAX, PyTorch). Perfect for rapid experimentation. ![GitHub stars](https://img.shields.io/github/stars/keras-team/keras?style=social)
- [tinygrad](https://github.com/tinygrad/tinygrad) - Minimalist deep learning framework with tiny code footprint. The "you like PyTorch? you like micrograd? you love tinygrad!" philosophy - simple yet powerful. ![GitHub stars](https://img.shields.io/github/stars/tinygrad/tinygrad?style=social)
- [PaddlePaddle](https://github.com/PaddlePaddle/Paddle) - Industrial deep learning platform from Baidu serving 23+ million developers and 760,000+ companies. China's first independent R&D framework with advanced distributed training and deployment capabilities. ![GitHub stars](https://img.shields.io/github/stars/PaddlePaddle/Paddle?style=social)
- [PyTorch Geometric](https://github.com/pyg-team/pytorch_geometric) - Library for deep learning on irregular input data such as graphs, point clouds, and manifolds. Part of the PyTorch ecosystem. ![GitHub stars](https://img.shields.io/github/stars/pyg-team/pytorch_geometric?style=social)
- [timm (PyTorch Image Models)](https://github.com/huggingface/pytorch-image-models) - The largest collection of PyTorch image encoders and backbones. 900+ pretrained models including ResNet, EfficientNet, Vision Transformer, ConvNeXt, and more with training and inference scripts. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/huggingface/pytorch-image-models?style=social)
- [Triton](https://github.com/triton-lang/triton) - Language and compiler for writing highly efficient custom deep-learning primitives. Powers kernel optimizations in PyTorch, JAX, and other frameworks. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/triton-lang/triton?style=social)
- [GGML](https://github.com/ggml-org/ggml) - Tensor library for machine learning. The foundational C/C++ library powering llama.cpp and many on-device inference engines. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/ggml-org/ggml?style=social)
- [MLX](https://github.com/ml-explore/mlx) - Array framework for machine learning on Apple silicon. Efficient unified memory design with NumPy-like API, automatic differentiation, and multi-device support. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/ml-explore/mlx?style=social)

#### High-Performance Compute Libraries

- [oneDNN](https://github.com/uxlfoundation/oneDNN) - oneAPI Deep Neural Network Library. Cross-platform performance library of basic building blocks for deep learning, optimized for Intel CPUs, GPUs, and Arm architectures. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/uxlfoundation/oneDNN?style=social)
- [ONNX](https://github.com/onnx/onnx) - Open standard for machine learning interoperability. Open Neural Network Exchange provides an open ecosystem that empowers AI developers to choose the right tools as their project evolves. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/onnx/onnx?style=social)
- [IREE](https://github.com/iree-org/iree) - Retargetable MLIR-based machine learning compiler and runtime toolkit. Lowers ML models to unified IR that scales from datacenter to mobile and edge deployments. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/iree-org/iree?style=social)

#### Rust ML Frameworks

- [Burn](https://github.com/tracel-ai/burn) - Next-generation deep learning framework in Rust. Backend-agnostic with CPU, GPU, WebAssembly support. ![GitHub stars](https://img.shields.io/github/stars/tracel-ai/burn?style=social)
- [Candle (Hugging Face)](https://github.com/huggingface/candle) - Minimalist ML framework for Rust. PyTorch-like API with focus on performance and simplicity. ![GitHub stars](https://img.shields.io/github/stars/huggingface/candle?style=social)
- [linfa](https://github.com/rust-ml/linfa) - Comprehensive Rust ML toolkit with classical algorithms. scikit-learn equivalent for Rust with clustering, regression, and preprocessing. ![GitHub stars](https://img.shields.io/github/stars/rust-ml/linfa?style=social)

#### Julia ML Frameworks

- [Flux.jl](https://github.com/FluxML/Flux.jl) - 100% pure-Julia ML stack with lightweight abstractions on top of native GPU and AD support. Elegant, hackable, and fully integrated with Julia's scientific computing ecosystem. ![GitHub stars](https://img.shields.io/github/stars/FluxML/Flux.jl?style=social)
- [MLJ.jl](https://github.com/JuliaAI/MLJ.jl) - Comprehensive Julia machine learning framework providing a unified interface to 200+ models with meta-algorithms for selection, tuning, and evaluation. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/JuliaAI/MLJ.jl?style=social)
- [ModelingToolkit.jl](https://github.com/SciML/ModelingToolkit.jl) - High-performance symbolic-numeric modeling framework for scientific machine learning. Automatically generates fast functions for model components like Jacobians and Hessians with automatic sparsification and parallelization. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/SciML/ModelingToolkit.jl?style=social)

#### NLP & Transformers

- [spaCy (Explosion AI)](https://github.com/explosion/spaCy) - Industrial-strength natural language processing with 75+ languages, transformer pipelines, and production-grade NER, parsing, and text classification. ![GitHub stars](https://img.shields.io/github/stars/explosion/spaCy?style=social)
- [Transformers (Hugging Face)](https://github.com/huggingface/transformers) - The de facto standard library for pretrained NLP models. 1M+ models, 250,000+ downloads/day. BERT, GPT, Llama, Qwen, and hundreds more. ![GitHub stars](https://img.shields.io/github/stars/huggingface/transformers?style=social)
- [sentence-transformers](https://github.com/UKPLab/sentence-transformers) - Classic library for sentence and image embeddings. ![GitHub stars](https://img.shields.io/github/stars/UKPLab/sentence-transformers?style=social)
- [tokenizers (Hugging Face)](https://github.com/huggingface/tokenizers) - Fast state-of-the-art tokenizers for training and inference. ![GitHub stars](https://img.shields.io/github/stars/huggingface/tokenizers?style=social)
- [fairseq2](https://github.com/facebookresearch/fairseq2) - FAIR Sequence Modeling Toolkit 2. Complete rewrite of fairseq with modern PyTorch APIs, native support for LLM training (70B+ models), vLLM integration, and first-party recipes for instruction finetuning and preference optimization. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/fairseq2?style=social)
- [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) - Self-hosted machine translation API powered by the Argos Translate engine. AGPL-3.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/LibreTranslate/LibreTranslate?style=social)

#### Data Processing & Manipulation

- [Pandas](https://github.com/pandas-dev/pandas) - The gold standard for data analysis and manipulation in Python. ![GitHub stars](https://img.shields.io/github/stars/pandas-dev/pandas?style=social)
- [Polars](https://github.com/pola-rs/polars) - Blazing-fast DataFrame library (Rust backend) - modern alternative to Pandas for large-scale workloads. ![GitHub stars](https://img.shields.io/github/stars/pola-rs/polars?style=social)
- [cuDF](https://github.com/rapidsai/cudf) - GPU DataFrame library from RAPIDS. Accelerates Pandas workflows on NVIDIA GPUs with zero code changes using cuDF.pandas accelerator mode. ![GitHub stars](https://img.shields.io/github/stars/rapidsai/cudf?style=social)
- [Dask](https://github.com/dask/dask) - Parallel computing for big data - scales Pandas/NumPy/scikit-learn to clusters. ![GitHub stars](https://img.shields.io/github/stars/dask/dask?style=social)
- [DataFlow](https://github.com/OpenDCAI/DataFlow) - LLM-ready data preparation system for turning raw PDFs, conversations, code, databases, and other sources into SFT, QA, and RAG-ready datasets. ![GitHub stars](https://img.shields.io/github/stars/OpenDCAI/DataFlow?style=social)
- [NumPy](https://github.com/numpy/numpy) - Fundamental array computing library that powers almost every AI stack. ![GitHub stars](https://img.shields.io/github/stars/numpy/numpy?style=social)
- [SciPy](https://github.com/scipy/scipy) - Scientific computing algorithms (optimization, linear algebra, statistics, signal processing). ![GitHub stars](https://img.shields.io/github/stars/scipy/scipy?style=social)
- [CuPy](https://github.com/cupy/cupy) - NumPy and SciPy-compatible array library for GPU-accelerated computing in Python. ![GitHub stars](https://img.shields.io/github/stars/cupy/cupy?style=social)
- [NetworkX](https://github.com/networkx/networkx) - Creation, manipulation, and study of complex networks. The foundational graph analysis library for Python data science. ![GitHub stars](https://img.shields.io/github/stars/networkx/networkx?style=social)
- [cuGraph](https://github.com/rapidsai/cugraph) - GPU graph analytics library with NetworkX-compatible API. 10-100x faster than CPU for large-scale graph algorithms. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/rapidsai/cugraph?style=social)
- [Vaex](https://github.com/vaexio/vaex) - Out-of-Core hybrid Apache Arrow/NumPy DataFrame for Python. Visualize and explore billion-row datasets at millions of rows per second. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/vaexio/vaex?style=social)
- [Datashader](https://github.com/holoviz/datashader) - High-performance large data visualization. Renders billions of points interactively without aggregation artifacts. BSD-3-Clause licensed. ![GitHub stars](https://img.shields.io/github/stars/holoviz/datashader?style=social)
- [Zarr](https://github.com/zarr-developers/zarr-python) - Chunked, compressed, N-dimensional array storage. Scalable tensor data format optimized for cloud and parallel computing. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/zarr-developers/zarr-python?style=social)
- [NVIDIA DALI](https://github.com/NVIDIA/DALI) - GPU-accelerated data loading and augmentation library with highly optimized building blocks for deep learning applications. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/DALI?style=social)
- [Narwhals](https://github.com/narwhals-dev/narwhals) - Lightweight compatibility layer between DataFrame libraries. Write Polars-like code that works seamlessly across Pandas, Polars, cuDF, Modin, and more. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/narwhals-dev/narwhals?style=social)
- [Ibis](https://github.com/ibis-project/ibis) - Portable Python dataframe library with 20+ backends. Write Pandas-like code that runs locally with DuckDB or scales to production databases (BigQuery, Snowflake, PostgreSQL) by changing one line. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/ibis-project/ibis?style=social)
- [skrub](https://github.com/skrub-data/skrub) - Machine learning with dataframes for dirty categorical data. Preprocessing and feature engineering for heterogeneous data with seamless Pandas/Polars integration. BSD-3-Clause licensed. ![GitHub stars](https://img.shields.io/github/stars/skrub-data/skrub?style=social)
- [Oxen](https://github.com/Oxen-AI/Oxen) - Lightning fast data version control for machine learning. Optimized for large datasets with efficient diffing, branching, and collaboration. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/Oxen-AI/Oxen?style=social)
- [Pandera](https://github.com/unionai-oss/pandera) - Statistical data testing and validation for dataframes. Pydantic-like API for Pandas, Polars, and other dataframe libraries with type hints and lazy validation. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/unionai-oss/pandera?style=social)
- [Snorkel](https://github.com/snorkel-team/snorkel) - System for quickly generating training data with weak supervision. Programmatically label, build, and manage training data using labeling functions and probabilistic consensus models. Powers Snorkel Flow and used by Google, Apple, and Intel. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/snorkel-team/snorkel?style=social)
- [DuckDB](https://github.com/duckdb/duckdb) - High-performance analytical in-process SQL database system. Fast, reliable, portable, and easy to use with rich SQL dialect support. Perfect for data processing and analytics workloads. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/duckdb/duckdb?style=social)
- [FiftyOne](https://github.com/voxel51/fiftyone) - Visual AI development toolkit for visualizing, labeling, and evaluating visual datasets and models. Supercharges computer vision workflows with dataset exploration and model analysis. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/voxel51/fiftyone?style=social)
- [Label Studio](https://github.com/HumanSignal/label-studio) - Multi-type data labeling and annotation tool with standardized output format. Configurable interface for images, text, audio, video, and time series with ML-assisted labeling. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/HumanSignal/label-studio?style=social)
- [Delta Lake](https://github.com/delta-io/delta) - Open-source storage framework enabling Lakehouse architecture with ACID transactions, scalable metadata handling, and unified batch/streaming processing. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/delta-io/delta?style=social)
- [Apache Iceberg](https://github.com/apache/iceberg) - High-performance open table format for huge analytic tables. Brings SQL table reliability to big data with time travel, hidden partitioning, and schema evolution. Works with Spark, Trino, Flink, Presto, Hive and Impala. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/apache/iceberg?style=social)
- [Apache Hudi](https://github.com/apache/hudi) - Open data lakehouse platform for ingesting, indexing, storing, serving, transforming and managing data across cloud environments. Supports upserts, deletes and incremental processing on big data with built-in ingestion tools for Spark and Flink. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/apache/hudi?style=social)
- [lakeFS](https://github.com/treeverse/lakeFS) - Data version control for your data lake that transforms object storage into Git-like repositories. Enables atomic, versioned data lake operations with branching, committing, and merging for data pipelines. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/treeverse/lakeFS?style=social)
- [Apache Airflow](https://github.com/apache/airflow) - Platform to programmatically author, schedule, and monitor workflows. Industry-standard orchestration for data pipelines and ML workflows with 500+ integrations. Apache 2.0 licensed. ![GitHub stars](https://img.shields…66670 tokens truncated…thub/stars/OvidijusParsiunas/deep-chat?style=social)
- [CopilotKit](https://github.com/CopilotKit/CopilotKit) - Best-in-class SDK for building full-stack agentic applications, Generative UI, and chat applications. Creators of the AG-UI Protocol adopted by Google, LangChain, AWS, and Microsoft. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/CopilotKit/CopilotKit?style=social)

#### CLI Tools & API Clients

- [Ruler](https://github.com/intellectronica/ruler) - Central AI agent rule registry. Manages and distributes rules for AI coding agents across projects. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/intellectronica/ruler?style=social)
- [PR-Agent (Qodo)](https://github.com/qodo-ai/pr-agent) - AI-powered code review agent for GitHub, GitLab, Bitbucket, and Azure DevOps. Automated PR analysis, improvement suggestions, and multi-platform deployment via CLI, GitHub Actions, or webhooks. AGPL-3.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/qodo-ai/pr-agent?style=social)
- [LLM (Simon Willison)](https://github.com/simonw/llm) - CLI tool and Python library for interacting with dozens of LLMs via remote APIs or locally. Extensible plugin ecosystem, SQLite logging. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/simonw/llm?style=social)
- [AIChat](https://github.com/sigoden/aichat) - All-in-one LLM CLI in Rust featuring Shell Assistant, Chat-REPL, RAG, AI Tools & Agents. Supports 20+ providers. MIT/Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/sigoden/aichat?style=social)
- [aicommits](https://github.com/Nutlope/aicommits) - CLI that writes your Git commit messages for you with AI. Never write a commit message again. Supports multiple providers including OpenAI, Groq, xAI, Ollama, and LM Studio. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/Nutlope/aicommits?style=social)
- [Codex CLI](https://github.com/openai/codex) - OpenAI's lightweight coding agent that runs in your terminal. Code generation, file editing, and command execution with approval. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/openai/codex?style=social)
- [Repomix](https://github.com/yamadashy/repomix) - Powerful tool that packs your entire repository into a single AI-friendly file. Perfect for feeding codebases to LLMs with smart filtering and token counting. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/yamadashy/repomix?style=social)
- [GitIngest](https://github.com/cyclotruc/gitingest) - Replace 'hub' with 'ingest' in any GitHub URL to get a prompt-friendly extract of a codebase. Optimized for Python ecosystem and data science workflows. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/cyclotruc/gitingest?style=social)
- [Instructor](https://github.com/jxnl/instructor) - Python library for extracting structured, validated data from LLMs using Pydantic models. Handles validation, retries, and error handling with 15+ provider support. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/jxnl/instructor?style=social)
- [Mirascope](https://github.com/Mirascope/mirascope) - Python toolkit for building LLM applications with automatic versioning, tracing, and cost tracking. The "LLM Anti-Framework" for developers who want control. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/Mirascope/mirascope?style=social)
- [Context7](https://github.com/upstash/context7) - Up-to-date code documentation for LLMs and AI code editors. Fetches latest docs and code examples directly into LLM context via MCP. Eliminates hallucinated APIs. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/upstash/context7?style=social)
- [Claude Squad](https://github.com/smtg-ai/claude-squad) - Manage multiple AI terminal agents like Claude Code, Codex, OpenCode, and Amp. Terminal multiplexer for AI coding agents with session management and parallel execution. AGPL-3.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/smtg-ai/claude-squad?style=social)
- [Herdr](https://github.com/ogulcancelik/herdr) - Terminal agent multiplexer and workspace manager with mouse-native split-panes and automatic agent state detection. AGPL-3.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/ogulcancelik/herdr?style=social)
- [agenttrace](https://github.com/luoyuctl/agenttrace) - Local-first TUI for observing AI coding agent sessions across Claude Code, Codex CLI, Gemini CLI, Aider, Cursor exports, OpenCode, and more. ![GitHub stars](https://img.shields.io/github/stars/luoyuctl/agenttrace?style=social)
- [agentsview](https://github.com/kenn-io/agentsview) - Local-first session intelligence and cost analytics dashboard for AI coding agents, supporting Claude Code, Codex, and other tools. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/kenn-io/agentsview?style=social)
- [Uni-CLI](https://github.com/olo-dot-io/Uni-CLI) - Self-repairing CLI catalog that exposes web, desktop, Electron, and bridge tools as deterministic commands for AI agents. ![GitHub stars](https://img.shields.io/github/stars/olo-dot-io/Uni-CLI?style=social)
- [OpenChamber Mobile Bridge](https://github.com/Zaradacht/opencode-openchamber-mobile-bridge) - OpenCode/OpenChamber helper for exposing devcontainer-based coding sessions to private Tailscale mobile access through a host bridge. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/Zaradacht/opencode-openchamber-mobile-bridge?style=social)
- [DesktopCommander MCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) - MCP server for Claude providing terminal control, file system search, and diff file editing capabilities. Enables autonomous code editing through Model Context Protocol. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/wonderwhy-er/DesktopCommanderMCP?style=social)
- [Claude Code Action](https://github.com/anthropics/claude-code-action) - GitHub Action for running Claude Code in PR and issue workflows with approval-aware automation and coding assistance. ![GitHub stars](https://img.shields.io/github/stars/anthropics/claude-code-action?style=social)
- [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) - Office suite purpose-built for AI agents to read, edit, and automate Word, Excel, and PowerPoint files without external Office installations. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/iOfficeAI/OfficeCLI?style=social)

#### SDKs & API Development Tools

- [Vercel AI SDK](https://github.com/vercel/ai) - Provider-agnostic TypeScript toolkit for building AI-powered applications and agents. Unified API for OpenAI, Anthropic, Google, and 20+ providers with first-class streaming, tool-calling, and structured output support. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/vercel/ai?style=social)
- [GitHub Copilot SDK](https://github.com/github/copilot-sdk) - Multi-platform SDK for integrating GitHub Copilot Agent into apps and services. Production-tested agent runtime with planning, tool invocation, and context management. Build Copilot-style agents without writing your own orchestration. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/github/copilot-sdk?style=social)
- [IBM MCP Context Forge](https://github.com/IBM/mcp-context-forge) - Gateway and registry for MCP/A2A/REST APIs with unified discovery, routing, and guardrails for production agent integrations. ![GitHub stars](https://img.shields.io/github/stars/IBM/mcp-context-forge?style=social)
- [Fern](https://github.com/fern-api/fern) - Open-source SDK generator for REST APIs. Generate type-safe API clients in TypeScript, Python, Go, Java, and more from OpenAPI specs. Powers SDKs for companies like OpenAI, Anthropic, and Cloudflare. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/fern-api/fern?style=social)

#### Testing & Debugging Tools

- [no-mistakes](https://github.com/kunchenguid/no-mistakes) - A local Git proxy and validation pipeline that runs AI-driven checks and applies fixes in a temporary worktree before forwarding pushes and opening clean PRs. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/kunchenguid/no-mistakes?style=social)
- [oai-smoke](https://github.com/airouter-dev/openai-compatible-api-smoke-test) - MIT-licensed, standard-library-only Go CLI that validates `/models` and opt-in `/chat/completions` behavior for OpenAI-compatible APIs and emits bounded diagnostics without credentials or response bodies. ![GitHub stars](https://img.shields.io/github/stars/airouter-dev/openai-compatible-api-smoke-test?style=social)

#### Prompt Engineering & Management

- [Helicone](https://github.com/Helicone/helicone) - Open-source LLM observability platform with prompt management, versioning, and experimentation. One-line integration, YC W23 company. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/Helicone/helicone?style=social)
- [GEPA](https://github.com/gepa-ai/gepa) - Reflective prompt evolution optimizer using natural language reflection and Pareto frontier learning. Outperforms reinforcement learning for prompt optimization. Integrated with DSPY and MLflow. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/gepa-ai/gepa?style=social)

---

## 14. Resources & Learning

#### Papers with Open Implementations

- [Papers with Code](https://paperswithcode.com) - Definitive database linking papers to open code and datasets.
- [Hugging Face Papers](https://huggingface.co/papers) - Daily-updated feed of the latest arXiv papers with open weights.
- [Open LLM Leaderboard (Hugging Face)](https://huggingface.co/spaces/open-llm-leaderboard) - Real-time ranking of open models.

#### Communities, Forums & Newsletters

- [Hugging Face Discussions](https://discuss.huggingface.co) - Largest open AI forum.

#### Educational Resources & Courses

- [AI Engineering from Scratch (rohitg00)](https://github.com/rohitg00/ai-engineering-from-scratch) - Comprehensive curriculum covering machine learning, deep learning, NLP, computer vision, and agents by implementing them from scratch. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/rohitg00/ai-engineering-from-scratch?style=social)
- [AMD Strix Halo Local LLM Guide](https://github.com/hogeheer499-commits/strix-halo-guide) - Reproducible Ubuntu, Ollama, llama.cpp, Vulkan/RADV, and ROCm setup and benchmark evidence for Ryzen AI MAX+ 395 local-AI systems. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/hogeheer499-commits/strix-halo-guide?style=social)
- [AI Agents in Depth](https://github.com/bojieli/ai-agent-book) - Open-source textbook and code repository covering AI agent design principles, architectures, and engineering practice. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/bojieli/ai-agent-book?style=social)
- [Prompt Engineering Guide (DAIR-AI)](https://github.com/dair-ai/Prompt-Engineering-Guide) - Comprehensive guides, papers, lessons, and notebooks for prompt engineering, context engineering, RAG, and AI Agents. The definitive open-source resource for learning prompt engineering with 3M+ learners. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/dair-ai/Prompt-Engineering-Guide?style=social)
- [Claude How To](https://github.com/luongnv89/claude-howto) - Comprehensive learning path and template guide for Claude Code, covering setup, hooks, custom skills, and MCP server integrations. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=social)
- [Maths, CS & AI Compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) - An open, unconventional textbook covering mathematics, computer science, and artificial intelligence from the ground up. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/HenryNdubuaku/maths-cs-ai-compendium?style=social)
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA) - Go-to subreddit for local/open-source LLM topics.

#### Courses & Interactive Playgrounds

- [Hugging Face Course](https://huggingface.co/learn) - Free hands-on courses using only open models.
- [ML For Beginners (Microsoft)](https://github.com/microsoft/ML-For-Beginners) - 12-week, 26-lesson, 52-quiz classic machine learning course for beginners. Comprehensive curriculum covering regression, classification, clustering, and NLP with practical projects. ![GitHub stars](https://img.shields.io/github/stars/microsoft/ML-For-Beginners?style=social)
- [AI For Beginners (Microsoft)](https://github.com/microsoft/AI-For-Beginners) - 12-week, 24-lesson curriculum on Artificial Intelligence. Covers symbolic AI, neural networks, computer vision, NLP, and reinforcement learning with hands-on labs. ![GitHub stars](https://img.shields.io/github/stars/microsoft/AI-For-Beginners?style=social)
- [Generative AI for Beginners (Microsoft)](https://github.com/microsoft/generative-ai-for-beginners) - 21 lessons covering generative AI fundamentals, prompt engineering, RAG applications, fine-tuning, and LLM app deployment with practical exercises. ![GitHub stars](https://img.shields.io/github/stars/microsoft/generative-ai-for-beginners?style=social)
- [LangChain Academy](https://academy.langchain.com) - Free courses on agents and RAG.
- [Data Science for Beginners (Microsoft)](https://github.com/microsoft/Data-Science-For-Beginners) - 10-week, 20-lesson curriculum on data science fundamentals. Covers data preparation, visualization, modeling, and deployment with practical projects. ![GitHub stars](https://img.shields.io/github/stars/microsoft/Data-Science-For-Beginners?style=social)
- [The Incredible PyTorch](https://github.com/ritchieng/the-incredible-pytorch) - Curated list of PyTorch tutorials, papers, projects, and communities for deep learning researchers. ![GitHub stars](https://img.shields.io/github/stars/ritchieng/the-incredible-pytorch?style=social)
- [Deep RL Class (Hugging Face)](https://github.com/huggingface/deep-rl-class) - Free deep reinforcement learning course with hands-on exercises and trained agent publishing to the Hugging Face Hub. ![GitHub stars](https://img.shields.io/github/stars/huggingface/deep-rl-class?style=social)
- [Practical RL (Yandex Data School)](https://github.com/yandexdataschool/Practical_RL) - Comprehensive reinforcement learning course covering RL fundamentals, deep RL, policy gradients, actor-critic methods, and practical applications in the wild. The Unlicense. ![GitHub stars](https://img.shields.io/github/stars/yandexdataschool/Practical_RL?style=social)
- [NLP Course (Yandex Data School)](https://github.com/yandexdataschool/nlp_course) - YSDA course in Natural Language Processing with 2025 materials covering text classification, language models, transformers, and modern NLP techniques. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/yandexdataschool/nlp_course?style=social)
- [Large Language Model Notebooks Course](https://github.com/peremartra/Large-Language-Model-Notebooks-Course) - Practical hands-on course about Large Language Models and their applications. Covers Chatbots, Code Generation, OpenAI API, Hugging Face, Vector databases, LangChain, Fine Tuning, PEFT, LoRA, QLoRA. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/peremartra/Large-Language-Model-Notebooks-Course?style=social)
- [Transformers Tutorials (Niels Rogge)](https://github.com/NielsRogge/Transformers-Tutorials) - Comprehensive tutorials and demos using the Hugging Face Transformers library for NLP, vision, and multimodal tasks. ![GitHub stars](https://img.shields.io/github/stars/NielsRogge/Transformers-Tutorials?style=social)
- [Made With ML (Goku Mohandas)](https://github.com/GokuMohandas/Made-With-ML) - End-to-end course on building production-grade ML systems with MLOps fundamentals, from design to deployment and iteration. ![GitHub stars](https://img.shields.io/github/stars/GokuMohandas/Made-With-ML?style=social)
- [AI Engineering Hub](https://github.com/patchy631/ai-engineering-hub) - 93+ production-ready projects with in-depth tutorials on LLMs, RAG, and real-world AI agent applications. Comprehensive resources for all skill levels from beginner to advanced. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/patchy631/ai-engineering-hub?style=social)
- [Complete Agentic AI Engineering Course](https://github.com/ed-donner/agents) - 6-week comprehensive course on Agentic AI covering autonomous agents, multi-agent systems, and practical agent development. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/ed-donner/agents?style=social)

#### Starter Projects & Examples

- [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - A collection of run-ready artificial intelligence templates and agent customizer scripts, featuring over 100 retrieval-augmented generation (RAG) and intelligent agent blueprints. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/Shubhamsaboo/awesome-llm-apps?style=social)
- [Claude Cookbooks](https://github.com/anthropics/claude-cookbooks) - Official collection of recipes and notebooks demonstrating tool use, prompt caching, structured outputs, and agentic workflows with Claude. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/anthropics/claude-cookbooks?style=social)
- [Hugging Face Transformers Notebooks](https://github.com/huggingface/notebooks) - Run Transformers, Datasets, and more in Colab. ![GitHub stars](https://img.shields.io/github/stars/huggingface/notebooks?style=social)
- [TensorFlow Tutorials](https://github.com/tensorflow/docs) - Official guides for beginners to advanced users. ![GitHub stars](https://img.shields.io/github/stars/tensorflow/docs?style=social)

#### Curated Resource Lists

- [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning) - The definitive curated list of machine learning frameworks, libraries and software organized by language. Covers Python, C++, Java, JavaScript, and more with comprehensive coverage of the ML ecosystem. CC0-1.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/josephmisiti/awesome-machine-learning?style=social)
- [Awesome Artificial Intelligence](https://github.com/owainlewis/awesome-artificial-intelligence) - Curated list of artificial intelligence courses, books, video lectures, and papers for developers and researchers. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/owainlewis/awesome-artificial-intelligence?style=social)
- [Andrej Karpathy Skills](https://github.com/forrestchang/andrej-karpathy-skills) - A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. Principles: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/forrestchang/andrej-karpathy-skills?style=social)
- [Awesome DESIGN.md](https://github.com/VoltAgent/awesome-design-md) - Curated collection of DESIGN.md files representing popular design systems to guide AI coding agents in consistent UI generation. MIT licensed. ![GitHub stars](https://img.shields.io/github/stars/VoltAgent/awesome-design-md?style=social)
- [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills) - Curated list of Claude Skills, plugins, resources, and custom commands to extend terminal and API workflows. Apache 2.0 licensed. ![GitHub stars](https://img.shields.io/github/stars/ComposioHQ/awesome-claude-skills?style=social)

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- Only OSI-approved licenses
- No minimum GitHub star requirement
- Useful, relevant, well-documented projects with a clear reason to exist
- Maintained current list, not a historical archive

