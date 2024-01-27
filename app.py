from flask import Flask, render_template, request, session

import openai

import os

app = Flask(__name__)
# Change this to a secret key for session management
app.secret_key = '\xa1:\xf2\x1e\x19\xac\x1c\x08\x13\x8d~;J\xeb\x93\x0f\x13\xeddc\x06h-'

# Set your OpenAI API key
openai.api_key = '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'

SECRET_KEY = "\xa1:\xf2\x1e\x19\xac\x1c\x08\x13\x8d~;J\xeb\x93\x0f\x13\xeddc\x06h-"



# Function to interact with the ChatGPT model
def chat_with_gpt(prompt):
    response = openapi.Completion.create(
        engine="text-davinci-003",  # Use the appropriate engine (e.g., text-davinci-003)
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Chat route
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    # Retrieve conversation history from session or initialize
    conversation_history = session.get('conversation_history', [])

    # Add user input to conversation history
    conversation_history.append(f"You: {user_input}")

    # Generate a response from the ChatGPT model
    prompt = "\n".join(conversation_history)
    bot_response = chat_with_gpt(prompt)

    # Add bot response to conversation history
    conversation_history.append(f"Bot: {bot_response}")

    # Save conversation history in session
    session['conversation_history'] = conversation_history

    return render_template('index.html', conversation_history=conversation_history)

if __name__ == "__main__": 
    app.run(debug=True)
