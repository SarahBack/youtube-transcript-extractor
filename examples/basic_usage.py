"""
Basic Usage Example - YouTube Transcript Extractor
Simple example showing how to extract transcripts from YouTube videos
"""

from src.transcript_extractor import YouTubeTranscriptExtractor

def basic_extraction_example():
    """Basic example of extracting transcripts"""
    
    # Initialize the extractor
    extractor = YouTubeTranscriptExtractor()
    
    # Example YouTube URLs (replace with your actual videos)
    video_urls = [
        "https://youtube.com/watch?v=YOUR_VIDEO_ID_1",
        "https://youtube.com/watch?v=YOUR_VIDEO_ID_2"
    ]
    
    print("🎯 Starting basic transcript extraction...")
    
    # Extract transcripts
    transcripts = extractor.extract_transcripts(video_urls)
    
    # Save in different formats
    extractor.save_transcripts(transcripts, format='json', filename='basic_transcripts')
    extractor.save_transcripts(transcripts, format='txt', filename='basic_transcripts')
    
    print("✅ Basic extraction complete!")
    print("Check the 'output' directory for your transcript files.")
    
    return transcripts

if __name__ == "__main__":
    basic_extraction_example()
