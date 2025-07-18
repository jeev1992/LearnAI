from wikipedia import page

article = page("Mahatma Gandhi")  # Use any public figure/topic
text = article.content
print(text[:1000])  # Preview

# LangChain: RecursiveCharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks[:3]):
    print(f"--- Chunk {i+1} ---\n{chunk}\n")