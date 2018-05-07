# Дискорд Бот с подключенним к нейронный сеть от DialogFlow
import discord, apiai, json

DISCORD_BOT_TOKEN = "DISCORD_BOT_TOKEN"
DIALOGFLOW_CLIENT_ACCESS_TOKEN = "DIALOGFLOW_CLIENT_ACCESS_TOKEN"
BOT_PREFIX = "$"
isBotActive = True
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

    global isBotActive
    if message.content.startswith(BOT_PREFIX+"start"):
        isBotActive = True
        return
    elif message.content.startswith(BOT_PREFIX+"stop"):
        isBotActive = False

    request = apiai.ApiAI(client_access_token=DIALOGFLOW_CLIENT_ACCESS_TOKEN).text_request()  #Токен API к Dialogflow
    request.lang = "ru" # На каком языке будет послан запрос
    request.session_id = "Jack_Vorobey_Bot" # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = message.content # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode("utf-8"))
    response = responseJson["result"]["fulfillment"]["speech"] # Разбираем JSON и вытаскиваем ответ
    
    #print(isBotActive)
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response and isBotActive:
        await client.send_message(message.channel, response)
    elif not response and isBotActive:
        await client.send_message(message.channel, "Я Вас не совсем понял!")

    #if message.content.startswith(BOT_PREFIX+"hello"):
    #    msg = "Hello {0.author.mention}".format(message)
    #    await client.send_message(message.channel, msg)


client.run(DISCORD_BOT_TOKEN)
