# 🚀 Slack Channel User Invite Automation

Automate the process of adding users to Slack channels with data from an Excel file. This script uses Python, `pandas`, and Slack's API to invite users to specified channels, making team management easier! 🎉

---

## 📋 Features
- 📊 Reads user and channel data from an Excel file.
- 🤖 Automatically invites users to specified Slack channels.
- 📁 Supports adding multiple users to multiple channels.
- 🔒 Ensures secure API calls with error handling.

---

## 🛠️ Requirements

1. **Python** (version 3.x)
2. Python Libraries:
   - `pandas`
   - `slack_sdk`
   - `openpyxl`

Install the required libraries:
```bash
pip install pandas slack_sdk openpyxl

3. In the configuration file or environment variables, replace xoxb-your-slack-bot-token with your actual bot token:

## 🤖 Slack App Setup
- To use this script, you need to create a Slack app with the proper permissions to invite users to channels. Follow these steps:

## Create a Slack App:

- Go to Slack API: Create New App and click Create New App.
- Choose From Scratch and give your app a name. Select the workspace where you want to use this app.

## Add Bot Token Scopes:

- In your app dashboard, navigate to OAuth & Permissions.
- Under Scopes, add the following Bot Token Scopes:
- channels:write.invites – Allows the bot to invite users to public channels.
- groups:write – Allows the bot to invite users to private channels (if it’s a member of the private channel).
- users:read – Allows the bot to look up users by email.

## Install the App to Your Workspace:

- Go to the OAuth & Permissions page in your app settings.
- Click Install App to Workspace and follow the prompts to authorize the app.
- Copy the Bot User OAuth Token displayed after installation—this is the token you'll use in your script to authenticate API requests.
- Add the Bot to Channels (if necessary):

For private channels, you need to manually invite the bot to the channel before it can add other users.
