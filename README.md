# Fun Quiz Game – Germany Edition 

Welcome to **Fun Quiz Game**, a command-line based trivia challenge that tests your knowledge of Germany through a dynamic 5-question experience.

---

## 🎯 Objective

The goal is simple:  
**Answer all 5 questions correctly and earn virtual euros along the way.**

But there’s a twist:  
One wrong answer? The game ends instantly — and you leave with whatever you’ve earned so far.

---

## 🧩 Game Flow

🧑‍💻 **Step-by-step experience:**

1. Game asks for your name and gives a warm welcome.
2. Displays one question at a time from a predefined list.
3. Checks your input against the correct answer (case-insensitive).
4. If your answer is correct, you move to the next question.
5. One wrong answer ends the game, and you’re told how much you’ve won.
6. If you clear all five, you get the full prize and a playful congratulation.

🎁 **Virtual reward structure:**

| Correct Answers | Reward (Euros) |
|------------------|----------------|
| 1                | 1000           |
| 2                | 2000           |
| 3                | 3000           |
| 4                | 4000           |
| 5                | 5000 (max win) |

---

## 🔍 Code Logic Breakdown

Here's how the program works under the hood:

### 🗃️ Data Storage

- All **questions** are stored in a list called `questions`.
- All **answers** are stored in a list called `answers`.
- This allows clean indexing and scalability for adding more Q&A later.

### 🔄 Conditional Nesting

```python
answer1 = input(questions[0])
if answer1.lower() == answers[0]:
    # proceed to question 2
    answer2 = input(questions[1])
    ...
```

Each block checks the answer and only proceeds if it's correct.  
If not, it exits the chain and prints the last won amount.

This nested logic gives a **“suspense chain”** effect — you keep playing as long as you keep getting answers right.

### 🔡 Case Handling

The use of `.lower()` on user input ensures that answers like `Berlin`, `berlin`, or `BERLIN` are treated the same — a small but important touch for usability.

### 💶 Reward Assignment

Reward amounts are stored as variables (`a`, `b`, `c`, `d`, `e`) and printed upon each correct answer. If the player fails at any point, their **last correct reward** is displayed as the final earning.

### 🎭 User Interaction

- Personalized greeting using the player's name.
- Friendly tone and gamified feedback for every correct response.
- Humorous failure lines to keep the experience light, not frustrating.

---

## 🚀 How to Run

1. Make sure you have Python installed.
2. Save the file as `fun_quiz_game.py`.
3. Open your terminal or command prompt.
4. Run:

   ```bash
   python fun_quiz_game.py
   ```

5. Enter your name and start answering!

---

## 📦 Example Questions

> ❓ What is the capital city of Germany?  
> ❓ Which German city is famous for Oktoberfest?  
> ❓ How many FIFA World Cups has Germany won (men's)?  
> ❓ Which is the biggest football club in Germany?  
> ❓ Who scored the winning goal in the 2014 World Cup final for Germany?

---

## 🧠 Why This Code Stands Out

- ✅ Simple, beginner-friendly structure  
- ✅ List-driven logic for easy expansion  
- ✅ Clearly separated logic and data  
- ✅ No external libraries, runs anywhere Python does  
- ✅ Excellent for small demos, learning projects, or command-line practice

---

## 🏁 Final Note

This project may be small in size, but it’s built with care.  
From its structure to its interactivity, it demonstrates how even simple CLI games can feel fun, clean, and thoughtfully designed.

Thanks for checking it out! 🎉  
Feel free to improve, remix, or extend it further.

**– Shuvo Ahmed**
