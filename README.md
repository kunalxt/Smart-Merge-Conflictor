# 🧑‍💻Smart Merge Conflictor

A Python tool to detect and resolve Git merge conflicts intelligently.
🔀 A smart tool to help resolve Git merge conflicts using AI.


## 🚀 Features

- Parses `.conflict` files containing Git-style conflict markers.
- Uses local LLMs via [Ollama](https://ollama.com/) (e.g., LLaMA 3) to suggest conflict resolutions.
- Easily extensible and works offline.
- Example conflicts provided for testing.
- Detects conflict markers in files
- Shows both versions clearly
- Optional: Uses AI (GPT) to merge smartly

## 🧠How to Use
1. Run `main.py`
2. Enter path to conflicted file
3. View resolution suggestions

## 🧪Example

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



## 🛠️ Installation

```bash
git clone https://github.com/kunalxt/smart-merge-conflictor.git
cd smart-merge-conflictor
pip install -r requirements.txt



## 🛡 License

**MIT License**

---

## 📌 Topics

**git** **merge** **ai** **conflict-resolution** **llm** **openai** **ollama** **llama3**

---

## 📁 __Project Structure__



smart-merge-conflictor/
│
├── main.py                 # Entry point
├── ai_helper.py            # Handles AI calls (Ollama/OpenAI)
├── conflict_parser.py      # Parses merge conflicts
├── resolver.py             # Merge logic
├── examples/               # Sample conflict files
├── requirements.txt        # Dependencies
├── .gitignore
└── README.md
