# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looked like a simple number guessing game with an input for your answers and three buttons below. One was to submit guesses, one to start a new game, and a checkbox to turn on/off hints. The sidebar also contained difficulty dropdown settings and a developer debug box displaying game variables.

- List at least two concrete bugs you noticed at the start  
The hints were completely inverted (telling the player to go higher when the guess was already too high), and the scoring system was erratic by adding points on wrong attempts instead of subtracting them. Additionally, changing difficulty levels didn't update the actual game range properly, and the code converted the secret number into a string on alternating turns, breaking numeric comparisons.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|---|---|---|---|
| Guess `82` (Secret: `50`) | Hint should say "Go Lower" | Hint displayed "📈 Go HIGHER!" | None |
| Guess `20` (Secret: `50`) | Hint should say "Go Higher" | Hint displayed "📉 Go LOWER!" | None |
| Attempt 2 wrong guess | Score should decrease by 5 points | Score increased by 5 points | None |
| App launch | Game should load logic from helper module | App crashed immediately with `NotImplementedError` | `NotImplementedError: Refactor this function from app.py into logic_utils.py` |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Gemini.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
When I tried to install project dependencies, my PowerShell terminal threw a `'pip' is not recognized` error because pip wasn't mapped directly in my environment variables. Gemini suggested using the Python module execution flag `python -m pip install -r requirements.txt` to invoke pip directly through the Python executable. I verified this by running it in the terminal, which immediately resolved the error and successfully installed all project requirements.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
When refactoring `logic_utils.py`, the AI initially suggested a complete rewrite of `app.py` along with several extra UI adjustments and validation checks that went beyond the immediate task. I rejected overwriting `app.py` all at once because the immediate blocker was a `NotImplementedError` raised specifically by `logic_utils.py`. Instead, I isolated the changes to `logic_utils.py` first, cleared `__pycache__`, and verified the functions independently before making any wider alterations.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was really fixed by recreating the exact conditions that triggered it during initial gameplay and observing whether the outcome followed expected logic. Beyond manual gameplay, I relied on automated unit tests to check both edge cases and core assertions so that future adjustments wouldn't accidentally bring the bug back.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I ran a test verifying that `check_guess(guess=75, secret=50)` returns the outcome `"Too High"` alongside a message directing the player to go lower. Running `pytest` on this function proved that our refactored comparison logic was strictly handling numbers rather than doing string-based comparisons, confirming that inverted hints were resolved across all attempt cycles.

- Did AI help you design or understand any tests? How?
Yes, the AI helped design concise unit tests with `pytest` that targeted individual helper functions in `logic_utils.py` rather than trying to test everything through the full browser UI. It explained how testing `check_guess` and `update_score` in isolation makes it much faster to catch bugs early without having to click through multiple game rounds.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit runs the entire Python script from top to bottom every single time a user interacts with a widget, clicks a button, or enters a value. Because of these frequent reruns, normal local variables get reset to their starting values on every interaction. `st.session_state` acts like persistent memory between runs, allowing you to preserve critical data—like the secret number, current score, and attempt count—across the entire user session.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Refactoring core calculation and validation logic out of the presentation layer into separate utility modules (`logic_utils.py`) is a habit I will continue using. Keeping logic separate makes code much easier to read, allows direct automated unit testing with `pytest`, and prevents UI reruns from obscuring underlying bugs.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I will provide the AI with narrower, single-function prompts and review file diffs step by step rather than accepting multi-file overhauls. Breaking tasks down into smaller milestones makes it much easier to diagnose specific errors—such as unsaved files or bytecode cache issues—without guessing where things broke.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that while AI can generate plausible-looking code very quickly, it frequently hides subtle logic flaws and deceptive edge cases. Developers cannot simply trust AI output blindly; thorough human code review and automated testing are essential before considering any code production-ready.