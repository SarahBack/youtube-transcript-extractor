"""
Ministry Example - YouTube Transcript Extractor
Perfect for churches, ministries, and faith-based content creators
"""

from src.transcript_extractor import YouTubeTranscriptExtractor, AITrainingDataPreparer

def extract_sermon_transcripts():
    """Extract sermon transcripts for church ministry use"""
    
    print("⛪ Church Ministry Transcript Extraction")
    print("-" * 50)
    
    # Initialize the extractor
    extractor = YouTubeTranscriptExtractor()
    
    # Example church YouTube videos (replace with actual sermon URLs)
    sermon_urls = [
        "https://youtube.com/watch?v=SERMON_VIDEO_1",
        "https://youtube.com/watch?v=SERMON_VIDEO_2",
        "https://youtube.com/watch?v=SERMON_VIDEO_3"
    ]
    
    print(f"📹 Processing {len(sermon_urls)} sermon videos...")
    
    # Extract transcripts
    transcripts = extractor.extract_transcripts(sermon_urls)
    
    # Save for accessibility and study
    extractor.save_transcripts(transcripts, format='txt', filename='sermon_transcripts')
    extractor.save_transcripts(transcripts, format='json', filename='sermon_transcripts')
    
    # Prepare for AI training (custom GPT for sermon prep)
    ai_preparer = AITrainingDataPreparer()
    training_data = ai_preparer.prepare_for_training(transcripts)
    
    print("✅ Ministry transcripts ready!")
    print(f"📊 {len(training_data)} segments prepared for AI training")
    print("🎯 Perfect for:")
    print("   • Accessibility for hearing-impaired congregants")
    print("   • Sermon study materials")
    print("   • Custom GPT training for ministry")
    print("   • Content analysis and insights")
    
    return transcripts, training_data

if __name__ == "__main__":
    extract_sermon_transcripts()
