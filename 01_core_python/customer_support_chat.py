# 1. Input Data: A list of multi-sentence support chats
chat_transcripts = [
    "I need a refund immediately. The billing process is broken.",
    "Can you help with billing? I need to update my card details.",
    "This is urgent! My account is locked and I need a response."
]

# 2. Setup Filters (Sets)
boring_words = {"i", "a", "the", "is", "to", "my", "with", "and"}
priority_keywords = {"refund", "billing", "urgent", "locked"}

# 3. Storage Structures
word_frequencies = {}
detected_priorities = set()

# 4. Processing Loops
for chat in chat_transcripts:
    # Normalize text and break it down into clean words
    words = chat.lower().replace(".", "").replace("!", "").split()
    
    for word in words:
        # Check if the word is a priority indicator
        if word in priority_keywords:
            detected_priorities.add(word)
            
        # Track regular word frequency if it isn't a boring word
        if word not in boring_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

# 5. Extracting and Sorting the Top Words
# (This sorts the dictionary items by their value/count in descending order)
sorted_words = sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)
top_5_words = sorted_words[:5]

# 6. Output Results
print("--- TOP 5 MOST COMMON WORDS (Filtered) ---")
for word, count in top_5_words:
    print(f"'{word}': appears {count} times")

print("\n--- UNIQUE PRIORITY TAGS FOUND ---")
print(detected_priorities)