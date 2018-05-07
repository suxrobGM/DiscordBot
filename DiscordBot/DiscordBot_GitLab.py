import discord, gitlab

DISCORD_BOT_TOKEN = "DISCORD_BOT_TOKEN"
GITLAB_USER_TOKEN = "GITLAB_USER_TOKEN"
BOT_PREFIX = "$"

client = discord.Client()
git = gitlab.Gitlab(url="http://gitlab.ecrisis.su", private_token=GITLAB_USER_TOKEN, email="suxrobgm@gmail.com", password="qwe123")
git.auth()
print(git.version())
#EC_project = git.projects.starred()
#p_ars = EC_project.accessrequests.list()
#print(p_ars)


@client.event
async def on_ready():
    print("Bot online ")
    print("Username: %s" %client.user.name)
    print("User ID: %s" %client.user.id)
    print("------------")

@client.event
async def on_member_join(member):
    server = member.server
    fmt = "Welcome {0.mention} to {1.name}!"
    await client.send_message(server, fmt.format(member, server))
