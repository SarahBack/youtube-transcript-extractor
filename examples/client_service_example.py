"""
Client Service Example - YouTube Transcript Extractor
Template for offering transcript extraction as a service
"""

from src.transcript_extractor import YouTubeTranscriptExtractor, AITrainingDataPreparer
import json

def process_client_channel(client_name, video_urls, service_type="standard"):
    """Process a client's YouTube content with professional service delivery"""
    
    print(f"🎯 Processing content for: {client_name}")
    print(f"📋 Service type: {service_type}")
    print("-" * 60)
    
    # Initialize extractor
    extractor = YouTubeTranscriptExtractor()
    
    # Extract transcripts
    print(f"📹 Processing {len(video_urls)} videos...")
    transcripts = extractor.extract_transcripts(video_urls)
    
    # Count successful extractions
    successful = sum(1 for t in transcripts.values() if t.get('status') == 'success')
    failed = len(transcripts) - successful
    
    # Save client deliverables
    client_filename = f"{client_name.lower().replace(' ', '_')}_transcripts"
    
    if service_type == "premium":
        # Premium service includes all formats
        extractor.save_transcripts(transcripts, format='json', filename=client_filename)
        extractor.save_transcripts(transcripts, format='txt', filename=client_filename)
        extractor.save_transcripts(transcripts, format='csv', filename=client_filename)
        
        # AI training data preparation
        ai_preparer = AITrainingDataPreparer()
        training_data = ai_preparer.prepare_for_training(transcripts)
        
        # Save training data
        with open(f'output/{client_filename}_ai_training.json', 'w') as f:
            json.dump(training_data, f, indent=2)
            
    else:
        # Standard service - JSON and TXT
        extractor.save_transcripts(transcripts, format='json', filename=client_filename)
        extractor.save_transcripts(transcripts, format='txt', filename=client_filename)
    
    # Generate client report
    print("\n📊 CLIENT DELIVERY REPORT")
    print("=" * 40)
    print(f"Client: {client_name}")
    print(f"Total videos processed: {len(video_urls)}")
    print(f"Successfully extracted: {successful}")
    print(f"Failed extractions: {failed}")
    
    if service_type == "premium":
        print(f"AI training segments: {len(training_data)}")
        print("Formats delivered: JSON, TXT, CSV, AI Training Data")
    else:
        print("Formats delivered: JSON, TXT")
    
    print(f"Files saved with prefix: {client_filename}")
    print("✅ Client delivery complete!")
    
    return transcripts

# Example client processing
if __name__ == "__main__":
    # Example: Premium service for a ministry client
    ministry_urls = [
        "https://youtube.com/watch?v=EXAMPLE1",
        "https://youtube.com/watch?v=EXAMPLE2"
    ]
    
    process_client_channel("Grace Community Church", ministry_urls, "premium")
