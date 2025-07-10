from huggingface_hub import InferenceClient

HF_TOKEN = "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"  # Make sure this stays private
client = InferenceClient("HuggingFaceH4/zephyr-7b-beta", token=HF_TOKEN)

def chatBot(query):
    try:
        # Handle empty input (e.g., silence from voice)
        if not query.strip():
            return "I didn't catch that. Could you please say it again?"

        messages = [
            {"role": "system", "content": "You are a helpful assistant named Jarvis. Keep your answers short and concise."},
            {"role": "user", "content": query}
        ]

        response = client.chat_completion(
            messages=messages,
            max_tokens=300,              # Reduced to avoid long replies
            temperature=0.7,
            stop=["[/ASS]"]              # Optional: stops when model outputs this token
        )

        reply = response.choices[0].message["content"]

        # Clean up unwanted formatting or tags
        reply = reply.replace("[/ASS]", "").replace("[ASS]", "").strip()

        # Limit response length for TTS (optional)
        if len(reply.split()) > 80:
            reply = ' '.join(reply.split()[:80]) + '...'

        print("[BOT]:", reply)
        return reply

    except Exception as e:
        import traceback
        print("❌ Error in chatBot():")
        traceback.print_exc()
        return "Sorry, I couldn't process that."
