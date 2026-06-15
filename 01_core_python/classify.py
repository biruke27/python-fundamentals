def classify_note(note):
  if "milestone" in note or "reached" in note:
        return "milestone"
  elif "agreed" in note or "final" in note:
      return "decision"
  elif "need" in note or "todo" in note:
        return "action"
  elif "?" in note or "who" in note:
        return "question"
  else:
      return "other"

def main():
    notes = [
        "reached: Phase 1 milestone",
        "agreed to use Python for the backend",
        "need to hire a designer",
        "who is responsible for testing?",
        "lunch was good"
    ]
    milestones, decisions, actions, questions, others = 0, 0, 0, 0, 0
    for note in notes:
        category = classify_note(note)
        if category == "milestone":
          milestones += 1
        elif category == "decision":
          decisions += 1
        elif category == "action":
          actions += 1
        elif category == "question":
          questions += 1
        else:
            others += 1
        print(f"Note: '{note}' | Classification: {category}")

    print(f"\nTotals - Milestones: {milestones}, Decisions: {decisions}, Actions: {actions}, Questions: {questions}, Others: {others}")


if __name__ == "__main__":
    main()
