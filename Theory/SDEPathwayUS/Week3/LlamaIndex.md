# LlamaIndex

**LlamaIndex** (formerly known as GPT Index) is a Python library designed to **bridge large language models (LLMs) like GPT with your own data**. It’s particularly useful in building applications where you want the model to reason over structured or unstructured documents rather than just generate text from scratch. Think of it as a **data connector + indexing system for LLMs**.

## Purpose

LLMs like GPT are amazing at generating text but **don’t have memory of your local documents**. LlamaIndex helps by:

- **Ingesting data**: PDFs, Word docs, HTML, Markdown, or even SQL databases.  
- **Creating indices**: Organizing data in a way that the LLM can efficiently query.  
- **Querying intelligently**: Allowing LLMs to answer questions based on your data, not just general knowledge.

## Core Concepts

### Documents
Any piece of data you want your LLM to reason over. Examples:

- PDFs, text files  
- HTML pages  
- CSV/JSON data converted to text  

### Text Splitting / Chunking
Large documents are split into **smaller chunks** (paragraphs, semantic sections, or tokens) so the LLM can handle them efficiently.

- **Token-based splitting**: Break by number of words/tokens.  
- **Semantic splitting**: Break by paragraph, heading, or logical sections (MarkdownNodeParser, HTMLNodeParser).

> More about differences between these two chunkings in the section: Token-based Splitting VS Semantic Splitting

### Nodes / Nodes List
After splitting, each chunk is stored as a **node**.

### Index
A structured representation of nodes that allows **fast retrieval**:

- `VectorStoreIndex`: Uses embeddings + vector search.  
- `ListIndex`: Simple list of nodes.  
- `TreeIndex`: Hierarchical, preserves document structure.  
- `KeywordTableIndex`: Keyword-based search.  

### Vector Store
Converts each node into a **vector embedding** (numeric representation) using models like OpenAI embeddings.  
These embeddings are used for **semantic search**, so the LLM can find relevant chunks quickly.

### Querying
Once your index is ready, you can run queries like:

```python
response = index.query("What are the main benefits of this document?")
print(response)
```

The LLM retrieves the most relevant nodes and answers based on them.

## Token-based Splitting VS Semantic Splitting

When we say that `MarkdownNodeParser` or `HTMLNodeParser` **splits documents semantically**, it means that the splitting is based on the **natural structure and meaning of the content**, rather than just counting tokens or characters.

- **Token-based / sentence-based splitting:**  
  - Splits purely by size (e.g., every 512 tokens or every N sentences).  
  - Ignores the **meaning or hierarchy** of the text.  
  - Example: a paragraph about AI might be split in the middle of a sentence because it reached the token limit.  

- **Semantic splitting:**  
  - Splits based on the **logical structure of the content**.  
  - Preserves **paragraphs, headings, lists, and sections** as individual “nodes.”  
  - Each node corresponds to a **coherent idea**.  

### How it works in Markdown?

Example Markdown file:

```markdown
# Artificial Intelligence

AI is a field of computer science.

## Applications

AI is used in healthcare, finance, transportation.
```

- `MarkdownNodeParser` splits this into:
    1. Node for # Artificial Intelligence + its paragraph
    2. Node for ## Applications + its paragraph

- Each node is semantically meaningful — it’s a complete section or sub-section, not just a chunk of 512 tokens.

### How it works in HTML?

Example HTML snippet:

```html
<h1>Industrial Revolution</h1>
<p>The Industrial Revolution transformed societies.</p>
<h2>Innovations</h2>
<p>Steam engines and railways revolutionized transport.</p>
```

- `HTMLNodeParser` splits into:
    1. Node for `<h1>Industrial Revolution</h1>` + its paragraph
    2. Node for `<h2>Innovations</h2>` + its paragraph

- Each node preserves the semantic block, like a section of the webpage.

### Why semantic splitting is useful

- Keeps ideas intact, so the LLM can reason about complete concepts instead of partial fragments.
- Improves retrieval quality, because the embedding represents a full paragraph or section, not a cut-off token slice.
- Works well for summarization, Q&A, or structured knowledge extraction.

In short:

> Semantic splitting = breaking documents into meaningful sections (paragraphs, headings, lists) instead of arbitrary token chunks.

## Indexing techniques in LlamaIndex

## 1. Vector Store Index

Vector Store Index converts text chunks into **numerical vectors** (embeddings) and finds similar content using **mathematical similarity**.

### Traditional vs Vector Search

#### Traditional Keyword Search
```
Query: "machine learning algorithms"
Matches: Documents containing exact words "machine" AND "learning" AND "algorithms"
❌ Misses: "neural networks", "AI models", "deep learning"
❌ Poor semantic understanding
```

#### Vector Search
```
Query: "machine learning algorithms" → [0.2, 0.8, 0.1, 0.9, ...] (embedding)
Matches: Similar vectors regardless of exact words
✅ Finds: "neural networks", "AI models", "deep learning"
✅ Understands meaning, not just keywords
```

### How It Works

#### Step 1: Convert Text to Vectors
```python
embed_model = OpenAIEmbedding()
vector_index = VectorStoreIndex(nodes, embed_model=embed_model)
```
- Each chunk becomes a list of numbers (vector)
- Similar meaning = similar numbers
- Creates searchable vector database

#### Step 2: Query Processing
```python
query_engine = vector_index.as_query_engine(similarity_top_k=3)
response = query_engine.query("How does supervised learning work?")
```
- Convert question to vector
- Find chunks with most similar vectors
- Return top matches

### Example: Research Paper Collection

#### Document Chunks
```
Chunk A: "Supervised learning uses labeled training data to learn mappings"
Chunk B: "Convolutional neural networks excel at image classification tasks"
Chunk C: "Random forests combine multiple decision trees for better accuracy"
Chunk D: "The stock market opened higher today due to economic indicators"
```

#### Query: "What are classification techniques?"

**Vector Search Process:**
1. Query → Vector: [0.3, 0.7, 0.1, 0.9, ...]
2. Compare with all chunk vectors
3. **Most Similar**: Chunk A (supervised learning) + Chunk B (classification) + Chunk C (classification method)
4. **Irrelevant**: Chunk D (finance, not ML)

**Result**: Gets machine learning classification methods, filters out unrelated financial content!

### Key Benefits
1. **Semantic Understanding**: Finds meaning, not just keywords
2. **Flexible Queries**: Works with natural language questions
3. **Cross-Domain**: Can find similar concepts across different fields
4. **Robust**: Handles synonyms, paraphrasing, and typos

### When to Use Vector Store Index
✅ **Good for:**
- Research paper collections
- FAQ systems
- Customer support knowledge bases
- Content recommendation systems
- Multi-language documents

❌ **Not ideal for:**
- Exact reference lookups (like citations)
- When precise terminology is critical
- Very small document sets

### Simple Implementation
```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding

documents = SimpleDirectoryReader("./research_papers").load_data()
embed_model = OpenAIEmbedding()
vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
query_engine = vector_index.as_query_engine(similarity_top_k=3)
response = query_engine.query("What are the latest advances in neural networks?")
```

---

## 2. Tree Index

TreeIndex preserves document structure by creating **parent-child relationships** between chunks based on headers.

### Traditional vs TreeIndex Chunking

#### Traditional Chunking
```
Document broken into random pieces:
[Chunk 1] [Chunk 2] [Chunk 3] [Chunk 4]
❌ No relationships
❌ Context scattered
```

#### TreeIndex Chunking  
```
Document organized as tree:
Main Section
├── Subsection A
│   └── Details A
└── Subsection B
    └── Details B
✅ Maintains structure
✅ Preserves context
```

### How It Works

#### Step 1: Parse Document Structure
```python
md_parser = MarkdownNodeParser()
nodes = md_parser.get_nodes_from_documents(documents)
```
- Finds markdown headers (`#`, `##`, `###`)
- Creates nodes for each section
- Identifies hierarchy levels

#### Step 2: Build Tree Relationships
```python
tree_index = TreeIndex(nodes, embed_model=embed_model)
```
- Connects parent sections to child sections
- Creates tree structure internally
- Generates embeddings for each node

#### Step 3: Query with Context
```python
response = query_engine.query("What are the experimental results?")
```
- Finds relevant sections using embeddings
- **Includes parent sections for context**
- **Includes child sections for details**
- Assembles hierarchical answer

### Example: Research Paper

#### Document Structure
```markdown
# Deep Learning for Medical Diagnosis
## Abstract
## Introduction
### Problem Statement
### Previous Work
## Methodology
### Data Collection
### Model Architecture
## Results
### Accuracy Metrics
### Comparison with Baselines
## Conclusion
```

#### TreeIndex Creates
```
Deep Learning Paper (Root)
├── Abstract
├── Introduction
│   ├── Problem Statement
│   └── Previous Work
├── Methodology
│   ├── Data Collection
│   └── Model Architecture
└── Results
    ├── Accuracy Metrics
    └── Comparison with Baselines
```

#### When You Ask: "What were the experimental results?"

**Traditional chunking** might return:
- Random chunk: "...accuracy of 94.2%..."
- Missing context about what was tested

**TreeIndex** returns:
- **Parent context**: "Results" section overview
- **Specific details**: "Accuracy Metrics" + "Comparison with Baselines"
- **Background context**: Links to methodology
- **Structured answer** following paper's organization

### Key Benefits
1. **Context Preservation**: Keeps related sections together
2. **Smart Retrieval**: Finds both overview and details
3. **Structured Answers**: Follows document's logical flow
4. **Academic Navigation**: Ideal for research papers and reports

### When to Use TreeIndex
✅ **Good for:**
- Research papers
- Technical documentation
- Academic theses
- Government reports
- Any structured content with clear sections

❌ **Not ideal for:**
- Unstructured text
- Flat content without headers
- Conversational documents

### Simple Implementation
```python
from llama_index.core import TreeIndex
from llama_index.core.node_parser import MarkdownNodeParser

md_parser = MarkdownNodeParser()
nodes = md_parser.get_nodes_from_documents(documents)
tree_index = TreeIndex(nodes, embed_model=OpenAIEmbedding())
query_engine = tree_index.as_query_engine()
response = query_engine.query("What methodology was used?")
```

---

## 4. ListIndex

### Step 1: Create Simple Documents for Clear Understanding  

We start with 4 short, focused documents:  

- **Doc 1**: *Python is a programming language. It is easy to learn and widely used for web development.*  
- **Doc 2**: *Machine learning is a subset of AI. It uses algorithms to find patterns in data.*  
- **Doc 3**: *Databases store information. SQL is used to query and manage database records.*  
- **Doc 4**: *Cloud computing provides remote servers. It offers scalability and cost-effective solutions.*  

### Step 2: Creating **ListIndex** – Internal Process  

When you call:  

```python
list_index = ListIndex.from_documents(documents)
```

#### What happens internally:
1. Takes your documents: `[Doc1, Doc2, Doc3, Doc4]`  
2. Stores them as a **simple Python list** (no embeddings, no processing).  
3. Maintains **insertion order**: Doc1 → Doc2 → Doc3 → Doc4.  
4. No indexing, no optimization, no algorithms.  
5. Just a **plain sequential container**.  

**Simplified internal structure:**  

```text
ListIndex.docstore = {
  'doc_1': 'Python is a programming language...',
  'doc_2': 'Machine learning is a subset of AI...',
  'doc_3': 'Databases store information...',
  'doc_4': 'Cloud computing provides remote servers...'
}
```

### Step 3: Query Processing – How **ListIndex** Handles Queries  

When you ask:  
> *"What programming concepts are mentioned?"*  

**Steps:**  
1. Query received.  
2. Loads **Doc 1**: Python  
3. Loads **Doc 2**: Machine Learning  
4. Loads **Doc 3**: Databases  
5. Loads **Doc 4**: Cloud Computing  
6. Sends **ALL documents** to the LLM.  
7. LLM synthesizes the answer.  

✅ Always processes everything.  

### Step 4: Comparison with Other Indexes  

**Query:** *"Tell me about databases"*  

- **ListIndex**  
  - Loads Doc1 → Doc2 → Doc3 → Doc4  
  - Sends **all docs** to LLM  
  - ✅ Gets database info but also includes unrelated context  

- **VectorIndex**  
  - Converts query → embedding  
  - Finds **closest doc** (Doc 3)  
  - ✅ More efficient, only retrieves Doc 3  

- **KeywordIndex**  
  - Extracts keywords: *["databases"]*  
  - Finds Doc 3 only  
  - ✅ Exact match, no extra context  

### Step 5: Sequential Processing Behavior  

For **any query**, ListIndex always processes:  
**Doc1 → Doc2 → Doc3 → Doc4**  

Examples:  

- *"What is Python?"* → still processes all docs  
- *"Explain machine learning"* → still processes all docs  
- *"How do databases work?"* → still processes all docs  
- *"What are the benefits mentioned?"* → still processes all docs  

### Step 6: Performance Characteristics  

- **Document size**: `n`  
- **Processing Pattern**: Always sequential  
- **Time Complexity**: O(n)  
- **Space Complexity**: O(n)  

**Token Usage:**  
- Sends **all docs** to LLM for every query → more cost.  

✅ **Benefits**  
- Simple setup  
- Comprehensive (never misses info)  
- Deterministic  
- No embeddings/models needed  

❌ **Limitations**  
- Inefficient for large collections  
- Higher API cost  
- Slower response times  

### Step 7: When to Use ListIndex  

**Perfect for:**  
- Small collections (2–10 docs)  
- Prototyping / quick testing  
- Educational purposes  
- Ensuring nothing is missed  

**Avoid for:**  
- Large collections (100+ docs)  
- Production with high performance needs  
- Cost-sensitive apps  

**Examples:**  
- Personal notes  
- Small product catalog  
- Few company policies  
- Research papers (2–3)  
- Small FAQ system  

---

## 4. Summary Index

Summary Index stores chunks as a **sequential list** and processes **all chunks** during each query for comprehensive answers.

### How Summary Index vs Others Work

#### Summary Index Processing
```
Query: "Summarize the company's annual performance"
Process: Loads ALL chunks → LLM processes everything → Complete summary
✅ Comprehensive coverage
✅ No information missed
❌ Slow for large documents
```

#### Other Indexes (Vector/Tree)
```
Query: "Summarize the company's annual performance"
Process: Find top-k relevant chunks → Process selected pieces → Partial view
✅ Fast processing
❌ May miss some financial details
```

### How It Works

#### Step 1: Create Sequential List
```python
summary_index = SummaryIndex.from_documents(documents)
```
- Stores all chunks in order
- No filtering or selection
- Simple list structure

#### Step 2: Process All Chunks
```python
query_engine = summary_index.as_query_engine()
response = query_engine.query("What are the key financial highlights?")
```
- Loads every single chunk
- Sends all content to LLM
- Synthesizes comprehensive response

### Example: Annual Report Analysis

#### Document with 12 Quarterly Chunks
```
Chunk 1: Q1 Revenue and growth metrics
Chunk 2: Q1 Operating expenses breakdown
Chunk 3: Q2 Revenue and market expansion
Chunk 4: Q2 R&D investments and costs
Chunk 5: Q3 Revenue and new product launches
Chunk 6: Q3 Marketing and sales expenses
Chunk 7: Q4 Revenue and holiday performance
Chunk 8: Q4 Year-end operational costs
Chunk 9: Annual profit margins analysis
Chunk 10: Cash flow and liquidity position
Chunk 11: Future investment strategies
Chunk 12: Risk factors and market outlook
```

#### Query: "How did the company perform this year?"

**Summary Index Process:**
- Uses ALL 12 chunks
- Complete financial picture across all quarters
- Includes revenue, expenses, investments, risks
- Nothing gets filtered out
- Comprehensive but processes everything

**Vector Index Process:**
- Might use chunks 1, 5, 9, 10 (most relevant to "performance")
- Faster but might miss important cost details or risks

### Key Benefits
1. **Complete Coverage**: Never misses any information
2. **Comprehensive Answers**: Uses entire document context
3. **Simple Setup**: No complex configuration needed
4. **Perfect for Small Docs**: Ideal when you need everything

### When to Use Summary Index
✅ **Good for:**
- Annual reports and financial documents
- Executive summaries
- Complete document analysis
- Small document collections (under 20 pages)
- When missing information is costly

❌ **Not ideal for:**
- Large document libraries
- Quick specific queries
- When speed is important
- Targeted information search

### Simple Implementation
```python
from llama_index.core import SummaryIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./annual_reports").load_data()
summary_index = SummaryIndex.from_documents(documents)
query_engine = summary_index.as_query_engine()
response = query_engine.query("Provide complete financial performance summary")
```

---

## 5. Keyword Table Index

Keyword Table Index extracts **specific keywords** from chunks and matches **exact terms** in queries for precise retrieval.

### Keyword vs Semantic Search

#### Keyword Search
```
Query: "Python pandas DataFrame"
Matches: Chunks containing exactly "Python", "pandas", "DataFrame"
✅ Precise programming terms
✅ Exact function/library matching
❌ Misses similar concepts with different terminology
```

#### Semantic Search (Vector)
```
Query: "Python pandas DataFrame"
Matches: "data manipulation", "tabular data", "spreadsheet operations"
✅ Finds related concepts
❌ May miss specific pandas functions
```

### How It Works

#### Step 1: Extract Keywords
```python
keyword_index = KeywordTableIndex.from_documents(documents)
```
- Analyzes each chunk for important keywords
- Builds keyword → chunk mapping
- Creates lookup table for fast retrieval

#### Step 2: Query Matching
```python
query_engine = keyword_index.as_query_engine()
response = query_engine.query("numpy array indexing slicing")
```
- Extracts keywords from query: "numpy", "array", "indexing", "slicing"
- Finds chunks containing these exact terms
- Returns matching programming documentation

### Example: Programming Documentation

#### Document Chunks with Keywords
```
Chunk A: "NumPy array indexing with brackets and slicing operations"
Keywords: ["NumPy", "array", "indexing", "brackets", "slicing", "operations"]

Chunk B: "Pandas DataFrame merge join operations on multiple columns"
Keywords: ["Pandas", "DataFrame", "merge", "join", "operations", "columns"]

Chunk C: "Machine learning model evaluation metrics and performance"
Keywords: ["Machine", "learning", "model", "evaluation", "metrics", "performance"]
```

#### Query: "array slicing numpy"

**Keyword Matching:**
- Query keywords: ["array", "slicing", "numpy"]
- **Perfect Match**: Chunk A (3/3 keywords match, including "NumPy"≈"numpy")
- **No Match**: Chunk B (0/3 keywords match)
- **No Match**: Chunk C (0/3 keywords match)

**Result**: Returns exact NumPy array documentation, not pandas or ML content!

### Key Benefits
1. **Exact Matching**: Finds precise programming terms and functions
2. **Technical Precision**: Perfect for API documentation
3. **Fast Retrieval**: Direct keyword lookup
4. **Deterministic**: Consistent results for same queries

### When to Use Keyword Table Index
✅ **Good for:**
- Programming documentation
- API references
- Technical manuals with specific terms
- Medical/scientific documents with precise terminology
- Product catalogs with part numbers

❌ **Not ideal for:**
- Conceptual questions
- Natural language exploration
- When you need semantic understanding
- General knowledge queries

### Simple Implementation
```python
from llama_index.core import KeywordTableIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./programming_docs").load_data()
keyword_index = KeywordTableIndex.from_documents(documents)
query_engine = keyword_index.as_query_engine()
response = query_engine.query("pandas DataFrame groupby aggregation")
```

---

## 6. Property Graph Index

Property Graph Index builds a **knowledge graph** with entities and relationships to understand complex connections between concepts.

### Traditional Search vs Knowledge Graph

#### Traditional Search
```
Query: "Which authors collaborated on neural network research?"
Result: Separate chunks mentioning different authors and papers
❌ No clear collaboration connections
❌ Manual piecing together needed
```

#### Knowledge Graph Search
```
Query: "Which authors collaborated on neural network research?"
Graph: Dr. Smith → co-authored with → Dr. Johnson → published → "Deep Learning Paper"
✅ Clear collaboration relationships
✅ Connected research networks
```

### How It Works

#### Step 1: Extract Entities and Relationships
```python
property_graph_index = PropertyGraphIndex.from_documents(documents)
```
- LLM identifies entities (authors, papers, concepts, institutions)
- Extracts relationships between entities
- Builds connected knowledge graph

#### Step 2: Graph-Based Retrieval
```python
query_engine = property_graph_index.as_query_engine()
response = query_engine.query("What research topics is Dr. Smith working on?")
```
- Finds relevant entities and connections
- Traverses relationship paths
- Returns connected research information

### Example: Academic Research Database

#### Document Content
```
"Dr. Alice Smith from MIT published 'Neural Networks for Image Recognition' in 2023.
She collaborated with Dr. Bob Johnson from Stanford University. 
The paper cites previous work by Dr. Chen on convolutional architectures.
This research was funded by NSF Grant #12345 and used the ImageNet dataset."
```

#### Knowledge Graph Created
```
Entities:
- Dr. Alice Smith (Person/Researcher)
- MIT (Institution)
- "Neural Networks for Image Recognition" (Paper)
- Dr. Bob Johnson (Person/Researcher)
- Stanford University (Institution)
- Dr. Chen (Person/Researcher)
- NSF Grant #12345 (Funding)
- ImageNet (Dataset)

Relationships:
- Dr. Smith → affiliated_with → MIT
- Dr. Smith → authored → "Neural Networks..." paper
- Dr. Smith → collaborated_with → Dr. Johnson
- Dr. Johnson → affiliated_with → Stanford
- Paper → cites → Dr. Chen's work
- Paper → funded_by → NSF Grant #12345
- Paper → uses_dataset → ImageNet
```

#### Query: "Who are Dr. Smith's research collaborators?"

**Graph Traversal:**
1. Find "Dr. Smith" entity
2. Follow "collaborated_with" relationships
3. Discover Dr. Johnson connection
4. Include their institutional affiliations
5. Return complete collaboration network

### Key Benefits
1. **Relationship Discovery**: Finds hidden connections between entities
2. **Research Networks**: Maps academic collaborations and influences
3. **Multi-hop Queries**: Can find indirect relationships
4. **Structured Knowledge**: Organizes complex research landscapes

### When to Use Property Graph Index
✅ **Good for:**
- Academic research databases
- Citation networks and collaboration mapping
- News articles with people/organizations
- Business documents with stakeholder relationships
- Social network analysis
- Scientific literature with cross-references

❌ **Not ideal for:**
- Simple single-author documents
- When relationships aren't important
- Pure content summarization
- Straightforward Q&A scenarios

### Simple Implementation
```python
from llama_index.core import PropertyGraphIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./research_papers").load_data()
property_graph_index = PropertyGraphIndex.from_documents(documents)
query_engine = property_graph_index.as_query_engine()
response = query_engine.query("What are the research connections between universities?")
```

---

## 7. Composable Index

Composable Index **combines multiple indexing methods** to leverage the strengths of different approaches for complex retrieval needs.

### Single Index vs Composable Approach

#### Single Index Limitation
```
Vector Index: Great for "What is machine learning?" ✅
             Poor for "Show me pandas.DataFrame.merge()" ❌

Keyword Index: Great for "pandas.DataFrame.merge()" ✅
              Poor for "What is machine learning?" ❌

Tree Index: Great for "What's in the Methods section?" ✅
           Limited for cross-document queries ❌
```

#### Composable Solution
```
Composable Index = Vector + Keyword + Tree
Query routing: Conceptual questions → Vector
              Exact functions → Keyword
              Document structure → Tree
✅ Best of all approaches
```

### How It Works

#### Step 1: Create Multiple Indexes
```python
# Create individual indexes for different purposes
vector_index = VectorStoreIndex.from_documents(documents)  # Concepts
keyword_index = KeywordTableIndex.from_documents(documents)  # Exact terms
tree_index = TreeIndex(nodes)  # Structure
```

#### Step 2: Compose Together
```python
from llama_index.core import ComposableGraph

composable_index = ComposableGraph.from_indices(
    [vector_index, keyword_index, tree_index],
    index_summaries=[
        "for conceptual and semantic queries about programming",
        "for exact function and API lookups", 
        "for navigating documentation structure"
    ]
)
```

#### Step 3: Intelligent Query Routing
```python
query_engine = composable_index.as_query_engine()
response = query_engine.query("How do I use pandas merge() and what are joins?")
```
- Analyzes query: contains both exact function name and conceptual question
- Routes to multiple indexes: Keyword for "pandas merge()" + Vector for "joins"
- Combines results intelligently

### Example: Programming Documentation System

#### Multiple Index Setup
```
Vector Index: Conceptual understanding ("What is data manipulation?")
Keyword Index: Exact API references ("pandas.DataFrame.merge()")
Tree Index: Documentation navigation ("What's in the Tutorial section?")
Property Graph: Library dependencies and relationships
```

#### Different Query Types

**Query 1**: "What is data visualization?" (Conceptual)
- **Routes to**: Vector Index
- **Returns**: Semantic explanation of data visualization concepts, libraries, techniques

**Query 2**: "matplotlib.pyplot.scatter parameters" (Exact API)
- **Routes to**: Keyword Index
- **Returns**: Exact function documentation and parameter list

**Query 3**: "What's in the Getting Started guide?" (Structural)
- **Routes to**: Tree Index
- **Returns**: Hierarchical tutorial content and navigation

**Query 4**: "How does NumPy relate to Pandas?" (Relationships)
- **Routes to**: Property Graph Index
- **Returns**: Library dependency mapping and integration points

### Key Benefits
1. **Versatile**: Handles different types of programming questions
2. **Optimal Performance**: Uses best index for each query type
3. **Complete Coverage**: Doesn't miss information due to index limitations
4. **Smart Routing**: Automatically selects best approach for each question

### When to Use Composable Index
✅ **Good for:**
- Comprehensive documentation systems
- Multi-purpose knowledge bases
- Programming help systems
- Research platforms with varied users
- When you can't predict query patterns

❌ **Not ideal for:**
- Simple single-purpose applications
- When setup complexity outweighs benefits
- Limited computational resources
- Very specific, uniform use cases

### Simple Implementation
```python
from llama_index.core import VectorStoreIndex, KeywordTableIndex, ComposableGraph

documents = SimpleDirectoryReader("./programming_docs").load_data()

# Create specialized indexes
vector_index = VectorStoreIndex.from_documents(documents)  # For concepts
keyword_index = KeywordTableIndex.from_documents(documents)  # For exact terms

# Compose together
composable_index = ComposableGraph.from_indices(
    [vector_index, keyword_index],
    index_summaries=[
        "for conceptual programming questions and explanations",
        "for exact function names, APIs, and code references"
    ]
)

query_engine = composable_index.as_query_engine()
response = query_engine.query("Explain list comprehensions and show me the syntax")
```

---

## Quick Index Selection Guide

| Need | Best Index | Example Query |
|------|------------|---------------|
| **Concept search** | Vector Store | "What is machine learning?" |
| **Structured docs** | Tree | "What's in the Methods section?" |
| **Complete analysis** | Summary | "Summarize this financial report" |
| **Exact terms** | Keyword Table | "pandas.DataFrame.merge()" |
| **Relationships** | Property Graph | "Which authors collaborated?" |
| **Multiple needs** | Composable | "Explain joins and show SQL syntax" |

Choose based on your **document type** and **query patterns**!


## LlamaIndex vs LangChain

LlamaIndex and LangChain **both help build applications around LLMs**, but they serve slightly different purposes and operate at different layers.


### Purpose & Focus

| Feature | **LlamaIndex** | **LangChain** |
|---------|----------------|---------------|
| **Primary Focus** | Organizing and indexing **your documents/data** so an LLM can reason over it efficiently. | Building **complex LLM pipelines/workflows**, chaining multiple LLM calls, tools, and logic. |
| **Best For** | Retrieval-Augmented Generation (RAG) tasks: semantic search, document QA, summarization. | Orchestrating LLM tasks: summarization, code execution, API calls, multi-step reasoning. |
| **Data Handling** | Strong: supports text, PDFs, HTML, Markdown, CSV, SQL, and builds indices automatically. | Limited: mainly acts as a wrapper; you can connect data sources but indexing is not built-in. |
| **Indexing** | Core feature: `VectorStoreIndex`, `TreeIndex`, `ListIndex`, etc. | Not a core focus; typically integrate an external vector store (FAISS, Pinecone, etc.). |
| **LLM Abstraction** | Focused on querying **data-driven context**. | Focused on **chaining LLM calls and tool interactions**. |
| **Complex Pipelines** | Less emphasis on multi-step workflows; mainly retrieval + LLM. | Built for multi-step chains, agents, and tool orchestration. |

### How They Can Work Together

- **LlamaIndex feeds LangChain**:
  - LlamaIndex retrieves the relevant document chunks.
  - LangChain processes them in a chain (e.g., summarize → generate report → call API).
- **LangChain alone** can do RAG, but you’d need to handle **indexing, embeddings, and retrieval manually**.
- **LlamaIndex simplifies document-to-query workflows**; LangChain simplifies **complex LLM workflows**.

```
LlamaIndex = “Turn your documents into an LLM-friendly database.”

LangChain = “Create LLM workflows and chains that can use multiple tools, steps, and logic.”
```

```
Analogy:

LlamaIndex = Librarian → finds the right books.

LangChain = Teacher → decides what to do with the books (summarize, quiz, write a report).
```

---

## Colab Notebook

[LlamaIndex Colab Notebook](https://colab.research.google.com/drive/1vaRH3rtGWDGIQ-dVoXTcGT_YQiGfpXGT?usp=sharing)