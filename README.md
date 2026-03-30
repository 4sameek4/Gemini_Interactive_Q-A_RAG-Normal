# Gemini Interactive Q&A System

A Python-based interactive question-answering system using Google's Gemini API. Supports both simple question answering and retrieval-augmented generation (RAG) with context.

## Aim

This project delivers a complete local demo for Gemini-based QA with:
- Interactive one-by-one question handling (normal QA mode)
- Context-aware answers using retrieval-augmented generation (RAG mode)
- Automatic Gemini model selection from available API models
- Conversation history capture and session summary on exit
- Simple error handling and troubleshooting guidance
- Minimal setup: `.env` API key and requirements install

## Quick Start

### 1. Prerequisites
- Python 3.8+
- Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### 2. Installation

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Setup API Key

Create a `.env` file in the project directory:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Run Interactive Mode

```bash
python interactive_qa.py
```

---

## Usage Modes

### Mode 1: Simple Question Answering

Ask questions directly without providing context. The AI will answer based on its training data.

**Example:**
```
📝 Ask a question: What is machine learning?
⏳ Processing...

✓ Answer:
Machine learning is a subset of artificial intelligence (AI) that enables systems 
to learn and improve from experience without being explicitly programmed. It involves:
- Algorithms that identify patterns in data
- Training on historical data
- Making predictions or decisions without manual programming
...
```

**When to use:**
- General knowledge questions
- Definitions and explanations
- Current facts within the model's training data

---

### Mode 2: Contextual Question Answering (RAG)

Provide context first, then ask questions. The AI will answer based on the provided context.

**How to use:**

1. Type `context` when prompted:
```
📝 Ask a question: context
```

2. Paste your context (documents, text, code, etc.):
```
📚 Enter context (type 'END' on a new line when done):
Python is a high-level programming language known for its simplicity.
It supports multiple programming paradigms including object-oriented, functional, 
and procedural programming. Python is widely used in web development, data science, 
artificial intelligence, and automation.
END
```

3. Ask your question:
```
❓ Now ask your question: What is Python used for?
⏳ Processing...

✓ Answer:
Based on the provided context, Python is used for:
1. Web development
2. Data science
3. Artificial intelligence
4. Automation
...
```

**When to use:**
- When you have specific documents to reference
- To get answers about non-public information
- For CV/Job description matching
- Technical documentation Q&A
- Paper or article analysis

---

## Examples

### Example 1: Product Documentation

**Context:**
```
Product: CloudSync Pro
Version: 2.5
Features:
- Real-time file synchronization
- End-to-end encryption
- Supports up to 100 devices
- 500GB storage included
- Price: $9.99/month
```

**Questions:**
- How many devices can CloudSync support?
- What is the storage capacity included?
- Is CloudSync encrypted?

---

### Example 2: Job Description Matching

**Context:**
```
Job Title: Senior Python Developer
Requirements:
- 5+ years of Python experience
- Knowledge of Django/FastAPI
- PostgreSQL expertise
- AWS/GCP experience
- Team leadership skills
```

**Questions:**
- What are the main Python frameworks required?
- What cloud platforms are needed?
- How many years of experience is required?

---

### Example 3: Code Review

**Context:**
```python
def calculate_total(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total
```

**Questions:**
- What does this function do?
- Are there any potential improvements?
- What edge cases should be handled?

---

## Commands

While using the interactive mode:

| Command | Action |
|---------|--------|
| `context` | Enter RAG mode (provide context first) |
| `quit` | Exit the program |
| Any other text | Asked as a normal question |

---

## Output Features

✅ **Real-time Answers** - Get responses instantly

✅ **Conversation History** - View all Q&A at the end of session:
```
📋 Conversation Summary (5 questions answered)

[1] Q: What is AI?
    A: Artificial Intelligence is the simulation of human intelligence...

[2] Q: List Python uses
    A: Based on context, Python is used for...
```

✅ **Error Handling** - Clear error messages if something goes wrong

---

## Tips for Best Results

### For Normal Q&A:
- Be specific with your questions
- Ask one question at a time
- Provide context if your question is narrow or specialized

### For Contextual Q&A (RAG):
- Paste complete, relevant documents
- Use clear, well-formatted text
- Ask specific questions about the context
- The AI will focus only on provided context
- Great for proprietary or recent information

### General Tips:
- **Temperature matters** - The model uses temperature=0.7 by default (balanced creativity)
- **Longer context = better answers** - More detailed context leads to more accurate responses
- **One question at a time** - Ask complete questions for clearer answers
- **Be patient** - API responses may take 5-10 seconds

---

## Troubleshooting

### Error: "API key not provided"
**Solution:** Make sure `.env` file exists with `GEMINI_API_KEY=your_key`

### Error: "Module google.genai could not be resolved"
**Solution:** Install the package:
```bash
pip install google-genai --upgrade
```

### Error: "429 - Quota exceeded"
**Solution:** You've used your free tier quota. Options:
- Wait 24 hours for free tier reset
- Upgrade to a paid plan at [Google AI Console](https://console.cloud.google.com/)

### Slow responses
**Solution:** This is normal - API calls take time. The first response is usually slower.

### Poor answer quality
**Solution:** 
- Provide more specific context
- Rephrase your question
- For RAG, ensure context is relevant and clear

---

## File Structure

```
Project 4 (RAG - CV Tailoring)/
├── interactive_qa.py       # Main interactive script (RUN THIS)
├── retrieval_system.py     # Core QA system logic
├── .env                    # API key (do not commit)
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---

## System Requirements

- **Python:** 3.8 or higher
- **RAM:** 512MB minimum
- **Disk Space:** 100MB for dependencies
- **Internet:** Required for API calls

---

## How It Works

1. **Simple Q&A Flow:**
   ```
   User Question → Gemini API → Response → Display
   ```

2. **RAG (Context) Flow:**
   ```
   User Context → User Question → Combine → Gemini API → Response → Display
   ```

The system maintains conversation history internally and displays a summary when you exit.

---

## Performance Notes

- **Average response time:** 5-15 seconds
- **Max context length:** Limited by API (typically 1M tokens)
- **Concurrent requests:** One at a time (sequential processing)
- **Model used:** gemini-2.5-flash (latest, fastest model)

---

## Support

For issues with:
- **Google Gemini API:** Visit [Google AI Documentation](https://ai.google.dev/docs)
- **This script:** Check troubleshooting section above
- **Python issues:** Ensure Python 3.8+ is installed

---

## Example Session

```
============================================================
Gemini Retrieval System - Interactive Mode
============================================================

Initializing system...

✓ Using model: gemini-2.5-flash

------------------------------------------------------------
Ready for questions! Type 'quit' to exit, 'context' for RAG mode
------------------------------------------------------------

📝 Ask a question: What is artificial intelligence?

⏳ Processing...

✓ Answer:
Artificial Intelligence (AI) is the branch of computer science...
[Full answer displayed]

------------------------------------------------------------

📝 Ask a question: context

📚 Enter context (type 'END' on a new line when done):
AI is transforming industries...
END

❓ Now ask your question: How is AI transforming industries?

⏳ Processing...

✓ Answer:
Based on the provided context, AI is transforming industries by...
[Response focused on context]

------------------------------------------------------------

📝 Ask a question: quit

✓ Thanks for using Gemini Retrieval System!

📋 Conversation Summary (2 questions answered)

[1] Q: What is artificial intelligence?
    A: Artificial Intelligence (AI) is the branch of computer...

[2] Q: How is AI transforming industries?
    A: Based on the provided context, AI is transforming...
```

---

## License

This project is available for personal and commercial use.

---

**Happy Questioning!** 🚀
