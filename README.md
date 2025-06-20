# YouTube Transcript Extractor 🎯

> AI-powered transcript extraction for content creators, ministries, and businesses from your Faith Tech Strategist Sarah DeLane Back

Transform YouTube content into structured, AI-ready transcripts with a single click. Perfect for training custom GPTs, creating accessible content, and analyzing video content at scale.

## ✨ Features

- **Bulk Processing** - Extract from multiple videos or entire channels
- **AI-Ready Output** - Clean, structured transcripts perfect for training
- **Multiple Formats** - JSON, TXT, and CSV export options
- **Ministry-Focused** - Ideal for sermon transcripts and church content
- **Error Handling** - Robust processing with detailed error reporting
- **Simple Interface** - One-click extraction from YouTube URLs

## 🚀 Quick Start

```python
from src.transcript_extractor import YouTubeTranscriptExtractor

extractor = YouTubeTranscriptExtractor()
transcripts = extractor.extract_transcripts([
    "https://youtube.com/watch?v=YOUR_VIDEO_ID"
])
