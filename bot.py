import discord
import requests
import json

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
        
        if message.content.startswith('hi'):
            await message.channel.send('Hello!')

        if message.content.startswith('$meme'):
            meme_url = get_meme()   # ✅ Call the function
            await message.channel.send(meme_url)  # ✅ Send the meme link

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('your token') #add your token here.