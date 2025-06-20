"""
YouTube Transcript Extractor
AI-powered transcript extraction for ministry and business use
"""

import json
import csv
import os
import logging
import re
from typing import List, Dict, Optional, Union
import requests
from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
from .config import *

class YouTubeTranscriptExtractor:
    """Extract and process YouTube video transcripts for AI training and content analysis"""
    
    def __init__(self, output_dir: str = DEFAULT_OUTPUT_DIR):
        self.output_dir = output_dir
        self.setup_logging()
        self.ensure_output_directory()
    
    def setup_logging(self):
        """Configure logging for the extractor"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def ensure_output_directory(self):
        """Create output directory if it doesn't exist"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def extract_video_id(self, url: str) -> Optional[str]:
        """Extract video ID from various YouTube URL formats"""
        patterns = [
            r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([^&\n?#]+)',
            r'(?:https?://)?(?:www\.)?youtu\.be/([^&\n?#]+)',
            r'(?:https?://)?(?:www\.)?youtube\.com/embed/([^&\n?#]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None
    
    def clean_transcript_text(self, text: str) -> str:
        """Clean transcript text for AI training"""
        # Remove content in brackets/parentheses
        text = re.sub(r'\[.*?\]', '', text)
        text = re.sub(r'\(.*?\)', '', text)
        
        # Clean up spacing and newlines
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    def extract_single_transcript(self, video_id: str) -> Optional[Dict]:
        """Extract transcript from a single video"""
        try:
            self.logger.info(f"Extracting transcript for video: {video_id}")
            
            # Get transcript
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            
            # Process transcript
            full_text = ""
            processed_segments = []
            
            for entry in transcript_list:
                cleaned_text = self.clean_transcript_text(entry['text'])
                full_text += cleaned_text + " "
                
                processed_segments.append({
                    'start': entry['start'],
                    'duration': entry.get('duration', 0),
                    'text': cleaned_text
                })
            
            return {
                'video_id': video_id,
                'full_text': full_text.strip(),
                'segments': processed_segments,
                'total_segments': len(processed_segments),
                'status': 'success'
            }
            
        except Exception as e:
            self.logger.error(f"Failed to extract transcript for {video_id}: {str(e)}")
            return {
                'video_id': video_id,
                'error': str(e),
                'status': 'failed'
            }
    
    def extract_transcripts(self, urls: List[str]) -> Dict[str, Dict]:
        """Extract transcripts from multiple YouTube URLs"""
        results = {}
        
        for url in urls:
            video_id = self.extract_video_id(url)
            if video_id:
                result = self.extract_single_transcript(video_id)
                results[video_id] = result
            else:
                self.logger.warning(f"Could not extract video ID from URL: {url}")
                results[url] = {
                    'error': 'Invalid YouTube URL',
                    'status': 'failed'
                }
        
        return results
    
    def save_transcripts(self, transcripts: Dict, format: str = 'json', filename: str = 'transcripts'):
        """Save transcripts in specified format"""
        if format not in SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported format: {format}. Use one of {SUPPORTED_FORMATS}")
        
        filepath = os.path.join(self.output_dir, f"{filename}.{format}")
        
        if format == 'json':
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(transcripts, f, indent=2, ensure_ascii=False)
        
        elif format == 'txt':
            with open(filepath, 'w', encoding='utf-8') as f:
                for video_id, data in transcripts.items():
                    if data.get('status') == 'success':
                        f.write(f"Video ID: {video_id}\n")
                        f.write(f"Full Text: {data['full_text']}\n")
                        f.write("-" * 80 + "\n\n")
        
        elif format == 'csv':
            rows = []
            for video_id, data in transcripts.items():
                if data.get('status') == 'success':
                    for segment in data.get('segments', []):
                        rows.append({
                            'video_id': video_id,
                            'start_time': segment['start'],
                            'duration': segment['duration'],
                            'text': segment['text']
                        })
            
            df = pd.DataFrame(rows)
            df.to_csv(filepath, index=False, encoding='utf-8')
        
        self.logger.info(f"Transcripts saved to: {filepath}")
        return filepath


class AITrainingDataPreparer:
    """Prepare transcript data specifically for AI training"""
    
    def __init__(self, max_chunk_length: int = 512):
        self.max_chunk_length = max_chunk_length
    
    def chunk_text(self, text: str) -> List[str]:
        """Split text into chunks suitable for AI training"""
        words = text.split()
        chunks = []
        current_chunk = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= self.max_chunk_length:
                current_chunk.append(word)
                current_length += len(word) + 1
            else:
                if current_chunk:
                    chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                current_length = len(word)
        
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
    
    def prepare_for_training(self, transcripts: Dict) -> List[Dict]:
        """Prepare transcripts for AI training"""
        training_data = []
        
        for video_id, data in transcripts.items():
            if data.get('status') == 'success':
                text_chunks = self.chunk_text(data['full_text'])
                
                for i, chunk in enumerate(text_chunks):
                    training_data.append({
                        'video_id': video_<span class="cursor">█</span>"""
YouTube Transcript Extractor
AI-powered transcript extraction for ministry and business use
"""

import json
import csv
import os
import logging
import re
from typing import List, Dict, Optional, Union
import requests
from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
from .config import *

class YouTubeTranscriptExtractor:
    """Extract and process YouTube video transcripts for AI training and content analysis"""
    
    def __init__(self, output_dir: str = DEFAULT_OUTPUT_DIR):
        self.output_dir = output_dir
        self.setup_logging()
        self.ensure_output_directory()
    
    def setup_logging(self):
        """Configure logging for the extractor"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def ensure_output_directory(self):
        """Create output directory if it doesn't exist"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def extract_video_id(self, url: str) -> Optional[str]:
        """Extract video ID from various YouTube URL formats"""
        patterns = [
            r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([^&\n?#]+)',
            r'(?:https?://)?(?:www\.)?youtu\.be/([^&\n?#]+)',
            r'(?:https?://)?(?:www\.)?youtube\.com/embed/([^&\n?#]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None
    
    def clean_transcript_text(self, text: str) -> str:
        """Clean transcript text for AI training"""
        # Remove content in brackets/parentheses
        text = re.sub(r'\[.*?\]', '', text)
        text = re.sub(r'\(.*?\)', '', text)
        
        # Clean up spacing and newlines
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    def extract_single_transcript(self, video_id: str) -> Optional[Dict]:
        """Extract transcript from a single video"""
        try:
            self.logger.info(f"Extracting transcript for video: {video_id}")
            
            # Get transcript
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            
            # Process transcript
            full_text = ""
            processed_segments = []
            
            for entry in transcript_list:
                cleaned_text = self.clean_transcript_text(entry['text'])
                full_text += cleaned_text + " "
                
                processed_segments.append({
                    'start': entry['start'],
                    'duration': entry.get('duration', 0),
                    'text': cleaned_text
                })
            
            return {
                'video_id': video_id,
                'full_text': full_text.strip(),
                'segments': processed_segments,
                'total_segments': len(processed_segments),
                'status': 'success'
            }
            
        except Exception as e:
            self.logger.error(f"Failed to extract transcript for {video_id}: {str(e)}")
            return {
                'video_id': video_id,
                'error': str(e),
                'status': 'failed'
            }
    
    def extract_transcripts(self, urls: List[str]) -> Dict[str, Dict]:
        """Extract transcripts from multiple YouTube URLs"""
        results = {}
        
        for url in urls:
            video_id = self.extract_video_id(url)
            if video_id:
                result = self.extract_single_transcript(video_id)
                results[video_id] = result
            else:
                self.logger.warning(f"Could not extract video ID from URL: {url}")
                results[url] = {
                    'error': 'Invalid YouTube URL',
                    'status': 'failed'
                }
        
        return results
    
    def save_transcripts(self, transcripts: Dict, format: str = 'json', filename: str = 'transcripts'):
        """Save transcripts in specified format"""
        if format not in SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported format: {format}. Use one of {SUPPORTED_FORMATS}")
        
        filepath = os.path.join(self.output_dir, f"{filename}.{format}")
        
        if format == 'json':
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(transcripts, f, indent=2, ensure_ascii=False)
        
        elif format == 'txt':
            with open(filepath, 'w', encoding='utf-8') as f:
                for video_id, data in transcripts.items():
                    if data.get('status') == 'success':
                        f.write(f"Video ID: {video_id}\n")
                        f.write(f"Full Text: {data['full_text']}\n")
                        f.write("-" * 80 + "\n\n")
        
        elif format == 'csv':
            rows = []
            for video_id, data in transcripts.items():
                if data.get('status') == 'success':
                    for segment in data.get('segments', []):
                        rows.append({
                            'video_id': video_id,
                            'start_time': segment['start'],
                            'duration': segment['duration'],
                            'text': segment['text']
                        })
            
            df = pd.DataFrame(rows)
            df.to_csv(filepath, index=False, encoding='utf-8')
        
        self.logger.info(f"Transcripts saved to: {filepath}")
        return filepath


class AITrainingDataPreparer:
    """Prepare transcript data specifically for AI training"""
    
    def __init__(self, max_chunk_length: int = 512):
        self.max_chunk_length = max_chunk_length
    
    def chunk_text(self, text: str) -> List[str]:
        """Split text into chunks suitable for AI training"""
        words = text.split()
        chunks = []
        current_chunk = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= self.max_chunk_length:
                current_chunk.append(word)
                current_length += len(word) + 1
            else:
                if current_chunk:
                    chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                current_length = len(word)
        
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
    
    def prepare_for_training(self, transcripts: Dict) -> List[Dict]:
        """Prepare transcripts for AI training"""
        training_data = []
        
        for video_id, data in transcripts.items():
            if data.get('status') == 'success':
                text_chunks = self.chunk_text(data['full_text'])
                
                for i, chunk in enumerate(text_chunks):
                    training_data.append({
                        'video_id': video_<span class="cursor">█</span>
