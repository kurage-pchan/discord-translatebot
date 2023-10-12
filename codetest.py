import discord

now

Update discordbot.py
Token = "ここにトークンを入力"
2 minutes ago

Add files via upload

Intents = discord.Intents.default()
Intents.message_content = True

client = discord.Client(intents=Intents)

#起動時動作
@client.event
async def on_ready():
    print("起床しました")

#メッセージ受信時動作
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '/ohayou':
now

Update discordbot.py
        await message.channel.send("おはBot")
2 minutes ago

Add files via upload

    if message.content.startswith('おやすみ'):
        await message.channel.send('おやすみ！また明日！')
        await client.close()


now

Update discordbot.py
client.run(Token)
