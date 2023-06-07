import argparse
import os
from video_utils import retrieve_video_url, download_video
from transcription import transcribe_video
from chatgpt import interact_with_chatgpt
from summary import generate_summary
import error_handling

def main():
    parser = argparse.ArgumentParser(description="Video Processing Script")
    parser.add_argument("video_url", type=str, help="URL of the video")
    parser.add_argument("--api_key", type=str, help="OpenAI API key")
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("OPENAI_API_KEY")

    try:
        # Retrieve the video URL
        video_url = retrieve_video_url(args.video_url)

        # Download the video
        video_path = download_video(video_url)

        # Transcribe the video
        transcription = transcribe_video(video_path)

        # Interact with ChatGPT
        generated_text = interact_with_chatgpt(transcription, api_key)

        # Generate summary with timestamps
        summary = generate_summary(transcription)

        # Display generated text and save it
        print(generated_text)
        with open("generated_text.txt", "w") as file:
            file.write(generated_text)

        # Save summary with timestamps
        with open("summary.txt", "w") as file:
            file.write(summary)

    except error_handling.VideoProcessingError as e:
        print(f"An error occurred during video processing: {e}")
        # Handle the error gracefully

if __name__ == "__main__":
    main()