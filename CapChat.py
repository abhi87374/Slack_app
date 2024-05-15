from flask import Flask, request, jsonify
from slack_sdk import WebClient
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
client = WebClient(token=os.getenv('SLACK_API_TOKEN'))

@app.route('/forward', methods=['POST'])
def forward_message():
    data = request.form
    message_text = data.get('text')

    message_text = data.get('text')
    channel_name = data.get('channel_name')

    if channel_name != 'channel-1':
        client.chat_postMessage(channel='#channel-2', text="'/forward' can only be used in #Channel-1")
        return jsonify({'response_type': 'in_channel'})
    
    if not message_text:
        client.chat_postMessage(channel=channel_name, text="Please provide a message to forward after the /forward command")
        return jsonify({'response_type': 'in_channel'})
    
    upper_case_message = message_text.upper()

    client.chat_postMessage(channel='#channel-2', text=upper_case_message)
    return jsonify({'response_type': 'in_channel'})

if __name__ == '__main__':
    app.run(debug=True)
