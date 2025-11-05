# 🔁 Python Loops — Quick Handbook

> 🐍 Loops let you repeat code automatically instead of writing it many times.

---

## 🔹 What is a Loop?

A **loop** runs a block of code repeatedly until a condition is no longer true. It helps automate repetitive tasks.

---

## 🔸 Types of Loops

| Type         | Description                                                | Best Use                                 |
| :----------- | :--------------------------------------------------------- | :--------------------------------------- |
| `for` loop   | Iterates over a sequence (like list, tuple, string, range) | When you know how many times to loop     |
| `while` loop | Runs while a condition is `True`                           | When the number of iterations is unknown |

---

## 🌀 `for` Loop — Syntax & Example

```python
for item in sequence:
    # code block
```

**Example:**

```python
for i in range(5):
    print("Hello", i)
```

✅ Use when iterating through lists, ranges, or strings.

---

## 🔄 `while` Loop — Syntax & Example

```python
while condition:
    # code block
```

**Example:**

```python
count = 0
while count < 3:
    print("Count:", count)
    count += 1
```

✅ Use when repeating actions until a condition changes.

---

## ⚙️ Loop Control Statements

| Keyword    | Function                   |
| :--------- | :------------------------- |
| `break`    | Exits the loop immediately |
| `continue` | Skips current iteration    |
| `pass`     | Placeholder (does nothing) |

---

## 🧠 Summary

* Use **`for`** for sequences.
* Use **`while`** for conditions.
* Combine with **`break`**, **`continue`**, and **`pass`** for control.

> 💡 **Tip:** Loops save time and make your code cleaner and more efficient!
