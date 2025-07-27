# Smart Merge Conflictor

A Python tool to detect and resolve Git merge conflicts intelligently.

## Features
- Detects conflict markers in files
- Shows both versions clearly
- Optional: Uses AI (GPT) to merge smartly

## How to Use
1. Run `main.py`
2. Enter path to conflicted file
3. View resolution suggestions

## Example

**Input file:**
```python
<<<<<<< HEAD
print("Hi from main")
=======
print("Hi from feature")
>>>>>>> feature
```

**Output:**
```python
# --- HEAD version ---
print("Hi from main")
# --- Incoming version ---
print("Hi from feature")
```

## Future Work
- GUI merge tool
- Semantic diff using AST