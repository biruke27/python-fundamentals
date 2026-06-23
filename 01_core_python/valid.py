# Look-Alike Project: Digital ID Badge Validator System

def verify_badge_permissions(badge_dict, standard_keys):
    """
    Checks if all required tracking metadata elements exist as keys inside the badge dictionary.
    """
    for key in standard_keys:
        if key not in badge_dict:
            return False  # Missing a required element! Exit early.
    return True  # All elements accounted for!


def calculate_clearance_ratio(score_a, score_b):
    """
    Safely computes the analytical performance ratio between two score metrics.
    Defensively intercepts ZeroDivisionError.
    """
    try:
        ratio = score_a / score_b
        return ratio
    except ZeroDivisionError:
        return "Division by zero is impossible"


def extract_clearance_level(raw_level_string):
    """
    Parses out a numerical level from a string sequence (e.g., "clearance_rank:4").
    Defensively intercepts ValueError during casting transformations.
    """
    try:
        # Step 1: Split the text pattern on the colon delimiter
        parts = raw_level_string.split(":")
        
        # Step 2: Grab the second chunk and attempt to transform it to an integer
        numerical_value = int(parts[1])
        return numerical_value
    except ValueError:
        # Fallback metric if parsing or integer conversion fails
        return 0


def main():
    print("--- RUNNING BADGE VALIDATOR INTEGRATION TESTS ---\n")
    
    # ==========================================
    # TEST CASE 1: Verifying Required Dictionary Keys
    # ==========================================
    required_metadata = ["id_num", "name", "role"]
    
    valid_badge = {"id_num": 1042, "name": "Alice", "role": "Engineer", "dept": "Cyber"}
    invalid_badge = {"id_num": 1043, "role": "Manager"}  # Missing "name"
    
    print("Test 1A (Valid Badge Keys):", verify_badge_permissions(valid_badge, required_metadata))
    print("Test 1B (Invalid Badge Keys):", verify_badge_permissions(invalid_badge, required_metadata))
    print("-" * 50)

    # ==========================================
    # TEST CASE 2: Safe Division Operations
    # ==========================================
    print("Test 2A (Normal Division):", calculate_clearance_ratio(100, 5))
    print("Test 2B (Zero Division Prevention):", calculate_clearance_ratio(100, 0))
    print("-" * 50)

    # ==========================================
    # TEST CASE 3: Data Parsing & Cast Verification
    # ==========================================
    print("Test 3A (Valid Text Parsing):", extract_clearance_level("clearance_rank:4"))
    print("Test 3B (Invalid Text Content Parsing):", extract_clearance_level("clearance_rank:LEVEL_A"))
    print("\n--- ALL VALIDATOR SYSTEM INTEGRATION TESTS COMPLETE ---")


if __name__ == "__main__":
    main()