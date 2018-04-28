import discord

client = discord.Client()
DISCORD_BOT_TOKEN = "NDM4NzUwODczNTEwODcxMDYx.DcJNzA.0hb6FM6r1jjLk3HgKQqB7YIdht0"

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        msg = "Hello {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

client.run(DISCORD_BOT_TOKEN)
