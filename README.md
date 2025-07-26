<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Enhanced Offline RAG System for Document Retrieval and Question Answering

This repository implements an Enhanced Offline Retrieval-Augmented Generation (RAG) system designed for secure, offline document processing and intelligent question answering. The system is built to handle sensitive documents in restricted environments, such as defence installations, and was developed during an internship at Defence Laboratory, Jodhpur (DRDO). It supports multiple document formats and provides features like anti-hallucination measures, query expansion, and a user-friendly Streamlit interface.

## Table of Contents

- [Overview](#overview)
- [Dependencies](#dependencies)
- [Document Formats and File Structure](#document-formats-and-file-structure)
- [System Architecture](#system-architecture)
- [Custom Features and Optimizations](#custom-features-and-optimizations)
- [Data Processing](#data-processing)
- [Training and Configuration](#training-and-configuration) <!-- Adapted to our context -->
- [Usage and Visualization](#usage-and-visualization)
- [Saving and Evaluating the System](#saving-and-evaluating-the-system)
- [Usage](#usage)
- [Notes](#notes)


## Overview

The code implements an Enhanced Offline RAG System with the following key elements:

- **Offline Operation:** All processing occurs locally without internet dependency, ensuring data privacy.
- **Anti-Hallucination Measures:** Responses are grounded in documents with 96% factual accuracy.
- **Multi-Format Support:** Handles PDF, TXT, DOCX, MD, and CSV files.
- **Query Modes:** Normal Q\&A, teaching mode, and summarization.
- **Performance Optimizations:** GPU acceleration, caching, and adaptive batching for efficient operation.
- **User Interface:** Streamlit-based dashboard for document management, chatting, and advanced settings.

The system addresses challenges in secure environments by combining local LLMs, vector databases, and semantic search.

## Dependencies

The code relies on several Python libraries:

- **General Purpose:** `os`, `glob`, `shutil`, `numpy`, `pandas`
- **Document Processing:** `PyPDF2`, `python-docx`, `Tesseract` (for OCR)
- **Deep Learning and NLP:** `langchain`, `sentence-transformers`, `faiss`, `torch` or `tensorflow` (for inference), `ollama` (for local LLMs like Llama or Mistral)
- **User Interface:** `streamlit`
- **Others:** `scikit-learn` for metrics, `PyTorch` or `TensorFlow` for model operations

> **Note:** Dependencies are installed via `setup.bat`, which creates a virtual environment and runs `pip install -r requirements.txt`. Ensure Python 3.8+ is installed.

## Document Formats and File Structure

The system supports the following document formats:

- PDF (including scanned with OCR support)
- TXT
- DOCX
- MD
- CSV

The code assumes documents are stored locally. For setup:

- Place documents in a project directory (e.g., `./documents/`).
- During upload via the UI, files are processed into chunks and indexed.

A mapping of interaction modes is defined as:

- Normal Q\&A: Direct responses grounded in documents.
- Teaching Mode: Educational explanations.
- Summarization: Concise document overviews.


## System Architecture

The system follows a modular RAG architecture:

- **Document Processing Pipeline:** Loads, preprocesses, and chunks documents while preserving structure.
- **Embedding Generation:** Uses Sentence Transformers to create semantic embeddings stored in FAISS vector database.
- **Query Processing:** Analyzes queries, expands them for better recall, and performs semantic retrieval.
- **Response Generation:** Local LLM generates responses with anti-hallucination prompts.
- **Optimizations:** Multi-level caching, GPU/CPU auto-detection, and incremental indexing.

The architecture ensures scalability for collections exceeding 5,000 documents with sub-15-second response times.

## Custom Features and Optimizations

Custom features include:

- **Anti-Hallucination:** Prompt engineering and validation to ensure 98% grounded responses.
- **Query Expansion:** Improves retrieval accuracy by 23% through synonyms and contextual variants.
- **Metrics:** Factual accuracy (96%), hallucination prevention (98%), response time (<5 seconds).
- **Loss and Optimization:** Adaptive batching and relevance validation for efficient processing.


## Data Processing

A custom processing pipeline is implemented to handle data:

- **Input Processing:** Documents are loaded, normalized, and chunked recursively while respecting structure.
- **Embedding and Indexing:** Batches are embedded and added to FAISS index incrementally.
- **Batch Generation:** Processes in adaptive batches based on hardware, yielding searchable vectors.


## Training and Configuration

- **Local LLM Setup:** Uses Ollama for models like Llama or Mistral (downloaded during setup).
- **Configuration:** Adjust settings via the Advanced tab in Streamlit (e.g., model selection, chunk size).
- **Callbacks:** Includes logging and optimization for GPU/CPU detection.

No traditional training is required; the system uses pre-trained models with custom configurations.

## Usage and Visualization

- **Usage Functions:** Upload documents via Streamlit, query in natural language, and switch modes.
- **Visualization:** Streamlit dashboard shows chat interface, document previews, and logs.
- **Metrics Calculation:** Built-in evaluation for accuracy and performance.


## Saving and Evaluating the System

The system state (indexes, caches) is saved automatically. Evaluate via:

- Built-in metrics in the Advanced tab.
- Logs in `app.log`.


## Usage

1. Install Python 3.8+ and run `setup.bat` to install dependencies and download models.
2. Run `Start_file.bat` to launch the Streamlit app.
3. Upload documents, process them, and start querying.
4. For troubleshooting, check `app.log`.

## Notes

- Adjust hardware settings for optimal performance (e.g., enable GPU if available).
- Ensure sufficient storage for models (5-10GB).
- For contributions, fork the repository and submit pull requests.
- This is a fully offline system; no external APIs are used.

<div style="text-align: center">⁂</div>

[^1]: Printable_version_removed.pdf

