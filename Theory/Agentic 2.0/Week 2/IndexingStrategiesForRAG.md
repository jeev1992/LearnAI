# Indexing Strategies for RAG

## Why Indexing Strategy Matters

### The Challenge
Not all queries need the same retrieval approach:

- **Specific questions:** "What's the API key for X?" → Need exact chunks
- **Broad questions:** "Tell me about authentication" → Need multiple related chunks
- **Exploratory queries:** "What issues are common?" → Need hierarchical browsing

### The Impact

| Bad Indexing | Good Indexing |
|---|---|
| Returns irrelevant chunks | Finds the right context |
| Misses related information | Connects concepts |
| Slow retrieval | Fast, scalable search |
| High false positives | Precise results |

---

## Five Indexing Strategies

### 1. Vector Index (Flat Index)

**Description:** Embed all chunks and retrieve by semantic similarity.

**How It Works:**

```
1. Chunk documents → [chunk1, chunk2, ..., chunkN]
2. Embed each chunk → [emb1, emb2, ..., embN]
3. Store in vector database
4. Query: Embed query → Find closest embeddings
```

**Code:**

```python
from llama_index.core import VectorStoreIndex, Document

# Create documents
docs = [Document(text=text, metadata=metadata) for text in texts]

# Create index
index = VectorStoreIndex.from_documents(docs)

# Query
query_engine = index.as_query_engine(similarity_top_k=3)
response = query_engine.query("How do I reset my password?")
```

**Pros:**
- ✅ Simple and effective
- ✅ Fast with modern vector DBs
- ✅ Works for 90% of use cases
- ✅ Easy to scale

**Cons:**
- ❌ No hierarchical structure
- ❌ May return fragmented chunks
- ❌ All chunks treated equally

**Best For:**
- General purpose RAG
- Q&A systems
- Semantic search
- Getting started quickly

**When to Use:**
- Default choice for most applications
- You have well-chunked documents
- Queries are specific and focused

**Real-World Use Cases:**

```
✓ Customer support ticket search
  Query: "How do I fix login issues?"
  Finds: "Authentication problems", "SSO failures"

✓ FAQ and documentation search
  Query: "What's the refund policy?"
  Finds: Semantically similar policy documents

✓ Chatbot knowledge base
  Query: "My order hasn't arrived"
  Finds: Shipping delay articles, tracking info

✓ Research paper search
  Query: "Machine learning for fraud detection"
  Finds: Related papers even with different terminology
```

**Scale:** Works well up to millions of documents

**Parameters:**

```python
query_engine = index.as_query_engine(
    similarity_top_k=3,  # Number of chunks to retrieve
    response_mode="compact",  # How to synthesize answer
    streaming=False  # Enable streaming responses
)
```

---

### 2. Summary Index

**Description:** Store and search through full documents using LLM evaluation.

**How It Works**

Unlike Vector Index which uses embeddings for similarity search, Summary Index stores full documents and uses the LLM to evaluate relevance:

**Storage (No Chunking, No Embeddings):**

```
[Doc 1: Full ticket text] → Stored as-is
[Doc 2: Full ticket text] → Stored as-is
[Doc 3: Full ticket text] → Stored as-is
...all documents stored without modification
```

**Query Process (Linear Scan):**

```
Query: "How do I fix authentication issues?"

Step 1: LLM reads Doc 1 → "Relevant? Yes"
Step 2: LLM reads Doc 2 → "Relevant? No"
Step 3: LLM reads Doc 3 → "Relevant? Yes"
... continues for ALL documents

Step N: Collect relevant docs → [Doc 1, Doc 3, ...]
Step N+1: Synthesize answer from all relevant docs
```

**Why It's Slow:**

```
Complexity: O(n) - must check every document
Each check = LLM call or LLM attention

10 documents:   ~2 seconds
100 documents:  ~20 seconds
1000 documents: ~200 seconds ⚠️ Too slow!
```

**Response Modes:**

```python
# tree_summarize: Hierarchical summarization
# - Summarizes groups of docs, then summarizes summaries
# - Good for comprehensive answers from multiple sources
query_engine = index.as_query_engine(response_mode="tree_summarize")

# compact: Fits as much as possible in one LLM call
query_engine = index.as_query_engine(response_mode="compact")

# refine: Iteratively refines answer with each doc
query_engine = index.as_query_engine(response_mode="refine")
```

**Code:**

```python
from llama_index.core import SummaryIndex

# Create index (no embeddings, stores full docs)
index = SummaryIndex.from_documents(docs)

# Query with tree_summarize for comprehensive answers
query_engine = index.as_query_engine(
    response_mode="tree_summarize"
)
response = query_engine.query("What are common auth issues?")
```

**Pros:**
- ✅ Returns full documents (no fragmentation)
- ✅ Good for high-level queries
- ✅ No embeddings needed (optional)

**Cons:**
- ❌ Slow for large datasets (O(n) scan)
- ❌ No semantic similarity
- ❌ LLM must process all docs

**Best For:**
- Small document collections (<100 docs)
- High-level summarization
- When you want full documents returned

**When to Use:**
- You have <50 documents
- Documents are naturally scoped (tickets, emails)
- Queries need broad context

**Real-World Use Cases:**

```
✓ Executive report summarization
  Query: "Summarize all customer complaints this week"
  Dataset: 20 complaint emails
  Returns: Comprehensive summary across all docs

✓ Meeting notes analysis
  Query: "What decisions were made about the budget?"
  Dataset: 15 meeting transcripts
  Returns: Full context from relevant meetings

✓ Email thread understanding
  Query: "What was the final agreement?"
  Dataset: 30 emails in a negotiation thread
  Returns: Complete thread context

✓ Small knowledge base Q&A
  Query: "What are our vacation policies?"
  Dataset: 25 HR policy documents
  Returns: Full policy documents, not fragments
```

**Scale:** <50 documents (gets slow beyond that)

**Performance:**

```
10 documents: ~2 seconds
100 documents: ~20 seconds
1000 documents: ~200 seconds ⚠️ Too slow!
```

---

### 3. Tree Index (Hierarchical)

**Description:** Build a tree structure from leaf nodes (chunks) to root (summary).

**How It Works:**

```
Root: "Support system overview"
  ├─ Branch: "Authentication issues"
  │   ├─ Leaf: "Password reset error"
  │   └─ Leaf: "SSO login failure"
  └─ Branch: "Performance problems"
      ├─ Leaf: "Database timeout"
      └─ Leaf: "Memory leak"

Query Process:
1. Start at root level
2. Find most relevant branch
3. Drill down to specific leaves
4. Return bottom-up synthesized answer
```

#### Tree Index: Detailed Example with Physics Textbook

Let's see how LlamaIndex builds and queries a tree structure using a Physics textbook:

**Input: Physics Textbook Chapters**

```
Chapter 1: Classical Mechanics
  - Section 1.1: Newton's Laws of Motion
    • Page 5: First Law (Inertia)
    • Page 7: Second Law (F=ma)
    • Page 10: Third Law (Action-Reaction)
  - Section 1.2: Energy and Work
    • Page 15: Kinetic Energy
    • Page 18: Potential Energy
    • Page 22: Conservation of Energy

Chapter 2: Electromagnetism
  - Section 2.1: Electric Fields
    • Page 45: Coulomb's Law
    • Page 48: Electric Field Strength
  - Section 2.2: Magnetic Fields
    • Page 55: Magnetic Force
    • Page 58: Electromagnetic Induction
```

#### How LlamaIndex Stores Nodes

LlamaIndex creates a multi-level hierarchy with two types of indexes:

**Level 1: Leaf Nodes (Detailed Index)**

```python
# These are the actual document chunks - stored with full content
Leaf_1a = Node(
    text="Newton's First Law states that an object at rest stays at rest, 
          and an object in motion stays in motion with constant velocity 
          unless acted upon by a net external force. This is the principle 
          of inertia...",
    metadata={'page': 5, 'section': '1.1', 'chapter': 1},
    node_id='leaf_1a'
)

Leaf_1b = Node(
    text="Newton's Second Law: F=ma. The net force on an object equals 
          its mass times acceleration. This fundamental equation allows 
          us to predict motion...",
    metadata={'page': 7, 'section': '1.1', 'chapter': 1},
    node_id='leaf_1b'
)

# ... more leaf nodes for each page
```

**Level 2: Branch Nodes (Summary Index - Coarse)**

```python
# LlamaIndex generates summaries of child nodes
Branch_1_1 = Node(
    text="Summary: This section covers Newton's Three Laws of Motion, 
          explaining inertia, force-mass-acceleration relationship, 
          and action-reaction pairs.",
    children=['leaf_1a', 'leaf_1b', 'leaf_1c'],
    metadata={'section': '1.1', 'chapter': 1},
    node_id='branch_1_1'
)

Branch_1_2 = Node(
    text="Summary: This section discusses energy concepts including 
          kinetic energy, potential energy, and the law of conservation 
          of energy.",
    children=['leaf_1d', 'leaf_1e', 'leaf_1f'],
    metadata={'section': '1.2', 'chapter': 1},
    node_id='branch_1_2'
)
```

**Level 3: Chapter Nodes (Higher-Level Summary)**

```python
Chapter_1 = Node(
    text="Summary: Classical Mechanics chapter covering Newton's Laws, 
          force, motion, energy, and work.",
    children=['branch_1_1', 'branch_1_2'],
    metadata={'chapter': 1},
    node_id='chapter_1'
)

Chapter_2 = Node(
    text="Summary: Electromagnetism chapter covering electric and 
          magnetic fields, Coulomb's Law, and electromagnetic induction.",
    children=['branch_2_1', 'branch_2_2'],
    metadata={'chapter': 2},
    node_id='chapter_2'
)
```

**Level 4: Root Node (Top-Level Summary)**

```python
Root = Node(
    text="Summary: Complete physics textbook covering Classical Mechanics 
          and Electromagnetism with fundamental laws and principles.",
    children=['chapter_1', 'chapter_2'],
    node_id='root'
)
```

#### Storage Structure

```
┌─────────────────────────────────────────────────────────────┐
│                    LLAMAINDEX TREE STORAGE                  │
└─────────────────────────────────────────────────────────────┘

Storage Layer:
  • All nodes stored in flat database (docstore)
  • Each node has: text, metadata, children, parent pointers
  • Summaries stored at branch/root level
  • Full content stored at leaf level

Tree Structure (logical, not storage):

                    [ROOT]
               "Physics Textbook"
                      │
        ┌─────────────┴─────────────┐
        │                           │
   [Chapter 1]                 [Chapter 2]
  "Classical Mech"          "Electromagnetism"
        │                           │
    ┌───┴───┐                   ┌───┴───┐
    │       │                   │       │
[Sec 1.1] [Sec 1.2]        [Sec 2.1] [Sec 2.2]
"Newton"  "Energy"          "Electric" "Magnetic"
    │       │                   │         │
  ┌─┼─┐   ┌─┼─┐              ┌─┼─┐     ┌─┼─┐
  L L L   L L L              L L       L L
  (Pages) (Pages)          (Pages)   (Pages)

L = Leaf nodes (detailed content)
Summary Index (Coarse) = Chapter, Section nodes
Detailed Index = Leaf nodes
```

#### Query Resolution: Multiple Matching Nodes

**Query Example:** "Explain Newton's Second Law and electromagnetic induction"

This query matches two different branches of the tree.

**Scenario 1: Matching Nodes on Same Path**

Query: "Explain Newton's First and Second Laws"

```
Matching nodes:
  • Branch_1_1 (Newton's Laws) - matches both
  • Leaf_1a (First Law) - matches
  • Leaf_1b (Second Law) - matches

Resolution:
┌─────────────────────────────────────────┐
│   SAME PATH - Traverse Down             │
└─────────────────────────────────────────┘

Step 1: Start at root, find Chapter 1 matches
Step 2: Drill into Branch_1_1 (Newton's Laws)
Step 3: Since multiple leaves match AND on same path:
        → Retrieve ALL matching leaves [1a, 1b]
Step 4: Synthesize answer from both leaves

Result: Comprehensive answer using BOTH leaf nodes
```

**Scenario 2: Matching Nodes on Different Paths**

Query: "Explain Newton's Second Law and electromagnetic induction"

```
Matching nodes:
  • Branch_1_1 (Newton's Laws) - matches "Second Law"
    └─ Leaf_1b (F=ma)
  • Branch_2_2 (Magnetic Fields) - matches "induction"
    └─ Leaf_2d (Electromagnetic Induction)

Resolution:
┌─────────────────────────────────────────┐
│   DIFFERENT PATHS - Evaluate Both       │
└─────────────────────────────────────────┘

Step 1: Start at root
Step 2: LLM evaluates: "Which chapters are relevant?"
        → Chapter 1: Relevance score = 0.8
        → Chapter 2: Relevance score = 0.9
Step 3: Explore BOTH chapters (controlled by child_branch_factor)
Step 4: Chapter 1 path:
        - Drill to Branch_1_1 → Retrieve Leaf_1b
Step 5: Chapter 2 path:
        - Drill to Branch_2_2 → Retrieve Leaf_2d
Step 6: Combine results from BOTH paths
Step 7: LLM synthesizes answer using both leaves

Result: Answer covering BOTH topics from different sections
```

#### LlamaIndex Query Algorithm

```python
def query_tree_index(query, root_node, child_branch_factor=1):
    """
    Traverse tree based on relevance
    
    Args:
        child_branch_factor: How many branches to explore at each level
                           1 = single path (greedy)
                           2+ = multiple paths (thorough)
    """
    current_level = [root_node]
    relevant_leaves = []
    
    while current_level:
        # Evaluate all nodes at current level
        scored_nodes = []
        for node in current_level:
            # LLM judges: "Is this node relevant to query?"
            relevance_score = llm.evaluate_relevance(query, node.text)
            scored_nodes.append((node, relevance_score))
        
        # Sort by relevance
        scored_nodes.sort(key=lambda x: x[1], reverse=True)
        
        # Select top child_branch_factor nodes
        selected = scored_nodes[:child_branch_factor]
        
        # Prepare next level
        next_level = []
        for node, score in selected:
            if node.is_leaf():
                # Reached bottom - this is detailed content
                relevant_leaves.append(node)
            else:
                # Intermediate node - continue traversing
                next_level.extend(node.children)
        
        current_level = next_level
    
    # Synthesize answer from all relevant leaves
    context = "\n\n".join([leaf.text for leaf in relevant_leaves])
    answer = llm.generate_answer(query, context)
    return answer
```

#### Key Insights

**1. Coarse-to-Fine Retrieval:**

```
Coarse (Summary Index): High-level summaries at branch/root
Fine (Detailed Index): Full content at leaf nodes
Query starts coarse, drills down to fine details
```

**2. Same Path Logic:**

```python
if all_matching_nodes_on_same_path:
    # Retrieve all matching leaves on that path
    return [leaf for leaf in path if leaf.matches(query)]
    # Example: "First Law and Second Law" → both from Newton section
```

**3. Different Path Logic:**

```python
if matching_nodes_on_different_paths:
    # Evaluate each path's relevance
    # Explore top K paths (K = child_branch_factor)
    # Collect leaves from multiple paths
    # Synthesize combined answer
    # Example: "Newton's Law and Induction" → two different chapters
```

**4. Efficiency:**

```
Don't read all documents (unlike Summary Index)
Only traverse relevant branches
Good for 1000+ documents with clear hierarchy
```

**Code:**

```python
from llama_index.core import TreeIndex

# Build tree
index = TreeIndex.from_documents(
    docs,
    num_children=10,  # Branching factor
    build_tree=True
)

# Query (traverses tree)
query_engine = index.as_query_engine(
    child_branch_factor=2  # How many branches to explore per level
)

# Single path query
response = query_engine.query("What is Newton's Second Law?")
# Traverses: Root → Chapter 1 → Section 1.1 → Leaf (F=ma)

# Multi-path query  
response = query_engine.query("Explain force and electromagnetic induction")
# Traverses: Root → Chapter 1 + Chapter 2 → Multiple sections → Multiple leaves
```

**Pros:**
- ✅ Efficient for large collections
- ✅ Natural hierarchical exploration
- ✅ Good for broad → specific queries
- ✅ Preserves relationships

**Cons:**
- ❌ Complex to build and maintain
- ❌ Requires good document structure
- ❌ Slower query time vs flat index

**Best For:**
- Large document collections (1000+)
- Hierarchical content (manuals, wikis)
- Multi-level queries
- Exploration and discovery

**When to Use:**
- You have 1000+ documents
- Documents have natural hierarchy
- Users ask broad then narrow down
- Browsing is important

**Real-World Use Cases:**

```
✓ Technical manuals and documentation
  Query: "Explain section 4.2 of the compliance policy"
  Structure: Manual → Chapters → Sections → Paragraphs
  Traverses: Root → Compliance Chapter → Section 4 → 4.2

✓ Legal document analysis
  Query: "What are the liability clauses?"
  Structure: Contract → Articles → Clauses → Sub-clauses
  Traverses: Root → Liability Article → Specific clauses

✓ Enterprise wiki search
  Query: "How does the authentication system work?"
  Structure: Wiki → Categories → Pages → Sections
  Traverses: Root → Engineering → Auth System → Details

✓ Textbook Q&A
  Query: "What is Newton's Second Law?"
  Structure: Textbook → Chapters → Sections → Paragraphs
  Traverses: Root → Physics → Mechanics → Newton's Laws
```

**Scale:** 1000+ documents with natural hierarchy

**Parameters:**

```python
TreeIndex.from_documents(
    docs,
    num_children=10,  # Branching factor (lower = deeper tree)
    build_tree=True,  # Auto-build hierarchy
    use_async=True  # Parallel construction
)
```

---

### 4. Keyword Table Index

**Description:** Extract keywords from each chunk, match query keywords.

**How It Works:**

```
Document: "Users report authentication failures after password reset"
Keywords: [authentication, failures, password, reset, users]

Query: "auth reset problem"
Keywords: [auth, reset, problem]

Match: auth→authentication ✓, reset✓, problem→failures✓
Score: 3/3 keywords matched
```

#### How Keywords Are Extracted

By default, LlamaIndex uses an LLM call to extract keywords:

```python
# LlamaIndex sends each document to the LLM with a prompt like:
"Extract keywords from the following text. Return as comma-separated list:
{document_text}"

# LLM returns: "authentication, password, reset, login, SSO, error"
```

**What gets stored (inverted index):**

```
Keyword → [Document IDs]
─────────────────────────
"password"  → [ticket_1, ticket_5, ticket_12]
"login"     → [ticket_1, ticket_3, ticket_8]
"timeout"   → [ticket_7, ticket_15]
"billing"   → [ticket_20, ticket_25]
```

**At query time:**
1. Extract keywords from query (also via LLM or simple tokenization)
2. Look up matching documents in the keyword table
3. Return documents that share keywords with the query

**Key difference from vector search:** No semantic understanding — "authentication" won't match "login" unless both keywords appear in the same document.

**Code:**

```python
from llama_index.core import KeywordTableIndex

# Build keyword index (uses LLM to extract keywords)
index = KeywordTableIndex.from_documents(docs)

# Query
query_engine = index.as_query_engine()
response = query_engine.query("password authentication")
```

**Pros:**
- ✅ No embeddings needed (faster, cheaper)
- ✅ Good for keyword-specific queries
- ✅ Exact term matching
- ✅ Works offline (no API calls)

**Cons:**
- ❌ No semantic understanding
- ❌ Misses synonyms ("car" != "vehicle")
- ❌ Poor for natural language queries
- ❌ Sensitive to wording

**Best For:**
- Code search (function names, error codes)
- Technical documentation
- ID/ticket number lookup
- Exact term matching

**When to Use:**
- You have structured data with IDs
- Queries use specific terminology
- Want to avoid embedding costs
- Offline operation needed

**Real-World Use Cases:**

```
✓ Ticket/Issue ID lookup
  Query: "TICK-001" or "JIRA-4532"
  Returns: Exact ticket with that ID

✓ Error code search
  Query: "HTTP 503 error" or "NullPointerException"
  Returns: Docs containing those exact error codes

✓ Code search
  Query: "function parseJSON" or "class UserAuthentication"
  Returns: Files containing those function/class names

✓ API endpoint lookup
  Query: "/api/v2/users/profile"
  Returns: Documentation for that exact endpoint

✓ Product SKU search
  Query: "SKU-78432-BLK"
  Returns: Product catalog entry
```

**Scale:** Any size, very fast, no LLM needed for retrieval

**Example Use Cases:**

```python
# Good queries for keyword index:
"TICK-001"  # Exact ID
"HTTP 503 error"  # Specific error code
"function parse_json"  # Code identifier

# Poor queries for keyword index:
"How do I fix login issues?"  # Natural language
"Problems with authentication"  # Synonyms
```

---

### 5. Hybrid Retrieval

**Description:** Combine multiple retrieval strategies for best results.

#### Why Hybrid?

Vector search and keyword search have complementary weaknesses:

| Search Type | Catches | Misses |
|---|---|---|
| Vector | Semantic matches ("login" ↔ "authentication") | Exact terms (ticket IDs, error codes) |
| Keyword | Exact matches ("TICK-001", "HTTP 503") | Synonyms, related concepts |

**Example:**

```
Query: "authentication timeout error TICK-001"

Vector Search finds:
  - "Login session expired after inactivity" (semantic match)
  - "SSO authentication failures" (semantic match)
  - MISSES "TICK-001" (not semantically similar)

Keyword Search finds:
  - "TICK-001: Auth service error" (exact match)
  - "timeout configuration issue" (keyword match)  
  - MISSES "Login session expired" (no keyword overlap)

Hybrid finds ALL of them → fewer missed results
```

**How It Works:**

```
Query: "authentication timeout"

Vector Search:     Keyword Search:
[Doc A: 0.89]      [Doc C: 3 keywords]
[Doc B: 0.85]      [Doc A: 2 keywords]
[Doc C: 0.75]      [Doc E: 1 keyword]

Fusion (RRF - Reciprocal Rank Fusion):
score(doc) = 1/(rank_vector + k) + 1/(rank_keyword + k)

Final Ranking:
[Doc A: 0.032]  # High in both → most confident
[Doc C: 0.029]  # Good in both
[Doc B: 0.015]  # Vector only
```

**Code:**

```python
# Simple hybrid approach
vector_index = VectorStoreIndex.from_documents(docs)
keyword_index = KeywordTableIndex.from_documents(docs)

# Retrieve from both
vector_nodes = vector_index.as_retriever(similarity_top_k=5).retrieve(query)
keyword_nodes = keyword_index.as_retriever().retrieve(query)

# Combine using RRF
def reciprocal_rank_fusion(results_list, k=60):
    scores = {}
    for results in results_list:
        for rank, node in enumerate(results, 1):
            node_id = node.node_id
            if node_id not in scores:
                scores[node_id] = {'node': node, 'score': 0}
            scores[node_id]['score'] += 1 / (rank + k)
    
    sorted_nodes = sorted(scores.values(), key=lambda x: x['score'], reverse=True)
    return [item['node'] for item in sorted_nodes]

# Get final results
hybrid_results = reciprocal_rank_fusion([vector_nodes, keyword_nodes])
```

**Pros:**
- ✅ Best of both worlds
- ✅ More robust to query variations
- ✅ Higher accuracy overall
- ✅ Reduces false negatives

**Cons:**
- ❌ Slower (runs multiple searches)
- ❌ More complex implementation
- ❌ Requires result fusion logic
- ❌ Higher computational cost

**Best For:**
- Production systems
- High-stakes applications
- Diverse query types
- Maximum accuracy required

**When to Use:**
- Accuracy > speed
- Mixed query types (natural + keywords)
- Users vary in query style
- Worth the extra cost

**Real-World Use Cases:**

```
✓ Production customer support
  Query: "auth error TICK-001"
  Vector finds: Related auth troubleshooting articles
  Keyword finds: Exact ticket TICK-001
  Combined: Both the specific ticket AND related solutions

✓ Enterprise search
  Query: "budget meeting Q3 2024"
  Vector finds: Semantically related budget discussions
  Keyword finds: Docs with exact "Q3 2024" mention
  Combined: Comprehensive results across both

✓ E-commerce product search
  Query: "comfortable running shoes size 10"
  Vector finds: Semantically similar athletic footwear
  Keyword finds: Products with exact "size 10" in specs
  Combined: Relevant products in the right size

✓ Medical/Legal search (high stakes)
  Query: "diabetes medication interactions"
  Vector finds: Related drug interaction articles
  Keyword finds: Exact drug names mentioned
  Combined: Can't afford to miss relevant results
```

**Scale:** Any size, but 2x retrieval cost
