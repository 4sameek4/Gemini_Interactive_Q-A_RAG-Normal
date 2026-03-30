# Gemini_Interactive_Q-A_RAG-Normal

A lightweight Python project that integrates Google Gemini for conversational question-answering with two modes:

Normal Q&A: Ask a question and get instant answers from Gemini.
Contextual Q&A (RAG): Provide a document/text block + question to get context-aware responses.
🔹 Key Features
interactive_qa.py: Real-time prompt loop (ask / context / quit)
retrieval_system.py: Core API wrapper using Gemini (google.genai)
Automatic model discovery (gemini-2.5-flash, gemini-2.5-pro, etc.)
Includes customizable context injection for Retrieval-Augmented Generation
Session history summary at exit
⚙️ Setup
pip install -r requirements.txt
Create .env:
GEMINI_API_KEY=your_api_key
Run:
python interactive_qa.py
🧠 Usage (command flow)
Simple question: directly type text
Context mode: type context, paste context, type END, then ask
Exit: quit

📌 Why this is useful
Rapid prototyping of RAG-style chatbots
Devs can test private knowledge Q&A with local text
Good base for resumes/PDL tailoring systems, docs chat, support bot
🛠️ Troubleshooting
google.genai import warning → pip install google-genai --upgrade
Model not found → use auto-listed available Geminis
429 quota → wait/upgrade Google billing
🧾 Aim
Add as a clean “project summary + instructions” in GitHub to show:

fast setup
clear modes
explicit API path
running example behavior
production-ready quick start
