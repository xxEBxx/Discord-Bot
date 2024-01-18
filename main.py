import discord
from discord.ext import commands
import requests
import json
import filetoken as tokenfile
import users
import asyncio
from nlpimport import Prediction
duration=10
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Function to fetch a random quote
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return quote

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    guild = bot.get_guild(tokenfile.guild_id)

    if guild:
        new_member_ids = {str(member.id) for member in guild.members} - set(users.server.player_data.keys())
        
        if new_member_ids:
            for member_id in new_member_ids:
                member = guild.get_member(int(member_id))
                
                if member:
                    player = users.User(int(member_id), member.display_name)
                    users.server.player_data[str(member_id)] = player.to_dict()
                    users.server.people[str(member_id)] = player.to_dict()
                    users.server.save_data()
                    print(f'{member.display_name} has been registered!')
    users.server.load_data()
@bot.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)

@bot.command()
async def spam(ctx):
    for i in range(10):  
        await ctx.send("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

@bot.command()
async def stop(ctx):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send('You don\'t have permission to stop the bot bro.')
        return 
    await ctx.send('Bot is saving changes.')
    users.server.save_data()
    await ctx.send('Bot is stopping.')
    await bot.close()

@bot.command()
async def members(ctx):
    print(users.server.player_data)

@bot.command()
#mieux de l'ecrire de cette forme : $unban member#1234
async def unban(ctx, *, member):
    if not ctx.author.guild_permissions.administrator :
        ctx.send(f'You don\'t have permission to unban a user')
        return 
    try:
        # Attempt to unban the member by username or ID
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            if member.lower() == user.name.lower() or member == str(user.id):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.name}#{user.discriminator} has been unbanned.')
                return
        await ctx.send('Member not found in the ban list.')
    except Exception as e:
        await ctx.send(f'An error occurred: {e}')

@bot.command()
async def unwarn(ctx, *, member: discord.Member):
    # Check if the author has administrator permissions
    if not ctx.author.guild_permissions.administrator:
        await ctx.send('You don\'t have permission to unwarn a user')
        return

    # Check if the member has any warnings
    member_id = str(member.id)
    if member_id not in users.server.people or users.server.people[member_id]["warnings"] == 0:
        await ctx.send(f'The member {member.mention} has no warnings')
        users.server.people[member_id]["behave"]=0
        users.server.player_data[member_id]["behave"]=0
        return

    try:
        # Reduce the number of warnings for the member
        users.server.people[member_id]["warnings"] -= 1
        users.server.player_data[member_id]["warnings"] -= 1
        users.server.save_data()

        # Send a success message with the updated number of warnings
        await ctx.send(f'The member {member.mention} has 1 less warning. Current warnings: {users.server.people[member_id]["warnings"]}')
    except Exception as e:
        await ctx.send(f'An error occurred: {e}')

@bot.command()
async def intiate_database(ctx):
    # Check if the command invoker has the necessary permissions
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("You do not have the necessary permissions to run this command.")
        return

    guild = ctx.guild
    members = guild.members  # Get a list of members in the guild

    for member in members:
        player_id = member.id
        player = users.User(player_id, member.display_name)
        
        # Assuming 'users.server' is your data management object
        users.server.player_data[str(player_id)] = player.to_dict()
        users.server.people[str(player_id)] = player.to_dict()
        
        # Assuming 'users.server.save_data()' saves the data
        users.server.save_data()
        
        print(f'{member.display_name} has been registered!')
        
        # Send a message to confirm registration
        await ctx.send(f"Member Name: {member.name}, Member ID: {member.id} has been registered!")

# Make sure to replace 'bot' with your actual bot instance when running this code.
def sectotime(seconds:int):
    if seconds<60:
        return f"{seconds} seconds"
    if seconds<3600:
        minutes=seconds//60
        return f"{minutes} minutes and {seconds-60*minutes} seconds"
    if seconds<86400:
        hours=seconds//3600
        seconds=seconds-hours*3600
        minutes=seconds//60
        seconds=seconds-minutes*60
        return f"{hours} hours ,{minutes} minutes ,{seconds-60*minutes} seconds"
    days=seconds//86400
    seconds-=days*86400
    hours=seconds//3600
    seconds=seconds-hours*3600
    minutes=seconds//60
    seconds=seconds-minutes*60
    return f"{days} days ,{hours} hours ,{minutes} minutes ,{seconds-60*minutes} seconds"

async def warn_user(message, author, bad_word, warnings):
    await message.channel.send(f"The user {author.mention} is warned for saying : {bad_word}. Current warnings: {warnings}")

# Function to ban the user
async def temp_ban_user(message, author, bad_word,duration):
    
    channel = discord.utils.get(message.guild.text_channels, name="warns-and-bans")
    await channel.send(f"The user {author.mention} is banned for {sectotime(duration)} for using the word: {bad_word}")
    await message.guild.ban(author)
    
    users.server.people[str(author.id)]["warnings"] = 0
    users.server.save_data()

    await asyncio.sleep(duration)

    await message.guild.unban(author)

async def send_message_to_channel_by_name(server, channel_name: str, message: str):
    # Find the target channel by name
    target_channel = discord.utils.get(server.text_channels, name=channel_name)

    if target_channel:
        # Send the message to the target channel
        await target_channel.send(message)
        print(f'Message sent to #{channel_name}: {message}')
    else:
        print(f'Channel #{channel_name} not found in this server.')

async def warn(message, author, bad_words_said, duration):
    channel=discord.utils.get(message.guild.text_channels, name="warns-and-bans")
    if users.server.player_data[str(author.id)]['warnings'] >= 2:
        # Ban the user after 3 warnings
        await temp_ban_user(message, author, bad_words_said[0], duration)
        await channel.send(f"{author.mention} is no longer banned from the server")
        users.server.people[str(author.id)]['warnings']=0
    else:
        # Warn the user and increment their warnings
        users.server.player_data[str(author.id)]['warnings'] += 1
        users.server.people[str(author.id)]['warnings'] += 1

        await warn_user(message, author, bad_words_said[0], users.server.player_data[str(author.id)]['warnings'])
# Event handler for when a message is received
@bot.event
async def on_message(message):
    author=message.author
    if author.bot:
        return
    content = message.content.lower()
    words = content.split()
    bad_words_said = [word for word in words if word in tokenfile.bad_words]
    channel=discord.utils.get(message.guild.text_channels, name="warns-and-bans")
    if bad_words_said:
        await warn(message, author, bad_words_said, duration)
    else : 
        if Prediction(content)=="disrespectful":
            if users.server.player_data[str(author.id)]['behave']==1:
                users.server.people[str(author.id)]['behave']=0
                users.server.player_data[str(author.id)]['behave']=0
                await warn(message, author, [content], duration)
            else:
                users.server.player_data[str(author.id)]['behave']=1
                await message.channel.send(f"The user {author.mention} is suspicious for bad behaviour :\"{content}\" current behavioural : 1")

    users.server.save_data()

    await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    player_id = member.id
    if str(player_id) in users.server.player_data:
        print(f'{member.display_name} is already registered!')
    elif str(player_id) in users.server.people:
        print(f'{member.display_name} came backkk!')
        users.server.player_data[str(player_id)] = users.server.people[str(player_id)]
    else:
        player = users.User(player_id, member.display_name)
        users.server.player_data[str(player_id)] = player.to_dict()
        users.server.people[str(player_id)] = player.to_dict()
        users.server.save_data()
        print(f'{member.display_name} has been registered!')

@bot.event
async def on_member_remove(member):
    player_id = member.id
    print(f'{users.server.people.get(str(player_id), {}).get("username", "Unknown user")} has left!')
    del users.server.player_data[str(player_id)]
    users.server.save_data()
    print("player_data",users.server.player_data)
    print("\npeople",users.server.people)

@bot.command()
async def list_members(ctx):
    print("Listing")
    await ctx.send("List of people in the server:")
    for id, data in users.server.player_data.items():
        if data.get("role") == "bot":
            continue
        await ctx.send(f"Username: {data['username']}, ID: {id}")
    
bot.run(tokenfile.token_code)
