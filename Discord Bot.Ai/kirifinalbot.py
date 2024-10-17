import discord
from discord.ext import commands
import os, random
from models import read_model
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def load_image(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            new_path_file = f"images/{file_name}"
            await attachment.save(new_path_file)
            await ctx.send(f"{read_model('keras_model.h5', 'labels.txt', file_name)}")
    else:
        ctx.send("Non ho trovato nessuna immagine")

bot.run("MTIwODA5MDMwNzIwNDQ4NTE5MQ.G2BFBP.E38y1ZwMrSEnPDuQ5PAPoWqpZiJFqXysI-oe08")
