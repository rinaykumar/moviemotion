API_TOKEN = 'ODE3NjI5Mjc0NjcyMzMyODMw.YEMSmQ.2MXL-_dj1ML25Ftzg0vudiEeY0U'

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Bot gets a message from channel
@client.event
async def on_message(message):
    user_id = message.author.id
    counter = 0
    messages = []

    if message.content.startswith('$test'):
         # Get user messages in the guild their in
        for chan in message.guild.text_channels:
            async for msg in chan.history(limit=50): # Last 50 messages in each channel 
                if msg.author.id == user_id:                                
                    counter += 1
                    # Save the messages to an array
                    messages.append(msg.content)
    # DM the user                
    await message.author.send(f'You have **{counter}** messages')
    await message.author.send(f'{messages}')

    # For testing
    print (counter)  
    print (messages)   

client.run(API_TOKEN)

# TODO

# Run text2emotion on the messages array

# Result from text2emotion mapped to movie genres

# Any movie db api call with selected genre

# Process and format result from movie db api to list of 3-5 movies
