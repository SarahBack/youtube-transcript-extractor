from src.transcript_extractor import YouTubeTranscriptExtractor

# Initialize the extractor
extractor = YouTubeTranscriptExtractor()

# Test with a simple video
test_urls = ["https://youtu.be/90mj79GqWhc?si=vsV7zFMErNt7uVSV"]

print("Starting test...")

# Extract transcripts
transcripts = extractor.extract_transcripts(test_urls)

# Print results
print("Results:")
print(transcripts)

print("Test complete!")
