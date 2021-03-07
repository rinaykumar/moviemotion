API_TOKEN = ''

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

client.run('ODE3NjI5Mjc0NjcyMzMyODMw.YEMSmQ.-oc7GUr__JZ1ua5VH2TTdJ2Ohzg')
