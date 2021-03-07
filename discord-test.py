import requests
import discord

# Get user messages with Guild ID and User ID
# def get_messages():
#     headers = {'Authorization': API_TOKEN}
#     search_url = 'https://discord.com/api/v8/guilds/758122726871007232/messages/search?author_id=698370734380154932'

#     response = requests.get(search_url, headers=headers)
#     print (response.content)

#get_messages()	

# def get_userid():
#     headers = {'Authorization': API_TOKEN}
#     search_url = 'https://discord.com/api/v8/users/719755032995823637'

#     response = requests.get(search_url, headers=headers)
#     print (response.content)

#get_userid()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('token')


# Bot gets a message from channel


# Use api to get last 50-100 user messages in that guild


# Parse and save the messages to a var


# Run text2emotion on the messages var


# Result from text2emotion mapped to movie genres


# Any movie db api call with selected genre


# Process and format result from movie db api to list of 3-5 movies


# Bot dm's user with movies

