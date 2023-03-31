import os
import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
token = os.getenv('TOKEN')
weather_key = os.getenv('WEATHER_KEY')


@bot.event
async def on_ready():
    await bot.tree.sync()
    print("bot is ready")


# @bot.command(name='get-weather')
@bot.tree.command(name='get-weather', description="Get Weather information for your City!")
async def get_weather(interaction: discord.Interaction, city: str):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric')
    data = response.json()

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    embed = discord.Embed(title=f"Weather in {city}", color=0xff69b4)
    embed.add_field(name="Temperature", value=f":thermometer: {temperature}°C", inline=False)
    embed.add_field(name="Description", value=description, inline=False)

    # await ctx.send(embed=embed)
    await interaction.response.send_message(embed=embed)

bot.run(token)
