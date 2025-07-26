import os
import sys

# Set environment variables
os.environ['TF_USE_LEGACY_KERAS'] = '1'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

print("📥 Downloading embedding models for offline use...")
print("This will download models to use offline later.\n")

try:
    # Use the new import
    from langchain_community.embeddings import HuggingFaceEmbeddings
    
    # Create cache directory
    cache_dir = "./models/embeddings"
    os.makedirs(cache_dir, exist_ok=True)
    
    # Download the model
    print("Downloading sentence-transformers/all-MiniLM-L6-v2...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        cache_folder=cache_dir
    )
    
    # Test it
    test_text = "This is a test"
    result = embeddings.embed_query(test_text)
    print(f"✅ Model downloaded successfully! Embedding dimension: {len(result)}")
    print(f"📁 Model saved in: {os.path.abspath(cache_dir)}")
    
except ImportError as e:
    print(f"Import error: {e}")
    print("\nInstalling required packages...")
    os.system("pip install langchain-community sentence-transformers")
    print("\nPlease run this script again after installation.")
    
except Exception as e:
    print(f"Error: {e}")