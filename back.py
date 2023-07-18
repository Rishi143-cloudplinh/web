from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = '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'

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data['user_input']

    # Call the ChatGPT API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_input,
        max_tokens=50
    )

    # Extract the generated message from the API response
    generated_message = response.choices[0].text.strip()

    return jsonify({'generated_message': generated_message})
@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')
    
if __name__ == '__main__':
    app.run()
