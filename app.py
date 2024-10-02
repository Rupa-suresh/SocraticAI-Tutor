from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = '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'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']

    # Generate a response using OpenAI GPT model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a teaching assistant using the Socratic method."},
            {"role": "user", "content": user_input}
        ]
    )

    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply


if __name__ == '__main__':
    app.run(debug=True)
