# CapChat: Slack Message Forwarder

CapChat is a Flask application that forwards messages from one Slack channel to another using the `/forward` slash command.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- Python 3.x installed on your local machine.
- `pip` package manager installed.
- Slack API token for your Slack workspace.

## Installation

To install the dependencies, follow these steps:

1. Clone the repository to your local machine:
   git clone <repository-url>
2. Navigate to the project directory:
   cd slack-message-forwarder
3. Install the required Python packages using pip:
   pip install -r requirements.txt


## Configuration
Before running the application, you need to set up your Slack API token as an environment variable. Create a .env file in the root directory of the project and add your Slack API token:
  SLACK_API_TOKEN=your-slack-api-token

## Usage
To start the Flask application, run the following command:
  python CapChat.py

Once the application is running, you can send messages to the designated Slack channel using the /forward slash command in the specified format.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
