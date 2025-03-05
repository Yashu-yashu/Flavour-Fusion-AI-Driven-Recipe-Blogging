import streamlit as st
import google.generativeai as genai
import random

# Configure the API key
api_key = "AIzaSyCAlM0Y_qZ1OlLc7eXqHnBa8Vr2SM8iqG8"  # Replace with your actual API key
genai.configure(api_key=api_key)

# Model configuration
generation_config = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}

# Initialize the Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

def get_joke():
    """Generate a random programmer joke."""
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Python programmers prefer using snake_case? Because it's easier to read!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 Dec 25.",
        "Why did the programmer get kicked out of the beach? Because he kept using the 'C' language!",
        "Why was the computer cold? It left its Windows open."
    ]
    return random.choice(jokes)

def recipe_generation(user_input, word_count):
    """Generate a recipe blog post based on user input and word count."""
    try:
        # Display generation message
        st.write("🍳 Generating your recipe...")
        
        # Display a joke while generating
        st.write(f"While I work on creating your blog, here's a little joke to keep you entertained:\n\n*{get_joke()}*")
        
        # Start a chat session
        chat_session = model.start_chat(history=[
            {
                "role": "user",
                "parts": [f"Write a recipe based on the input topic: {user_input} and number of words: {word_count}"]
            }
        ])
        
        # Generate the response
        response = chat_session.send_message(user_input)
        
        st.success("🎉 Your recipe is ready!")
        return response.text
    
    except Exception as e:
        st.error(f"Error generating blog: {e}")
        return None

def main():
    """Main Streamlit application."""
    st.title("🍽️ Flavour Fusion: AI-Driven Recipe Blogging")
    st.write("Hello! I'm RecipeMaster, your friendly robot. Let's create a fantastic recipe together!")
    
    # User inputs
    user_input = st.text_input("Topic", help="Enter the recipe or cuisine you want to create")
    word_count = st.number_input("Number of words", min_value=100, max_value=2000, value=500, step=50)
    
    # Generate button
    if st.button("Generate Recipe"):
        if user_input:
            recipe = recipe_generation(user_input, word_count)
            if recipe:
                st.markdown("## Generated Recipe")
                st.write(recipe)
        else:
            st.warning("Please enter a topic for your recipe!")

if __name__ == "__main__":
    main()
