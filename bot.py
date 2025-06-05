# Import the discord library for Discord bot functionality
import discord
# Import requests library for making HTTP requests
import requests
# Import json library for parsing JSON data
import json
# Import os and dotenv for environment variables
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to fetch a random meme from the meme API
def get_meme():
  # Make a GET request to the meme API endpoint
  response = requests.get('https://meme-api.com/gimme')
  # Parse the JSON response text into a Python dictionary
  json_data = json.loads(response.text)
  # Return the URL of the meme from the parsed data
  return json_data['url']

# Define a custom Discord client class that inherits from discord.Client
class MyClient(discord.Client):
    # Event handler that runs when the bot successfully connects to Discord
    async def on_ready(self):
        # Print a confirmation message with the bot's username
        print('Logged on as {0}!'.format(self.user))
    
    # Event handler that runs whenever a message is sent in a channel the bot can see
    async def on_message(self, message):
      # Check if the message author is the bot itself to prevent infinite loops
      if message.author == self.user:
        return

      # Check if the message content starts with the '$hello' command
      if message.content.startswith('$hello'):
        # Send a greeting message to the same channel
        await message.channel.send('Hello World!')
      
      # Check if the message content starts with the '$meme' command
      if message.content.startswith('$meme'):
        # Call the get_meme function and send the meme URL to the channel
        await message.channel.send(get_meme())
        
# Create an Intents object with default permissions
intents = discord.Intents.default()
# Enable the message content intent to allow the bot to read message content
intents.message_content = True

# Create an instance of the custom client with the specified intents
client = MyClient(intents=intents)
# Start the bot using the token from environment variables
client.run(os.getenv('DISCORD_TOKEN'))