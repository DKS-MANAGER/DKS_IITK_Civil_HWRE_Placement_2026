# Module 08: Agentic AI, Graph Analytics, and Knowledge Graphs

> **Module Code**: DEL-M08  
> **Priority**: P3 (Specialized Breadth — Explicit JD Requirement)  
> **Target Assessment**: Advanced Technical Interviews & Technology Architecture Defense  
> **Standard**: Complete theoretical foundations, agent loop mechanics, graph algorithms, Cypher syntax, GNN message passing intuition, and enterprise fraud/relationship use cases.

---

## 1. Part A: Agentic AI & Autonomous Workflows

### 1.1 From LLM Calls to Autonomous Agents

```text
Level 1: Zero-Shot LLM Call
  User Prompt ──► LLM ──► Text Output
  • Fixed, single step. No real-time data, no external tools.

Level 2: Retrieval-Augmented Generation (RAG)
  User Prompt ──► Vector Search ──► LLM + Context ──► Grounded Text Output
  • Read-only access to external documents. Deterministic, single-hop retrieval.

Level 3: Autonomous Agent (The ReAct Loop)
  User Goal ──► LLM Reasoner (Thought)
                     │
                     ▼
                 Action (Tool Selection: SQL / API / Search)
                     │
                     ▼
                 Environment Execution (Observation)
                     │
                     ▼
                 Reflection / State Update ──► Loop until Goal or Stopping Criterion!
```

---

### 1.2 Tool Calling Mechanics & Function Schemas

Modern LLMs do not execute code directly; they output structured JSON calling signatures matching a predefined tool schema:

```json
{
  "name": "query_enterprise_erp",
  "description": "Fetches real-time inventory levels from SAP S/4HANA for a given SKU",
  "parameters": {
    "type": "object",
    "properties": {
      "sku_code": {"type": "string", "description": "Unique material master ID"},
      "plant_id": {"type": "string", "description": "Manufacturing facility code"}
    },
    "required": ["sku_code", "plant_id"]
  }
}
```

### 1.3 Agent Orchestration Architectures
* **Single-Agent System**: One LLM maintains thought history, calls tools sequentially, and decides completion. High risk of infinite loops or context degradation on complex multi-step tasks.
* **Hierarchical Multi-Agent System (Manager-Worker)**:
  * **Supervisor / Router Agent**: Decomposes high-level client brief into subtasks; delegates tasks to specialized subagents; aggregates results.
  * **Specialist Subagents**: Dedicated prompts and constrained tools (e.g., *SQL Agent*, *Code Interpreter Agent*, *Report Drafting Agent*).

### 1.4 Guardrails, Loop Detection, and When NOT to Use Agents
* **Loop Prevention**: Maintain a global step counter (e.g., `max_iterations = 8`); detect duplicate tool calls with identical parameters.
* **Human-in-the-Loop (HITL)**: Mandatory manual confirmation gates for destructive actions (database updates, email dispatch, financial trades).
* **Consulting Pragmatism Rule**: If a business process follows a deterministic sequence of steps (e.g., monthly payroll calculation), **do not use an autonomous agent**. Deterministic code (Python script / Airflow DAG) is 100x cheaper, 10x faster, and has zero probability of hallucinated drift.

---

## 2. Part B: Graph Analytics & Knowledge Graphs

### 2.1 Graph Foundations & Network Theory

A graph $G = (V, E)$ consists of vertices (nodes) $V$ and edges $E$.
* **Adjacency Matrix ($A$)**: $A_{ij} = 1$ if edge $(i, j) \in E$, else $0$. Space: $O(|V|^2)$. Efficient for dense graphs, wasteful for sparse graphs.
* **Adjacency List**: Maps each node to its immediate neighbors. Space: $O(|V| + |E|)$. Optimal for real-world sparse enterprise networks.

### 2.2 Network Centrality Metrics & Enterprise Meaning

| Centrality Metric | Mathematical Definition | Consulting & Enterprise Application |
| :--- | :--- | :--- |
| **Degree Centrality** | $C_D(v) = \text{deg}(v)$ | Identifying high-volume transaction hubs or active communication nodes. |
| **Betweenness Centrality** | $C_B(v) = \sum_{s \ne v \ne t} \frac{\sigma_{st}(v)}{\sigma_{st}}$ | Detecting critical bridge nodes or single-point-of-failure suppliers in supply chains. |
| **Closeness Centrality** | $C_C(v) = \frac{1}{\sum_{u \ne v} d(v, u)}$ | Finding central distribution warehouses that minimize transit latency across a network. |
| **PageRank** | $PR(v) = \frac{1-d}{|V|} + d \sum_{u \in M(v)} \frac{PR(u)}{L(u)}$ | Measuring systemic importance in interconnected banking or interbank counterparty networks. |

---

### 2.3 Knowledge Graphs & Property Graph Querying (Cypher)

* **Knowledge Graph**: A structured semantic network storing real-world entities (nodes) connected by typed relationships (edges) with explicit schema constraints and entity resolution.
* **Property Graph Example (Neo4j / Cypher)**:

```cypher
// Query: Identify potential synthetic fraud rings sharing accounts or phone numbers
MATCH (c1:Customer)-[:HAS_IDENTIFIER]->(id:PhoneNumber)<-[:HAS_IDENTIFIER]-(c2:Customer)
WHERE c1.customer_id <> c2.customer_id
MATCH (c1)-[t:TRANSFERRED_FUNDS]->(c2)
RETURN c1.customer_id, c2.customer_id, id.value, t.amount
ORDER BY t.amount DESC;
```

---

### 2.4 Graph Neural Networks (GNN) Intuition: Message Passing

Standard neural networks cannot handle non-Euclidean graph topologies with variable node degrees. **Graph Neural Networks (GNNs)** solve this via **Neighborhood Aggregation (Message Passing)**:

```text
Step 1: Aggregate messages from local neighbors
  a_v^(k) = AGGREGATE( { h_u^(k-1) : u ∈ N(v) } )   [e.g., Sum, Mean, Max]

Step 2: Update target node representation
  h_v^(k) = UPDATE( h_v^(k-1), a_v^(k) )            [e.g., Linear layer + ReLU]
```

At layer $k$, node $v$ incorporates information from its $k$-hop neighborhood. Enables high-accuracy node classification (fraud detection) and link prediction (recommendation engines).

---

## 3. Self-Assessment Checklist

- [ ] Can articulate the transition from Zero-Shot LLM calls to the ReAct autonomous loop.
- [ ] Understand why multi-agent systems use supervisor routers and when deterministic scripts are preferred.
- [ ] Mastered degree, betweenness, and PageRank centralities in business context.
- [ ] Can read and write basic Cypher pattern matching queries (`MATCH ... WHERE ... RETURN`).
- [ ] Understand the 2-step intuition of GNN message passing (Aggregate and Update).
