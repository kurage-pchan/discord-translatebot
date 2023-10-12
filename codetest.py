import discord

Token = "ここにトークンを入力"

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
        await message.channel.send("おはBot")
        
    if message.content.startswith('おやすみ'):
        await message.channel.send('おやすみ！また明日！')
        await client.close()

client.run(Token)
