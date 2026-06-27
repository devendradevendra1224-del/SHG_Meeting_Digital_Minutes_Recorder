def generate_minutes(text):
    sentences = text.split('.')

    minutes = "MEETING MINUTES\n\n"

    for i, sentence in enumerate(sentences, start=1):
        if sentence.strip():
            minutes += f"{i}. {sentence.strip()}\n"

    return minutes
