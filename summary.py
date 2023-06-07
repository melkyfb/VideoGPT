def generate_summary(transcription):
    # Split the transcription into sections based on sentences or time intervals
    sections = transcription.split(". ")

    # Generate timestamps based on the number of sections
    duration = 10  # Set the duration of each section in seconds
    timestamps = [f"{i * duration}s - {(i+1) * duration}s" for i in range(len(sections))]

    # Combine the sections with their corresponding timestamps
    summary = "\n".join(f"{timestamps[i]}: {sections[i]}" for i in range(len(sections)))

    return summary
