def capitalize_each_word(text: str) -> str:
    if not text:
        return text
    return " ".join(
        word[0].upper() + word[1:].lower() if word else ""
        for word in text.split(" ")
    )
