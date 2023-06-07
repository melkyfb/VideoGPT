# VideoGPT

VideoGPT is a Python script that leverages the OpenAI API to transcribe and summarize audio from videos or audio files. It also allows you to interact with the transcription using ChatGPT by asking questions related to the content.

## Features

- Transcribe audio from video files or standalone audio files using the OpenAI Whisper API.
- Save the transcription to a specified file or in the same folder as the input file.
- Summarize the transcription using the OpenAI API.
- Save the summary to a specified file or in the same folder as the input file.
- Interact with the transcription using ChatGPT by asking questions and receiving answers.

## Prerequisites

- Python 3.6 or higher
- OpenAI Python library (install with `pip install openai`)
- MoviePy library (install with `pip install moviepy`)
- Click library (install with `pip install click`)
- Or all of them with `pip install -r requirements.txt`
- ffmpeg library (required by MoviePy for video/audio manipulation) https://www.ffmpeg.org/download.html

## Usage

1. Clone the repository or download the source code.
2. Install the required dependencies: `pip install openai moviepy`.
3. Set up an OpenAI API key and export it as an environment variable:
    ```export OPENAI_API_KEY=your-api-key```
4. Run the script with the following command:
    ```python script.py --api-key your-api-key --language en-US /path/to/audio_or_video --transcription-path /path/to/save/transcription.txt --summary-path /path/to/save/summary.txt```

- `--api-key`: Your OpenAI API key.
- `--language`: (Optional) The language for the transcription (e.g., en-US).
- `/path/to/audio_or_video`: The path to the video or audio file.
- `--transcription-path`: (Optional) The path to save the transcription file. If not provided, it will be saved in the same folder as the input file with a timestamped filename.
- `--summary-path`: (Optional) The path to save the summary file. If not provided, it will be saved in the same folder as the input file with a timestamped filename.

5. Follow the on-screen instructions to view the transcription, summary, and interact with ChatGPT by asking questions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
