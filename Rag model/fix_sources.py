from offline_rag import OfflineRAG
from pathlib import Path

def fix_document_sources():
    """Fix incorrect source names in existing documents"""
    
    # Load the system
    rag = OfflineRAG(persist_directory="./rag_storage")
    rag.load()
    
    print("Current documents in system:")
    for doc in rag.metadata["documents"]:
        print(f"- {doc['name']}")
    
    # Mapping of wrong names to correct names
    name_fixes = {
        "deeplearningbook.pdf": "Ian Goodfellow, Yoshua Bengio, Aaron Courville - Deep Learning - (2017, MIT).pdf",
        "Advanced Topics in CNN and RNN.pdf": "2402.03300v3.pdf",  # or whichever is correct
    }
    
    # Fix in metadata
    for doc in rag.metadata["documents"]:
        if doc["name"] in name_fixes:
            old_name = doc["name"]
            new_name = name_fixes[old_name]
            doc["name"] = new_name
            print(f"Fixed metadata: {old_name} -> {new_name}")
    
    # Fix in document chunks
    fixed_count = 0
    for chunk in rag.documents:
        source = chunk.metadata.get("source", "")
        if source in name_fixes:
            chunk.metadata["source"] = name_fixes[source]
            fixed_count += 1
    
    print(f"Fixed {fixed_count} document chunks")
    
    # Rebuild vector store with corrected metadata
    if rag.documents:
        print("Rebuilding vector store...")
        rag.vector_store = FAISS.from_documents(
            documents=rag.documents,
            embedding=rag.embeddings
        )
        rag._create_qa_chain()
    
    # Save the fixes
    rag.save()
    print("✓ Fixes saved!")

if __name__ == "__main__":
    fix_document_sources()