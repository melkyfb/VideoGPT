class VideoProcessingError(Exception):
    pass

# Define specific exceptions for different error scenarios
class InvalidURL(VideoProcessingError):
    pass

class UnsupportedFormat(VideoProcessingError):
    pass

class TranscriptionError(VideoProcessingError):
    pass

# Handle specific error scenarios
def handle_invalid_url(url):
    raise InvalidURL(f"The URL '{url}' is invalid or inaccessible.")

def handle_unsupported_format(format):
    raise UnsupportedFormat(f"The video format '{format}' is not supported.")

def handle_transcription_error():
    raise TranscriptionError("An error occurred during transcription.")

