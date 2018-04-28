# Обычный дискорд бот
import discord
from discord.ext import commands

DISCORD_BOT_TOKEN = "NDM4NzUwODczNTEwODcxMDYx.DcJNzA.0hb6FM6r1jjLk3HgKQqB7YIdht0"
bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")

@bot.command()
async def add(a: int, b: int):
    await bot.say(a+b)

@bot.command()
async def multiply(a: int, b: int):
    await bot.say(a*b)

@bot.command()
async def greet():
    await bot.say(":smiley: :wave: Hello, there!")

@bot.command()
async def cat():
    await bot.say("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info():
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="<YOUR-USERNAME>")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value="{len(bot.get_all_channels()}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await bot.say(embed=embed)

bot.remove_command("help")

@bot.command()
async def help():
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await bot.say(embed=embed)

bot.run(DISCORD_BOT_TOKEN)
