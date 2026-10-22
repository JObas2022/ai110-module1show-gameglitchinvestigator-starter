# logic_utils.py

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 500  # Hard should provide a broader challenge range
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        # Avoid silently converting floating-point inputs
        if "." in raw:
            return False, None, "Please enter a whole integer, not a decimal."
        value = int(raw)
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Enforce integer comparison to avoid string lexicographical sorting glitches
    guess_val = int(guess)
    secret_val = int(secret)

    if guess_val == secret_val:
        return "Win", "🎉 Correct!"
    elif guess_val > secret_val:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        return current_score + max(points, 10)

    # Standardize penalty for wrong guesses
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score