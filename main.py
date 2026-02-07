import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random
import read_skins as sk

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

#agents intents
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
 
@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "shit" in message.content.lower():
        await message.channel.send(f"staaahp! {message.author.mention}")

    #makes it so the bot still does other things while processing this function
    await bot.process_commands(message)

@bot.command()
#ctx gets the situation where the bot was called, so if inside a thread or a random channel, the bot responds there
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def gamble(ctx):
    rolled_num = random.randrange(10)
    if rolled_num == 5:
        await ctx.send(f"Today's your lucky day, {ctx.author.mention}! Here, have a trillion bucks!")
    else:
        await ctx.send(f"Too bad, {ctx.author.mention}, got fucked..")

@bot.command()
async def skin_match(ctx, *, input_string):
    #separates string into champs
    champion_name_list = [name.strip() for name in input_string.split(',')]
    #converts all names to lowercase
    #for i in range(len(champion_name_list)):
    #    champion_name_list[i] = champion_name_list[i].lower()
    champions_skins = []
    for entry in champion_name_list:
        champions_skins.append(sk.get_champion_skins(entry))
    print(len(champions_skins))

    no_suitable_skinlines = 0
    suitable_skinlines = []

    for champion1_skin in champions_skins[0]:
        for champion2_skin in champions_skins[1]:
            if champion1_skin[1] == champion2_skin[1]:
                for champion3_skin in champions_skins[2]:
                    if champion2_skin[1] == champion3_skin[1]:
                        for champion4_skin in champions_skins[3]:
                            if champion3_skin[1] == champion4_skin[1]:
                                for champion5_skin in champions_skins[4]:
                                    if champion4_skin[1] == champion5_skin[1]:
                                        suitable_skinlines.append(champion1_skin[1])
                                        no_suitable_skinlines =+ 1
    if suitable_skinlines:
        suitable_skins = []
        for skinline in suitable_skinlines:
            suitable_skins.append(get_skin_names(skinline,champions_skins))
        await ctx.send(f"Yes! {no_suitable_skinlines} skinline(s) were found!")
        await ctx.send(f"Skinline: {suitable_skinlines}")
        for i in range(5):
            await ctx.send(f"{champion_name_list[i].capitalize()}: {suitable_skins[0][i]}")
        await ctx.send(f"GGs, have fun! {ctx.author.mention}")
    else:
        await ctx.send(f"Sorry {ctx.author.mention}, no skinline was found..")
            
@bot.command()
async def skin_ideas(ctx):
    all_universes = sk.get_all_universes
    for universe in all_universes:
        for skin in universe:
            if skin[1]

def get_skin_names(skinline,champion_list):
    skin_list = []
    for champion in champion_list:
        for skin in champion:
            if skin[1] == skinline:
                skin_list.append(skin[0])
    return skin_list


bot.run(token, log_handler=handler, log_level=logging.DEBUG)