API_TOKEN = ''
OMDB_TOKEN = ''

import discord
import text2emotion as te
import random 
import requests

# Movie title arrays
surprise = ["The Suicide Squad", "Midsommar", "Shutter Island", "Gone Girl", "Get Out", "National Treasure", "North by Northwest", "The Prestige", "Jurassic Park", "The Little Things", "Prisoners", "Donnie Darko", "Sicario", "The Usual Suspects", "Tenet", "The Lord of the Rings: The Return of the King", "Inception", "Interstellar", "Seven Samurai", "The Lion King"]
fear =["Get Out", "Alien", "The Meg", "The Shining", "Split", "Saving Private Ryan", "The Pianist", "Casablanca", "Dara of Jasenovac", "Apocalypse Now", "A Quiet Place", "The Silence of the Lambs", "Joker", "Oldboy", "Psycho", "Rosemary's Baby", "Halloween", "Wonder Woman 1984", "The Suicide Squad", "28 Days Later"]
angry = ["The Matrix", "Star Wars: Episode V", "Gladiator", "Terminator 2", "Oldboy", "Aliens", "Warrior", "Die Hard", "Mission: Impossible", "Black Panther", "Snowpiercer", "Joker", "Pulp Fiction", "The Departed", "Goodfellas", "American Psycho", "Ocean’s Eleven", "Taxi Driver", "The Equalizer", "Scarface"]
sad = ["The Shawshank Redemption","The Godfather","The Dark Knight","Schindler's List","Fight Club","Shadow of a Doubt","The Night of the Hunter","The Third Man","Touch of Evil","Out of the Past","Judas and the Black Messiah","12 Angry Men","Forrest Gump","City of God","The Green Mile","Whiplash","American History X","Braveheart","Lawrence of Arabia","12 Years a Slave"]
happy = ["Coming to America","Parasite","Once Upon a Time... In Hollywood","Thor: Ragnarok","The Gentlemen","Deadpool","Back to the Future","Snatch","The Sting","Lock, Stock and Two Smoking Barrels","The Grand Budapest Hotel","The Greatest Showman","Aladdin","The Sound of Music","The Blues Brothers","The Goonies","The Princess Bride","Wall-E","Toy Story","Friday"]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Bot gets a message from channel
@client.event
async def on_message(message):
    user_id = message.author.id
    messages = ""

    if message.content.startswith('!moviemotion'):
         # Get user messages in the guild their in
        for chan in message.guild.text_channels:
            async for msg in chan.history(limit=100): # Last 100 messages in each channel 
                if msg.author.id == user_id:                                
                    # Save the messages to an array
                    messages = messages + " " + msg.content

        # Format messages
        messages = messages.replace('\n', '')
        messages = messages.replace('\t', '')
        messages = messages.strip('\n')  
        messages = messages.strip('\t')

        # Run text2emotion on messages 
        emotions = te.get_emotion(messages)

        # Result from text2emotion mapped to movie genres
        Keymax = max(emotions, key=emotions.get) 

        # Generate 3 random numbers
        RandomListOfIntegers = []

        for i in range(3):
            r = random.randint(0, 19)
            if r not in RandomListOfIntegers: RandomListOfIntegers.append(r)

        # Choose correct movie title array based on Keymax
        if Keymax == 'Happy':
            movie_array = happy
        if Keymax == 'Angry':
            movie_array = angry
        if Keymax == 'Surprise':
            movie_array = surprise
        if Keymax == 'Sad':
            movie_array = sad
        if Keymax == 'Fear':
            movie_array = fear

        # Assign 3 random movie titles
        movie1 = movie_array[RandomListOfIntegers[0]]
        movie2 = movie_array[RandomListOfIntegers[1]]
        movie3 = movie_array[RandomListOfIntegers[2]]
        
        # OMBD api call with selected movies
        movie1_url = 'https://www.omdbapi.com/?apikey=' + OMDB_TOKEN + '&t=' + movie1
        movie1_response = requests.get(movie1_url)
        movie1_json = movie1_response.json()

        movie2_url = 'https://www.omdbapi.com/?apikey=' + OMDB_TOKEN + '&t=' + movie2
        movie2_response = requests.get(movie2_url)
        movie2_json = movie2_response.json()
  
        movie3_url = 'https://www.omdbapi.com/?apikey=' + OMDB_TOKEN + '&t=' + movie3
        movie3_response = requests.get(movie3_url)
        movie3_json = movie3_response.json()
       
        # Process and format result from OMBD api
        newline = '\n'
        movie1_poster = movie1_json['Poster']
        movie2_poster = movie2_json['Poster']
        movie3_poster = movie3_json['Poster']

        movie1_year = movie1_json['Year'] 
        movie2_year = movie2_json['Year']
        movie3_year = movie3_json['Year']

        movie1_plot = movie1_json['Plot']
        movie2_plot = movie2_json['Plot']
        movie3_plot = movie3_json['Plot']

        movie1_id = movie1_json['imdbID']
        movie1_link = "https://www.imdb.com/title/" + movie1_id
        movie2_id = movie2_json['imdbID']
        movie2_link = "https://www.imdb.com/title/" + movie2_id
        movie3_id = movie3_json['imdbID']
        movie3_link = "https://www.imdb.com/title/" + movie3_id
        
        # Format embeds and DM the user                
        embed = discord.Embed(title="Hi there!", description="These are your top 3 movie recommendations based on your recent Discord messages. Enjoy!", color=discord.Color.blue())
        embed.set_author(name="moviemotion", icon_url="https://i.ibb.co/9yF0trY/logo.png")
        embed.add_field(name=f"1. {movie1}", value=f"({movie1_year}) {newline} {movie1_link}", inline=False)
        embed.set_image(url=f'{movie1_poster}')
        embed.set_footer(text=f"{movie1_plot}")

        await message.author.send(embed=embed)

        embed2 = discord.Embed(color=discord.Color.blue())
        embed2.add_field(name=f"2. {movie2}", value=f"({movie2_year}) {newline} {movie2_link}", inline=False)
        embed2.set_image(url=f'{movie2_poster}')
        embed2.set_footer(text=f"{movie2_plot}")

        await message.author.send(embed=embed2)

        embed3 = discord.Embed(color=discord.Color.blue())
        embed3.add_field(name=f"3. {movie3}", value=f"({movie3_year}) {newline} {movie3_link}", inline=False)
        embed3.set_image(url=f'{movie3_poster}')
        embed3.set_footer(text=f"{movie3_plot}")

        await message.author.send(embed=embed3)

client.run(API_TOKEN)
