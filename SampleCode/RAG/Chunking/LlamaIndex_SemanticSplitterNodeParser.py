from wikipedia import page

article = page("Mahatma Gandhi")  # Use any public figure/topic
text = article.content
print(text[:1000])  # Preview

#  LlamaIndex: SemanticSplitterNodeParser (Optional if embeddings allowed)
# Here’s what it internally does:
    # 1. Splits text into candidate sentences/paragraphs
    # 2. Uses OpenAIEmbedding to get embedding vectors of each block
    # 3. Computes semantic similarity between nearby paragraphs
    # 4. Combines sentences/paragraphs that are close in meaning
    # 5. Returns Node objects, each representing one semantic chunk
    
from dotenv import load_dotenv
import os

load_dotenv()  # ✅ Load .env before anything else

from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.node_parser import SemanticSplitterNodeParser

# Initialize OpenAI embedding model (make sure your API key is set in the environment)
embed_model = OpenAIEmbedding()

# Create a semantic chunker using the embedding model
parser = SemanticSplitterNodeParser(embed_model=embed_model)

# The input must be a `Document` object, not raw text
from llama_index.core.schema import Document
document = Document(text=text)

# Get nodes from the document
nodes = parser.get_nodes_from_documents([document])

# Print the first 3 semantic chunks
for i, node in enumerate(nodes[:3]):
    print(f"--- Semantic Chunk {i+1} ---\n{node.text}\n")