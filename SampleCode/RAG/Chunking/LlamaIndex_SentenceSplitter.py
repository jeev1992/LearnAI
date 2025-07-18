from wikipedia import page

article = page("Mahatma Gandhi")  # Use any public figure/topic
text = article.content
print(text[:1000])  # Preview

# LlamaIndex: SentenceSplitter
from llama_index.core.node_parser import SentenceSplitter

splitter = SentenceSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks[:3]):
    print(f"--- Chunk {i+1} ---\n{chunk}\n")