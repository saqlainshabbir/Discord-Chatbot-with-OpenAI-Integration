import discord
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai_client = OpenAI()
# Set up intents and client
intents = discord.Intents.default()
intents.message_content = True

token = "MTI0MjQ3Nzc2NjA1ODgzNTk5MA.GLVRh5.J1P2xpSs3XQF5qb6QtWLbwYxk6U28cPvbEDg3Y"
# Replace with your OpenAI API key
api_key = os.environ.get("OPENAI_API_KEY")

discord_client = discord.Client(intents=intents)

@discord_client.event
async def on_ready():
    print(f"We have logged in as {discord_client.user}")

@discord_client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(username + " said " + user_message.lower() + " in " + channel)

    if message.author == discord_client.user:
        return
    if message.channel.name == 'general':
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        content = response.choices[0].message.content

        print(content)
        await message.channel.send(content)

discord_client.run(token)