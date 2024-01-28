import discord
from discord.ext import commands
from module import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def yes(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            file_name = i.filename
            file_url = i.url
            await i.save(f"./{i.filename}")
            await ctx.send (get_class(model_path='keras_model.h5', labels_path="labels.txt", image_path=f"./{i.filename}"))
    else:
        while True:
            await ctx.send("@everyone Вы забили загрузить картинку ._.")

bot.run()
