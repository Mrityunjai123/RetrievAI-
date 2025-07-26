from offline_rag import OfflineRAG

# Load the system
rag = OfflineRAG(persist_directory="./rag_storage")
rag.load()

# Check what's actually stored
print("Documents in metadata:")
for doc in rag.metadata["documents"]:
    print(f"- {doc['name']} ({doc['chunks']} chunks)")

print("\nChecking actual document chunks:")
# Check first few documents
for i, doc in enumerate(rag.documents[:5]):
    print(f"\nChunk {i}:")
    print(f"  Source: {doc.metadata.get('source', 'MISSING')}")
    print(f"  Content preview: {doc.page_content[:50]}...")