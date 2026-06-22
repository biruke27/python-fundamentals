"""
Day 5-6: Dictionaries and Sets

Spec (see ../../fundamentals/01_core_python/README.md for full details):

- Given a list of meeting transcripts (multi-sentence strings), split each
  into words (`.lower().split()`) and build a dictionary of word
  frequencies.
- Print the 5 most common words, excluding this stop-word set:
    {"the", "a", "and", "to", "of", "in", "is"}
- Separately, use a set to collect all unique action-item keywords found
  across the transcripts (e.g. "need", "follow", "action") by checking
  which appear.
"""

STOP_WORDS = {"the", "a", "and", "to", "of", "in", "is"}
ACTION_KEYWORDS = {"need", "follow", "action"}


def build_word_frequencies(transcripts):
    """Return a dict of {word: count} across all transcripts, excluding stop words."""
    # TODO: implement
    word_counts = {}
    
    for transcript in transcripts:
        clean_text = transcript.lower().replace(".","").replace("!","")
        words = clean_text.split()
        
        for word in words:
            if word not in STOP_WORDS:
                word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def find_action_keywords(transcripts):
    """Return a set of action-item keywords that appear anywhere in transcripts."""
    # TODO: implement
    found_keywords = set()
    for transcript in transcripts:
        clean_text = transcript.lower().replace(".","").replace("!","")
        words = clean_text.split()

        for word in words:
            if word in ACTION_KEYWORDS:
                found_keywords.add(word)
    return found_keywords 


def main():
    transcripts = [
        "We need to follow up on the budget before Friday.",
        "The team decided the launch date is final.",
        "I need an action plan for the marketing campaign.",
        "Please follow the instructions and prepare the report.",
        "The manager said we need immediate action on this issue.",
        "Our team will follow up with the client next week.",
        "We need to review the project timeline before taking action.",
        "The action items are clear and we need to start immediately.",
        "I will follow the checklist and update the team tomorrow."
        # TODO: add a couple more sample transcripts of your own
    ]

    # TODO: call build_word_frequencies, print top 5 words
    # TODO: call find_action_keywords, print the resulting set

    # 1. Processing Word Frequencies
    frequencies = build_word_frequencies(transcripts)

    # Sorting the dict items by value in descending order
    sorted_words = sorted(
        frequencies.items(), key=lambda item: item[1], reverse=True
    )
    top_5 = sorted_words[:5]

    print("--- TOP 5 MOST COMMON WORDS ---")
    for word, count in top_5:
        print(f"'{word}': appears {count} times")

    # 2. Extracting Target Action Items
    detected_tags = find_action_keywords(transcripts)

    print("\n--- UNIQUE TAGS FOUND ---")
    print(detected_tags)


if __name__ == "__main__":
    main()
