import openai
import streamlit as st

# Set up OpenAI API credentials
openai.api_key = st.secrets["CHAT_GPT_KEY"]

# Define function to summarize a given review using OpenAI GPT-3
def summarize_review(review_text):
    completions = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Extract the 4 most important keywords from this product review: {review_text} ",
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0
        )
    message = completions.choices[0].text.strip()
    return message


# Define Streamlit app function
def app():
    # Set up sidebar inputs
    st.sidebar.header("Product Review Classifier")
    review_text = st.sidebar.text_input("Enter the product review:")

    # Summarize the review and extract 4 key phrases
    if review_text:
        summary = summarize_review(review_text)
        st.write("### These are the most important keywords extracted from that review:")
        st.write(summary)

# Run the Streamlit app
if __name__ == "__main__":
    app()
