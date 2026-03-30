import google.genai as genai
from typing import Optional, List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GeminiRetrieverQA:
    """
    A retrieval question-answering system using Google Gemini API.
    This system can answer questions based on retrieved context or general knowledge.
    """
    
    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        """
        Initialize the Gemini Retriever QA system.
        
        Args:
            api_key: Google API key. If None, reads from GEMINI_API_KEY environment variable
            model_name: The Gemini model to use. If None, uses the first available model
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key not provided. Set GEMINI_API_KEY environment variable or pass api_key parameter."
            )
        
        # Initialize Genai client
        self.client = genai.Client(api_key=self.api_key)
        
        # Use provided model or get first available
        if model_name:
            self.selected_model = model_name
        else:
            # Get available models
            available_models = self.list_available_models(self.client)
            if not available_models:
                raise ValueError("No available models found. Check your API key and permissions.")
            self.selected_model = available_models[0]
        
        print(f"✓ Using model: {self.selected_model}\n")
        self.conversation_history = []
    
    @staticmethod
    def list_available_models(client=None):
        """List available models from the API that support generateContent."""
        try:
            if client is None:
                # Create a temporary client for listing models
                api_key = os.getenv("GEMINI_API_KEY")
                if not api_key:
                    return ['gemini-2.5-flash', 'gemini-2.5-pro', 'gemini-2.0-flash']
                client = genai.Client(api_key=api_key)
            
            models = client.models.list()
            available = []
            for model in models:
                if hasattr(model, 'name'):
                    model_name = model.name.replace('models/', '')
                    available.append(model_name)
            
            if not available:
                return ['gemini-2.5-flash', 'gemini-2.5-pro', 'gemini-2.0-flash']
            
            # Prioritize newer models (2.5 and 3.x versions)
            priority_order = [
                'gemini-2.5-flash',
                'gemini-2.5-pro',
                'gemini-3.1-flash-lite-preview',
                'gemini-3-flash-preview',
                'gemini-2.0-flash',
                'gemini-flash-latest',
                'gemini-pro-latest'
            ]
            
            # Sort by priority
            sorted_models = []
            for priority_model in priority_order:
                if priority_model in available:
                    sorted_models.append(priority_model)
            
            # Add any remaining models
            for model in available:
                if model not in sorted_models:
                    sorted_models.append(model)
            
            return sorted_models
        except Exception as e:
            print(f"Warning: Could not fetch available models: {e}")
            # Fallback to known working models
            return ['gemini-2.5-flash', 'gemini-2.5-pro', 'gemini-2.0-flash']
    
    def retrieve_and_answer(
        self, 
        question: str, 
        context: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1024
    ) -> str:
        """
        Answer a question optionally with provided context (RAG approach).
        
        Args:
            question: The user's question
            context: Optional context/documents to consider for the answer
            temperature: Creativity level (0.0-1.0). Lower is more deterministic
            max_tokens: Maximum response length
            
        Returns:
            The answer from Gemini API
        """
        # Build the prompt
        if context:
            prompt = f"""Based on the following context, please answer the question.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:"""
        else:
            prompt = question
        
        # Generate response using the client
        response = self.client.models.generate_content(
            model=self.selected_model,
            contents=prompt,
            config={
                "temperature": temperature,
                "max_output_tokens": max_tokens
            }
        )
        
        answer = response.text
        
        # Store in conversation history
        self.conversation_history.append({
            "question": question,
            "context": context,
            "answer": answer
        })
        
        return answer
    
    def answer_question(
        self, 
        question: str,
        temperature: float = 0.7,
        max_tokens: int = 1024
    ) -> str:
        """
        Answer a general question without providing context.
        
        Args:
            question: The user's question
            temperature: Creativity level
            max_tokens: Maximum response length
            
        Returns:
            The answer from Gemini API
        """
        return self.retrieve_and_answer(
            question=question,
            context=None,
            temperature=temperature,
            max_tokens=max_tokens
        )
    
    def batch_answer_questions(
        self, 
        questions: List[str],
        context: Optional[str] = None,
        temperature: float = 0.7
    ) -> List[str]:
        """
        Answer multiple questions at once.
        
        Args:
            questions: List of questions
            context: Optional context for all questions
            temperature: Creativity level
            
        Returns:
            List of answers
        """
        answers = []
        for question in questions:
            answer = self.retrieve_and_answer(
                question=question,
                context=context,
                temperature=temperature
            )
            answers.append(answer)
        return answers
    
    def get_conversation_history(self) -> List[dict]:
        """Get the conversation history."""
        return self.conversation_history
    
    def clear_history(self):
        """Clear the conversation history."""
        self.conversation_history = []


def main():
    """Example usage of the Gemini Retriever QA system."""
    
    try:
        # Initialize the system
        qa_system = GeminiRetrieverQA()
        
        print("=" * 60)
        print("Gemini Retrieval QA System")
        print("=" * 60)
        
        # Example 1: Simple question without context
        print("\n[Example 1] Simple Question:")
        question1 = "What is machine learning?"
        print(f"Q: {question1}")
        answer1 = qa_system.answer_question(question1)
        print(f"A: {answer1}\n")
        
        # Example 2: Question with context (RAG approach)
        print("[Example 2] Question with Context (RAG):")
        context = """
        Python is a high-level programming language known for its simplicity and readability.
        It supports multiple programming paradigms including object-oriented, functional, 
        and procedural programming. Python is widely used in web development, data science, 
        artificial intelligence, and automation.
        """
        question2 = "What is Python used for?"
        print(f"Q: {question2}")
        answer2 = qa_system.retrieve_and_answer(question2, context=context)
        print(f"A: {answer2}\n")
        
        # Example 3: Batch questions
        print("[Example 3] Batch Questions:")
        batch_questions = [
            "What is artificial intelligence?",
            "What is deep learning?",
            "What is natural language processing?"
        ]
        batch_answers = qa_system.batch_answer_questions(batch_questions)
        for q, a in zip(batch_questions, batch_answers):
            print(f"Q: {q}")
            print(f"A: {a}\n")
        
        # Example 4: Interactive mode
        print("\n[Interactive Mode]")
        print("Type 'quit' to exit\n")
        while True:
            user_question = input("Ask a question: ").strip()
            if user_question.lower() == 'quit':
                break
            
            answer = qa_system.answer_question(user_question)
            print(f"Answer: {answer}\n")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
