import os
from slack_bolt import App
from dotenv import load_dotenv

load_dotenv()
app = App(
    token=os.getenv("SLACK_API_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)

@app.command("/forward_reverse")
def forward_message(ack, body, say):

    ack()

    channel_name = body["channel_name"]
    
    if channel_name != "channel-2":
        say("This command can only be used in #Channel-2")
        return

    message_text = body["text"].strip()

    say(text=message_text.upper(), channel_name="channel-1")


if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
