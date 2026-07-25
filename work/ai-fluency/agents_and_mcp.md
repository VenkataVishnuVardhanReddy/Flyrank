# Agents, Workflows, and the Model Context Protocol (MCP)

This document provides a technical explainer on the distinction between AI workflows and autonomous agents, analyzes the primitives of the Model Context Protocol (MCP), and outlines the upgrade path for the literature synthesis pipeline.

---

## 1. Workflows vs. Agents: The Crucial Boundary

In modern AI system design, the terms "workflow" and "agent" are often conflated, but they represent entirely different architectural paradigms:

### The AI Workflow (Deterministic Chaining)
A **workflow** is a structured, predefined sequence of steps where the control flow is hardcoded. The developer defines exactly what happens at Step 1, how the output is transformed, and how it is handed off to Step 2 and Step 3. The LLM is used as an execution engine within these rigid boundaries; it does not decide *what* to do next or *which* tools to use. It only executes the prompt at the current node. 
- *Classification of our FL-03 Pipeline:* Our literature synthesis pipeline is strictly a **workflow**. The sequence—Gathering raw math, Critiquing against bilateral shielding, and Drafting final academic markdown—is entirely hardcoded. Claude cannot decide to skip the critique step or dynamically query a new paper on its own.

### The Autonomous Agent (Dynamic Routing)
An **agent** is a system where the AI is given a high-level goal and is equipped with a suite of tools (e.g. web search, file readers, code compilers). The model decides its own execution path: it calls a tool, observes the output, determines if it is sufficient, plans the next step, and stops only when it evaluates that the goal has been met. The control flow is dynamic and routed by the model's reasoning loop.

```text
WORKFLOW: [Input] ──► [Prompt 1] ──► [Prompt 2] ──► [Prompt 3] ──► [Output]
                                  (Hardcoded Track)

   AGENT: [Goal] ──► [Reasoning Loop] ◄──► [Tool Selector] ◄──► [FileSystem / OS]
                                  (Dynamic Routing)
```

---

## 2. What is the Model Context Protocol (MCP)?

The **Model Context Protocol (MCP)** is an open standard developed by Anthropic that acts as a "USB-C port" for AI applications. Historically, every AI developer had to write custom integrations for the model to access databases, files, or APIs. MCP standardizes this connection, allowing a single client interface to connect to any MCP-compliant server.

MCP defines three primary communication primitives:
1. **Tools (Read/Write Execution):** Executable functions that the model can invoke to perform operations in the real world (e.g., executing a command line, writing a file, or calling an API). Tools return raw output data to the model's context.
2. **Resources (Read-Only Data):** Data sources exposed by the server that the model can read but not modify. Examples include database tables, system logs, active configuration files, or local Git repositories.
3. **Prompts (Templates):** Structured prompt templates exposed by the server that can be loaded dynamically (e.g., a pre-defined bug-triage template or literature review guide).

---

## 3. Evidence of MCP Integration: Three Tool-Call Executions

We leverage an active MCP environment (Antigravity client) to interact directly with the local Windows workspace. This capability is impossible for standard chat models without tool integration:

### Task 1: Filesystem Query (Using `view_file` Tool)
- *What Chat Cannot Do:* Read a file from a local hard drive.
- *Tool Call:* `view_file` on `d:\Flyrank\work\notebooks\w03_data_contract.ipynb`.
- *Execution Evidence:*
  ```json
  // Request
  {
    "AbsolutePath": "d:\\Flyrank\\work\\notebooks\\w03_data_contract.ipynb",
    "toolAction": "Viewing w03 data contract notebook"
  }
  // Response (Truncated)
  {
    "output": "File Path: file:///d:/Flyrank/work/notebooks/w03_data_contract.ipynb\nTotal Lines: 85..."
  }
  ```

### Task 2: OS Shell Execution (Using `run_command` Tool)
- *What Chat Cannot Do:* Execute terminal bash/powershell scripts to check git status.
- *Tool Call:* `run_command` -> `git status`.
- *Execution Evidence:*
  ```json
  // Request
  {
    "CommandLine": "git status",
    "Cwd": "d:\\Flyrank"
  }
  // Response
  {
    "output": "On branch main\nYour branch is up to date with 'origin/main'.\nnothing to commit, working tree clean"
  }
  ```

### Task 3: Pattern Extraction (Using `grep_search` Tool)
- *What Chat Cannot Do:* Search through thousands of lines of unindexed local repository files for specific pattern matches.
- *Tool Call:* `grep_search` -> Query: `is_declining` on search path `d:\Flyrank\work`.
- *Execution Evidence:*
  ```json
  // Request
  {
    "SearchPath": "d:\\Flyrank\\work",
    "Query": "is_declining"
  }
  // Response (JSON Array of matches containing filenames and line numbers)
  ```

---

## 4. Upgrading the FL-03 Workflow to an Agent

To upgrade our literature synthesis workflow into an autonomous research agent, we must implement a **ReAct (Reasoning and Acting)** loop and equip it with MCP tools:

1. **Tool Equipping:** The model must be given access to an MCP Web Search Tool (e.g., Brave Search API) and an MCP PDF Reader Tool.
2. **Dynamic Routing Loop:** Instead of a hardcoded 3-step prompt chain, we give the model a high-level goal: 
   > *"Find and summarize all papers published between 2020 and 2026 proposing pre-processing filters for defending ResNet models against PGD attacks. Stop when you have compiled 5 valid papers."*
3. **Execution Logic:**
   - *Search:* The agent queries the web search tool to find relevant arXiv paper IDs.
   - *Evaluate:* The agent downloads and reads the paper text. It reads the methodology to evaluate if it uses ResNet and PGD. If it does not, the agent dynamically decides to discard it and query another.
   - *Verify:* The agent runs a code verification tool to check if the math matches before saving the summary.
   - *Halt:* Once 5 papers are verified, it compiles the final report and ends its turn.
   This changes the system from a rigid prompt track to an adaptive, goal-oriented researcher.
