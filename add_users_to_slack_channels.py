import pandas as pd
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Slack API token
slack_token = "xoxb-your-actual-token-here"
client = WebClient(token=slack_token)

def add_user_to_channel(user_email, channel_name):
    try:
        # Fetch the user ID from the email
        response = client.users_lookupByEmail(email=user_email)
        user_id = response['user']['id']
        
        # Fetch the channel ID from the channel name
        channels = client.conversations_list()
        channel_id = None
        for channel in channels['channels']:
            if channel['name'] == channel_name:
                channel_id = channel['id']
                break
        
        if not channel_id:
            print(f"Channel '{channel_name}' not found.")
            return
        
        # Invite the user to the channel
        client.conversations_invite(channel=channel_id, users=user_id)
        print(f"User {user_email} added to channel {channel_name}")
    
    except SlackApiError as e:
        print(f"Error adding user {user_email} to {channel_name}: {e.response['error']}")

def main():
    # Load the Excel file
    df = pd.read_excel("users_and_channels.xlsx")
    
    for _, row in df.iterrows():
        user_email = row['username']
        channel_name = row['channel_name']
        add_user_to_channel(user_email, channel_name)

if __name__ == "__main__":
    main()
