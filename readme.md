# VideoGPT Documentation

This documentation provides information on how to use the Video Processing Script. The script is designed to retrieve a video URL, download the video, transcribe it, interact with ChatGPT for generating text, and generate a summary with timestamps. Here's how to get started:

## Requirements

- Python 3.x
- Google Cloud SDK (for transcription with Google Cloud Speech-to-Text)
- OpenAI API key (for interacting with ChatGPT)

## Installation

1. Clone the repository: `git clone https://github.com/MelkyFB/VideoGPT.git`
2. Navigate to the project directory: `cd repository`
3. Install the required dependencies: `pip install -r requirements.txt`

## Set Up Google Cloud SDK

To use the Google Cloud Speech-to-Text service for transcription, you need to set up the Google Cloud SDK. Here are the steps:

1. Create a Google Cloud project and enable the Speech-to-Text API.
2. Install the Google Cloud SDK by following the instructions in the official documentation: [Installing Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
3. Authenticate the SDK by running the command: `gcloud auth login`.
4. Set the project ID by running the command: `gcloud config set project YOUR_PROJECT_ID`, replacing `YOUR_PROJECT_ID` with your actual project ID.

## Set Up OpenAI API Key

To interact with ChatGPT, you need to obtain an OpenAI API key. Here's how you can set up your API key:

1. Create an OpenAI account if you haven't already: [OpenAI](https://www.openai.com/).
2. Follow the OpenAI documentation to get your API key: [OpenAI API Documentation](https://docs.openai.com/reference/authentication/).

## Usage

1. Run the script using the command: `python main.py <video_url> [--api_key API_KEY]`, where `<video_url>` is the URL of the video you want to process, and `--api_key API_KEY` is an optional argument to provide your OpenAI API key.
2. Follow the instructions and prompts displayed in the command-line interface.
3. Interact with ChatGPT by entering your questions or prompts when prompted.
4. Once the script finishes, the generated text and summary will be saved in separate text files.

## Script Files

- `main.py`: The main script that orchestrates the different functionalities of the project.
- `video_utils.py`: Contains utility functions for retrieving the video URL and downloading the video.
- `transcription.py`: Handles the transcription of the downloaded video using Google Cloud Speech-to-Text.
- `chatgpt.py`: Interacts with the OpenAI API to communicate with ChatGPT.
- `summary.py`: Generates a summary of the video with timestamps.
- `error_handling.py`: Contains error handling mechanisms and custom exception classes.
- `documentation.md`: The documentation file you are currently reading.
- `requirements.txt`: Contains the list of dependencies required for the project.

For any issues or questions, please refer to the project repository or contact the project maintainers.

