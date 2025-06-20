"""
Business Example - YouTube Transcript Extractor
For content creators, consultants, and business applications
"""

from src.transcript_extractor import YouTubeTranscriptExtractor, AITrainingDataPreparer

def extract_business_content():
    """Extract transcripts for business and consulting use"""
    
    print("💼 Business Content Transcript Extraction")
    print("-" * 50)
    
    # Initialize the extractor
    extractor = YouTubeTranscriptExtractor()
    
    # Example business content URLs
    business_urls = [
        "https://youtube.com/watch?v=BUSINESS_VIDEO_1",
        "https://youtube.com/watch?v=TRAINING_VIDEO_2",
        "https://youtube.com/watch?v=TESTIMONIAL_VIDEO_3"
    ]
    
    print(f"🎯 Processing {len(business_urls)} business videos...")
    
    # Extract transcripts
    transcripts = extractor.extract_transcripts(business_urls)
    
    # Save for analysis
    extractor.save_transcripts(transcripts, format='csv', filename='business_transcripts')
    extractor.save_transcripts(transcripts, format='json', filename='business_transcripts')
    
    # Prepare for AI training
    ai_preparer = AITrainingDataPreparer(max_chunk_length=256)  # Smaller chunks for business use
    training_data = ai_preparer.prepare_for_training(transcripts)
    
    print("✅ Business transcripts ready!")
    print(f"📈 {len(training_data)} segments prepared for analysis")
    print("🚀 Perfect for:")
    print("   • Client testimonial analysis")
    print("   • Training material transcription")
    print("   • Content strategy insights")
    print("   • Custom AI assistant training")
    
    return transcripts, training_data

if __name__ == "__main__":
    extract_business_content()
