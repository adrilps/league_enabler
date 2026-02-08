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
bot.remove_command('help')
 
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
async def match(ctx, *, input_string):
    champion_name_list = [name.strip() for name in input_string.split(',')]
    
    first_champion = champion_name_list[0]
    first_champion_skins = sk.get_champion_skins(first_champion)
    
    if not first_champion_skins:
        await ctx.send(f"Champion {first_champion} not found.")
        return

    random.shuffle(first_champion_skins)

    for index in first_champion_skins:
        universe = sk.get_by_universe(index[1])
        if not universe:
            continue
            
        skins_dict = {champ.lower(): skin_name for champ, skin_name in universe}
        
        i = 0
        for champ in champion_name_list:
            if skins_dict.get(champ.lower()) is None:
                break
            else:
                i += 1

        if i == len(champion_name_list):
            await ctx.send(f"{ctx.author.mention}, I found a matching universe: {index[1]}")
            for champ in champion_name_list:
                await ctx.send(f"{champ.capitalize()} has the skin {skins_dict.get(champ.lower())}.")
            return #
    await ctx.send(f"{ctx.author.mention}, I think there are no matching skinlines :(")
    return

@bot.command()
async def help(ctx):
    help_message=(
        f"heya, {ctx.author.mention} here are the available commands: \n\n" \
        "!help: this!\n" \
        "!gamble: test your luck!\n" \
        "!idea: give me a number and i'll give you that number of random champs that share a skinline\n" \
        "!match: give me champs and i'll let you know if they share a skinline!\n\n" \
        "developed by yours truly, <@226542884935958538>"
    )
    await ctx.send(help_message)
        

            
@bot.command()
async def ideas(ctx, input_string):
    #get a random universe
    try:
        number_of_champions = int(input_string)
    except ValueError:
        await ctx.send(f"Please enter a valid number, {ctx.author.mention}.")
        return
    print(1)
    all_universes = sk.get_all_universes()

    available_universes = [
        (name, skins) for name, skins in all_universes.items() 
        if len(skins) >= number_of_champions
    ]
    
    print(available_universes)

    if not available_universes:
        await ctx.send("Nenhum universo encontrado com essa quantidade de skins.")
        return

    print(2)
    skinline_name, skins_list = random.choice(available_universes)
    print(3)

    random_skins = random.sample(skins_list, number_of_champions)
    #removes last skin appended to random_skins, so not to pick the same skin twice
    print(4)
    await ctx.send("The selected skins were:")
    for i in range(len(random_skins)):
        await ctx.send(f"{random_skins[i]}")


@bot.command()
async def get_skin_names(skinline,champion_list):
    skin_list = []
    for champion in champion_list:
        for skin in champion:
            if skin[1] == skinline:
                skin_list.append(skin[0])
    return skin_list


bot.run(token, log_handler=handler, log_level=logging.DEBUG)