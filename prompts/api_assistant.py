"""
API Assistant Prompt Template
This file contains the prompt used to generate API documentation answers.
"""

def generate_api_response(context: str, question: str) -> str:
    """
    Generate API documentation response based on context and question.
    
    Args:
        context: Retrieved documentation context
        question: User's question
        
    Returns:
        Generated answer
    """
    
    # ORIGINAL PROMPT (causes hallucination)
    # prompt = f"""
    # You are an API documentation assistant. Answer the question based on your knowledge.
    # 
    # Question: {question}
    # Context: {context}
    # 
    # Provide a comprehensive answer with examples.
    # """
    
    # FIXED PROMPT (grounded in context)
    prompt = f"""
You are an API documentation assistant. Answer the question using ONLY the information provided in the context below.

Context:
{context}

Question: {question}

Instructions:
- Use ONLY information from the context above
- Do not add information from your general knowledge
- If the context doesn't contain enough information, say so
- Be concise and accurate

Answer:"""
    
    return prompt


# Example usage
if __name__ == "__main__":
    context = """
    API authentication uses Bearer token authentication via the Authorization header.
    Format: Authorization: Bearer YOUR_API_KEY
    API keys can be generated from the developer dashboard.
    """
    
    question = "How do I authenticate with the API?"
    
    prompt = generate_api_response(context, question)
    print(prompt)
