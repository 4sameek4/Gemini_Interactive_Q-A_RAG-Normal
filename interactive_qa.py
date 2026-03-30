"""
Real-time interactive Q&A script for testing the Gemini Retrieval System.
Run this file to ask questions one by one in real-time.
"""

from retrieval_system import GeminiRetrieverQA

def main():
    print("\n" + "=" * 60)
    print("Gemini Retrieval System - Interactive Mode")
    print("=" * 60)
    print("\nInitializing system...\n")
    
    try:
        # Initialize the QA system
        qa_system = GeminiRetrieverQA()
        
        print("\n" + "-" * 60)
        print("Ready for questions! Type 'quit' to exit, 'context' for RAG mode")
        print("-" * 60 + "\n")
        
        while True:
            # Get user input
            user_input = input("📝 Ask a question: ").strip()
            
            if user_input.lower() == 'quit':
                print("\n✓ Thanks for using Gemini Retrieval System!\n")
                break
            
            if user_input.lower() == 'context':
                # RAG mode - ask for context
                print("\n📚 Enter context (type 'END' on a new line when done):")
                context_lines = []
                while True:
                    line = input()
                    if line.strip().upper() == 'END':
                        break
                    context_lines.append(line)
                
                context = "\n".join(context_lines)
                question = input("\n❓ Now ask your question: ").strip()
                
                if question:
                    print("\n⏳ Processing...\n")
                    answer = qa_system.retrieve_and_answer(question, context=context)
                    print(f"✓ Answer:\n{answer}\n")
                continue
            
            if not user_input:
                print("⚠️  Please enter a question.\n")
                continue
            
            # Simple Q&A mode
            print("\n⏳ Processing...\n")
            answer = qa_system.answer_question(user_input)
            print(f"✓ Answer:\n{answer}\n")
            print("-" * 60 + "\n")
        
        # Show conversation history at the end
        history = qa_system.get_conversation_history()
        if history:
            print("\n" + "=" * 60)
            print(f"📋 Conversation Summary ({len(history)} questions answered)")
            print("=" * 60 + "\n")
            for i, conv in enumerate(history, 1):
                print(f"[{i}] Q: {conv['question']}")
                print(f"    A: {conv['answer'][:100]}...\n")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n⚠️  Make sure:")
        print("  1. .env file exists with GEMINI_API_KEY")
        print("  2. google-genai is installed: pip install google-genai")
        print("  3. Internet connection is active")


if __name__ == "__main__":
    main()
