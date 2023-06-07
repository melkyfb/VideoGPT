import openai

def interact_with_chatgpt(transcription):
    # Set up OpenAI API client
    openai.api_key = "YOUR_API_KEY"

    # Set the chat prompt
    prompt = f"Video transcription:\n{transcription}\n\nUser:"

    # Initialize the conversation history
    conversation_history = []

    # Start the conversation loop
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break

        # Add the user's input to the conversation history
        conversation_history.append(f"User: {user_input}")

        # Generate a response from ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt + "\n" + "\n".join(conversation_history),
            max_tokens=50,
            n=1,
            stop=None,
        )

        # Extract the generated text from the response
        generated_text = response.choices[0].text.strip()

        # Display the generated text
        print("ChatGPT:", generated_text)

        # Add ChatGPT's response to the conversation history
        conversation_history.append(f"ChatGPT: {generated_text}")

    # Return the generated text
    return generated_text
