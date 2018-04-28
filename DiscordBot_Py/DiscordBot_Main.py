# Дискорд Бот с подключенним к нейронный сеть от DialogFlow
import discord, apiai, json

DISCORD_BOT_TOKEN = "NDM4NzUwODczNTEwODcxMDYx.DcJNzA.0hb6FM6r1jjLk3HgKQqB7YIdht0"
DIALOGFLOW_CLIENT_ACCESS_TOKEN = "e6f61617821741a5953f12dcee6e9cc5"
BOT_PREFIX = "$"
client = discord.Client()

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

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    request = apiai.ApiAI(client_access_token=DIALOGFLOW_CLIENT_ACCESS_TOKEN).text_request()  #Токен API к Dialogflow
    request.lang = "ru" # На каком языке будет послан запрос
    request.session_id = "Jack_Vorobey_Bot" # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = message.content # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode("utf-8"))
    response = responseJson["result"]["fulfillment"]["speech"] # Разбираем JSON и вытаскиваем ответ
    
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        await client.send_message(message.channel, response)
    else:
        await client.send_message(message.channel, "Я Вас не совсем понял!")

    #if message.content.startswith(BOT_PREFIX+"hello"):
    #    msg = "Hello {0.author.mention}".format(message)
    #    await client.send_message(message.channel, msg)


client.run(DISCORD_BOT_TOKEN)
