# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit[cite: 10].
It wrote the code, ran away, and now the game is unplayable[cite: 10]. 

- You can't win[cite: 10].
- The hints lie to you[cite: 10].
- The secret number seems to have commitment issues[cite: 10].

## 🛠️ Setup

1. Install dependencies: `python -m pip install -r requirements.txt`
2. Run the fixed app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win[cite: 10].
2. **Find the State Bug.** Keep variables from resetting across Streamlit component updates using `st.session_state`.
3. **Fix the Logic.** Correct the inverted "Higher/Lower" hints and numeric type-casting comparisons[cite: 6, 10].
4. **Refactor & Test.** - Move the logic into `logic_utils.py`[cite: 5, 10].
   - Run `pytest` in your terminal[cite: 5, 10].
   - Keep fixing until all tests pass[cite: 10]!

## 📝 Document Your Experience

- **Game Purpose:** An interactive Streamlit number-guessing game where players select a difficulty, deduce a randomly generated target number within an allowed attempt limit, and receive direction-based hints and calculated score updates.
- **Bugs Identified:**
  1. *Inverted Hint Logic:* In `check_guess`, guessing a number higher than the secret told the player to "Go HIGHER!", while guessing lower told them to "Go LOWER!"[cite: 6].
  2. *Alternating Type Coercion:* The game cast `secret` into a `str` on even attempt turns[cite: 6], triggering lexicographical comparisons rather than numeric checks (e.g., `'9' > '10'`).
  3. *Inconsistent Scoring:* In `update_score`, incorrect "Too High" guesses awarded 5 bonus points on even attempts instead of penalizing the score[cite: 6].
  4. *Stub Exceptions:* Core helper functions in `logic_utils.py` threw `NotImplementedError` placeholders upon application startup[cite: 7].
- **Fixes Applied:**
  - Extracted game calculations and validation logic from `app.py` into `logic_utils.py`[cite: 5].
  - Implemented correct directional hints and integer casting in `check_guess` to prevent type mismatches[cite: 6].
  - Standardized `update_score` to uniformly deduct 5 points for wrong answers[cite: 6].
  - Synchronized `st.session_state` management so difficulty changes properly reinitialize boundaries and attempt counters[cite: 6].

## 📸 Demo Walkthrough

1. The user selects **Normal** difficulty (number range 1 to 100, 8 attempts allowed)[cite: 6].
2. The user inputs an initial guess of `50`. The secret target is `73`[cite: 6].
3. The game responds with `📈 Go HIGHER!`, records `50` in the history log, and decrements the player's score by 5 points[cite: 6].
4. The user inputs a second guess of `85`.
5. The game responds with `📉 Go LOWER!`, records `85`, and subtracts another 5 points[cite: 6].
6. The user enters `73`.
7. The game triggers celebration balloons, announces `🎉 Correct!`, sets the game status to won, displays the final score calculation, and stops further inputs[cite: 6].

## 🧪 Test Results

```bash
pytest test/
============================= test session starts =============================
platform win32 -- Python 3.11.x, pytest-8.x.x
rootdir: C:\Users\Jerry\codepath-demo\ai110-module1show-gameglitchinvestigator-starter
collected 3 items

test/test_game_logic.py ...                                              [100%]

============================== 3 passed in 0.12s ==============================