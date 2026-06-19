# --- GLOBAL FILTERS ---
STOP_WORDS = {"the", "a", "and", "to", "of", "in", "is"}
ACTION_KEYWORDS = {"refund", "billing", "urgent", "locked"}  # Using our chat tags


def build_word_frequencies(transcripts):
    """Return a dict of {word: count} across all transcripts, excluding stop words."""
    word_counts = {}

    for transcript in transcripts:
        # Standardize and clean the punctuation just like the spec recommends
        clean_text = transcript.lower().replace(".", "").replace("!", "")
        words = clean_text.split()

        for word in words:
            # Check if it should be ignored
            if word not in STOP_WORDS:
                # Safe dictionary lookup using .get()
                word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def find_action_keywords(transcripts):
    """Return a set of action-item keywords that appear anywhere in transcripts."""
    found_keywords = set()

    for transcript in transcripts:
        clean_text = transcript.lower().replace(".", "").replace("!", "")
        words = clean_text.split()

        for word in words:
            # Membership verification using 'in' with our target set
            if word in ACTION_KEYWORDS:
                # Dynamically append to our unique tracker
                found_keywords.add(word)

    return found_keywords


def main():
    # Simulated customer support transcripts instead of meeting data
    chat_transcripts = [
        "I need a refund immediately. The billing process is broken.",
        "Can you help with billing? I need to update my card details.",
        "This is urgent! My account is locked and I need a response.",
    ]

    # 1. Processing Word Frequencies
    frequencies = build_word_frequencies(chat_transcripts)

    # Sorting the dict items by value in descending order
    sorted_words = sorted(
        frequencies.items(), key=lambda item: item[1], reverse=True
    )
    top_5 = sorted_words[:5]

    print("--- TOP 5 MOST COMMON WORDS ---")
    for word, count in top_5:
        print(f"'{word}': appears {count} times")

    # 2. Extracting Target Action Items
    detected_tags = find_action_keywords(chat_transcripts)

    print("\n--- UNIQUE TAGS FOUND ---")
    print(detected_tags)


if __name__ == "__main__":
    main()