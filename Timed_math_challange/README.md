# 🧮 Timed Math Challenge

A **fun, terminal-based math quiz game** written in Python.  
Test your arithmetic speed and accuracy across randomly generated math problems — addition, subtraction, multiplication, modulus, and floor division — all against the clock!  

---

## 🚀 Features

✅ Randomly generated math problems  
✅ Timed performance tracking per question  
✅ Hint system (after 2 wrong attempts)  
✅ Colored terminal output (using `colorama`)  
✅ Skip option for tough questions  
✅ Summary report at the end:  
- Total problems  
- Correct answers  
- Wrong attempts  
- Total and average time  
- Accuracy percentage  

---

## 🧩 Example Gameplay

```
Timed Math Challenge
Solve a set of math problems as quickly and accurately as you can!

Problems: 10  Range: 1-20

Press Enter to start...
Starting in 3...
Starting in 2...
Starting in 1...

Problem #1/10
  8 * 5 = ?
Your answer (or type "skip"): 40
Correct! (+)  Time: 2.15s

Problem #2/10
  7 // 3 = ?
Your answer (or type "skip"): 2
Correct! (+)  Time: 1.12s
...
```

At the end, you’ll get a result summary like this:

```
RESULTS
----------------------------------------
Total problems: 10
Problems solved correctly: 9
Total attempts made: 11
Wrong attempts: 2
Total time: 35.6s
Average time per solved problem: 3.95s
Approx. accuracy: 80.0%
----------------------------------------
Thanks for playing! Run the script again to try for a better score.
```

---

## 🧠 How It Works

1. **Random Problems:**  
   Each round generates a random arithmetic expression using Python’s `operator` module.

2. **Timing:**  
   Each question’s response time is recorded, and a total duration is shown at the end.

3. **Hint System:**  
   After two wrong attempts, the program hints whether the answer is **even** or **odd**.

4. **Colored Output:**  
   Uses `colorama` (or ANSI fallback) for colorful and clear terminal UI.

---

## 🛠️ Requirements

- Python 3.7 or above  
- (Optional) `colorama` for better cross-platform color support  

Install dependencies with:  
```bash
pip install colorama
```

---

## 📂 File Structure

```
timed_math_challenge/
│
├── math_challenge.py      # Main game script
├── README.md              # Documentation (this file)
```

---

## ▶️ How to Run

Run directly in your terminal:  
```bash
python math_challenge.py
```

To restart, just run it again — each session generates new problems.  

---

## ⚙️ Customization

You can tweak these constants at the top of the script:  

| Variable         | Description                        | Default |
|------------------|------------------------------------|----------|
| `MIN_VALUE`      | Minimum number in math problems    | `1` |
| `MAX_VALUE`      | Maximum number in math problems    | `20` |
| `TOTAL_PROBLEM`  | Number of problems per session     | `10` |
| `OPERATORS`      | List of operations to include      | `['+', '-', '*', '%', '//']` |

Example:
```python
MIN_VALUE = 5
MAX_VALUE = 50
TOTAL_PROBLEM = 15
```

---

## 🧾 Notes

- Works on Windows, macOS, and Linux.  
- Clears the screen between rounds for a clean UI.  
- Gracefully handles `Ctrl+C` (KeyboardInterrupt).  
- Uses integer arithmetic only — no floating-point operations.  

---

## 💡 Future Improvements

- Add difficulty levels (easy/medium/hard)  
- Support division with real numbers  
- Add leaderboard or local score saving  
- GUI version using Tkinter or PyQt  

---

## 🧑‍💻 Author

**Prahalad Kumar**  
Python Developer 🐍  

Feel free to fork, modify, and contribute!  

📧 *Suggestions or improvements?* Open a GitHub issue or reach out.  