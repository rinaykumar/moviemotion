API_TOKEN = ''

import discord
import text2emotion as te

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Bot gets a message from channel
@client.event
async def on_message(message):
    user_id = message.author.id
    counter = 0
    messages = ""

    if message.content.startswith('$test'):
         # Get user messages in the guild their in
        for chan in message.guild.text_channels:
            async for msg in chan.history(limit=100): # Last 100 messages in each channel 
                if msg.author.id == user_id:                                
                    counter += 1
                    # Save the messages to an array
                    messages = messages + " " + msg.content

    # Remove newlines and tabs from messages
    messages = messages.replace('\n', '')
    messages = messages.replace('\t', '')
    messages = messages.strip('\n')  
    messages = messages.strip('\t')
    
    # For testing
    print (messages)
    print (counter)

    # Run text2emotion on messages 
    emotions = te.get_emotion(messages)
    print (emotions)

    # Result from text2emotion mapped to movie genres

    # Any movie db api call with selected genre

    # Process and format result from movie db api to list of 3-5 movies

    # DM the user                
    await message.author.send(f'You have **{counter}** messages')
    await message.author.send(f'{messages}')

client.run(API_TOKEN)
