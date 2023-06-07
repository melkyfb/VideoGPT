import click
import openai
import os
import io
from pydub import AudioSegment
from datetime import datetime

@click.command()
@click.option("--api-key", default="", help="OpenAI API key")
@click.option("--language", default="", help="Language for transcription")
@click.argument("audio_or_video_path", type=click.Path(exists=True))
@click.argument("transcription_path", type=click.Path(), required=False)
@click.argument("summary_path", type=click.Path(), required=False)
def summarize_transcription(api_key, language, audio_or_video_path, transcription_path, summary_path):
    try:
        openai.api_key = api_key or os.environ["OPENAI_API_KEY"]

        if audio_or_video_path.lower().endswith((".mp4", ".avi", ".mov")):
            # Extract audio from video
            audio_path = "extracted_audio.mp3"
            audio = AudioSegment.from_file(audio_or_video_path)
            audio.export(audio_path, format="mp3")
        else:
            audio_path = audio_or_video_path

        transcription = openai.Audio.transcribe('whisper-1', io.open(audio_path, 'rb')).text

        if transcription:
            print("Transcription completed successfully:")
            print(transcription)

            # Save the transcription to the specified file or in the same folder as the audio/video file
            if not transcription_path:
                audio_or_video_dir = os.path.dirname(audio_or_video_path)
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                transcription_path = os.path.join(audio_or_video_dir, f"transcription_{timestamp}.txt")
            with open(transcription_path, "w") as f:
                f.write(transcription)
            print("Transcription saved to:", transcription_path)

            # Summarize the transcription using the OpenAI API
            summary_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=1,
                messages = [
                    {
                        "role": "system",
                        "content": "You are a professional summarizer and you will summarize transcriptions provided by the user."
                    }, {
                        "role": "user",
                        "content": "Please summarize the following transcription including bullet points for each topic: {}".format(transcription)
                    }
                ]
            )
            summary = summary_response['choices'][0]['message']['content']

            if summary:
                print("Summary completed successfully:")
                print(summary)
                # Save the summary to the specified file or in the same folder as the audio/video file
                if not summary_path:
                    audio_or_video_dir = os.path.dirname(audio_or_video_path)
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    summary_path = os.path.join(audio_or_video_dir, f"summary_{timestamp}.txt")
                with open(summary_path, "w") as f:
                    f.write(summary)
                print("Summary saved to:", summary_path)
            else:
                print("Failed to generate a summary.")

            # Ask questions related to the transcription
            while True:
                question = input("Ask ChatGPT (Enter 'I want to quit' to exit): ")
                if question.lower() == "i want to quit":
                    break
                question_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    temperature=1,
                    messages = [
                        {
                            "role": "system",
                            "content": "You will read the following text and respond the questions that the user ask: {}".format(transcription)
                        }, {
                            "role": "user",
                            "content": question
                        }
                    ]
                )
                response_content = question_response['choices'][0]['message']['content']
                print("Answer:", response_content)
        else:
            print("Failed to transcribe audio.")

        if audio_or_video_path != audio_path:
            os.remove(audio_path)

    except Exception as e:
        print("An error occurred during audio transcription:")
        print(str(e))

if __name__ == "__main__":
    summarize_transcription()
