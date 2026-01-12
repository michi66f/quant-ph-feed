# quant-ph-feed

This repository automatically collects newly published papers from the arXiv quant-ph category
and converts them into LLM-friendly text formats (Markdown and JSONL).

The goal is not precise statistical analysis, but lightweight, qualitative trend exploration
using generative AI tools such as NotebookLM or ChatGPT.

## Features

- Daily fetch of arXiv quant-ph "new" feed
- Metadata normalization via the arXiv API
- Output formats optimized for LLM ingestion
  - Weekly Markdown digests
  - JSONL for downstream processing
- Fully automated using GitHub Actions
- No database required

## Typical Use Cases

- Weekly or monthly trend overviews of quantum information research
- Topic clustering and qualitative analysis with LLMs
- Personal research digest and long-term archive

## Notes

- Only public metadata (title, authors, abstract, categories) is stored
- PDF files are not archived
- This repository is intended for research and educational use
