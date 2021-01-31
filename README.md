## Overview

This is a Slack app built with the [Bolt for Python framework][2] that showcases
responding to events and interactive buttons.

## Basic functionality includes:
1. Detect "how to get/getting started or found/find interesting" and reply with a automated response.
```zsh
   Automated response in message thread to reduce spam
```
2. Slash commands for projects which respond with the FAQs for each major project @CCExtractor.
```zsh
These commands are visible to users who type the slash command only to minimize spam.
```
## Running locally

### 1. Setup environment variables

```zsh
# Replace with your signing secret and token
export SLACK_BOT_TOKEN=<your-bot-token>
export SLACK_SIGNING_SECRET=<your-signing-secret>
```

### 2. Setup your local project

```zsh
# Clone this project onto your machine
git clone https://github.com/Techno-Disaster/GSoC-Helper.git

# Change into the project
cd GSoC-Helper/

# Install the dependencies
pip install -r requirements.txt
```

### 3. Start servers

[Setup ngrok][3] to create a local requests URL for development.

```zsh
./ngrok http 3000
```

#### For production, use heroku. 

[1]: https://slack.dev/bolt-python/tutorial/getting-started
[2]: https://slack.dev/bolt-python/
[3]: https://slack.dev/bolt-python/tutorial/getting-started#setting-up-events
[4]: https://github.com/slackapi/bolt-python/issues/new