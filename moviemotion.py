API_TOKEN = ''

import discord
import text2emotion as te
import random 

# Movie arrays
surprise = ["Behind Her Eyes", "The Sinner", "Tell Me Your Secrets", "The Blacklist", "Resident Alien", "I Care a Lot", "Mortal Kombat", "The Walking Dead", "Army of the Dead", "The Little Things", "WandaVision", "Superman and Lois", "The Mandalorian", "Spider-Man: No Way Home", "Tenet", "The Lord of the Rings: The Return of the King", "Inception", "Interstellar", "Seven Samurai", "The Lion King"]
fear =["Attack on Titan", "Wrong Turn", "Supernatural", "American Horror Story", "The Vampire Diaries", "Saving Private Ryan", "The Pianist", "Casablanca", "Dara of Jasenovac", "Apocalypse Now", "Raatchasan", "The Silence of the Lambs", "Joker", "Oldboy", "Tumbbad", "WandaVision", "Supernatural", "Wonder Woman 1984", "The Suicide Squad", "Soul", "Shadow and Bone"]
angry = ["The Matrix", "Star Wars: Episode V", "Gladiator", "Terminator 2", "Oldboy", "Aliens", "Warrior", "Die Hard", "Mission: Impossible", "Black Panther", "Snowpiercer", "Joker", "Pulp Fiction", "The Departed", "Goodfellas", "American Psycho", "Ocean’s Eleven", "Taxi Driver", "The Equalizer", "Scarface"]
sad=["Hababam Sinifi","The Godfather","The Dark Knight","Schindler's List","Fight Club","Shadow of a Doubt","The Night of the Hunter","The Third Man","Touch of Evil","Out of the Past","Judas and the Black Messiah","It's a Sin","The Crown","The Trial of the Chicago 7","Age of Samurai: Battle for Japan","WandaVision“","Tribes of Europa","Game of Thrones","Outlander","Monster Hunter"]
happy = ["Coming to America","Parasite","Once Upon a Time... In Hollywood","Thor: Ragnarok","The Gentlemen","Deadpool","Back to the Future","Snatch","The Sting","Lock, Stock and Two Smoking Barrels","The Grand Budapest Hotel","The Greatest Showman","Aladdin","The Sound of Music","The Blues Brothers","The Goonies","The Princess Bride","Wall-E","Toy Story","Friday"]

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

    if message.content.startswith('!moviemotion'):
         # Get user messages in the guild their in
        for chan in message.guild.text_channels:
            async for msg in chan.history(limit=100): # Last 100 messages in each channel 
                if msg.author.id == user_id:                                
                    counter += 1
                    # Save the messages to an array
                    messages = messages + " " + msg.content

        # Format messages
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
        Keymax = max(emotions, key=emotions.get) 
        print(Keymax) 

        # Any movie db api call with selected genre
        Start = 0
        Stop = 19
        limit = 3

        RandomListOfIntegers = [random.randint(Start, Stop) for iter in range(limit)]

        print(RandomListOfIntegers)

        # Process and format result from movie db api to list of 3-5 movies

        # DM the user                
        await message.author.send(f'You have **{counter}** messages')
        await message.author.send(f'{messages}')
        await message.author.send('https://m.media-amazon.com/images/M/MV5BYzg0NGM2NjAtNmIxOC00MDJmLTg5ZmYtYzM0MTE4NWE2NzlhXkEyXkFqcGdeQXVyMTA4NjE0NjEy._V1_SX300.jpg')

client.run(API_TOKEN)
