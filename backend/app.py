import openai
import fitz  # PyMuPDF

# Your OpenAI API key
openai.api_key = 'your-api-key'  # Replace with your actual API key

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

# Specify the path to your PDF file
pdf_path = "path/to/your/file.pdf"  # Replace with the actual path to your PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Start a chat session
def chat_with_openai(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": pdf_text}  # Provide PDF content
        ],
        max_tokens=150  # Adjust the number of tokens as needed
    )
    return response['choices'][0]['message']['content'].strip()

# Example user input
user_query = "Can you summarize the key points from the document?"

# Get the assistant's response
assistant_response = chat_with_openai(user_query)
print("Assistant:", assistant_response)
