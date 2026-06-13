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
    return {}


def find_action_keywords(transcripts):
    """Return a set of action-item keywords that appear anywhere in transcripts."""
    # TODO: implement
    return set()


def main():
    transcripts = [
        "We need to follow up on the budget before Friday.",
        "The team decided the launch date is final.",
        # TODO: add a couple more sample transcripts of your own
    ]

    # TODO: call build_word_frequencies, print top 5 words
    # TODO: call find_action_keywords, print the resulting set


if __name__ == "__main__":
    main()
