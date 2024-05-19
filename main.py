import discord
from discord.ext import commands

# Define the bot prefix
prefix = '!'

# Define the necessary intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot with the specified intents
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready!')

@bot.command()
async def globalwarming(ctx):
    await ctx.send("Global warming is a long-term increase in Earth's average surface temperature due to human activities such as burning fossil fuels and deforestation.")

@bot.command()
async def carbonfootprint(ctx):
    part1 = ("Transportation Cars, Trucks, etc:\n"
             "Air Pollution: Combustion engines emit pollutants like carbon monoxide, nitrogen oxides, and particulate matter, contributing to air pollution.\n"
             "Land Use: Roads and highways often require deforestation and habitat destruction during construction.\n"
             "Solution: Promote the use of electric vehicles (EVs), invest in public transportation infrastructure, encourage carpooling, and implement stricter emissions standards.")
    
    part2 = ("Aviation:\n"
             "Carbon Emissions: Airplanes emit greenhouse gases like carbon dioxide, which contribute to climate change.\n"
             "Noise Pollution: Aircraft noise disrupts wildlife habitats and human communities.\n"
             "Solution: Invest in research and development for more fuel-efficient aircraft, implement carbon offset programs, and improve air traffic management systems to reduce congestion and fuel consumption.")
    
    part3 = ("Maritime Transportation:\n"
             "Ballast Water Discharge: Ships often discharge ballast water containing invasive species, disrupting ecosystems.\n"
             "Oil Spills: Accidental oil spills from ships can have catastrophic effects on marine life and coastal ecosystems.\n"
             "Solution: Implement stricter regulations on ballast water management, enforce maritime safety standards, and invest in spill prevention and response technologies.")
    
    part4 = ("Rail Transportation:\n"
             "Habitat Fragmentation: Railway lines can fragment habitats, disrupt wildlife migration patterns, and contribute to species decline.\n"
             "Noise and Vibration: Trains produce noise and vibration, which can disturb wildlife and nearby communities.\n"
             "Solution: Implement wildlife crossings and habitat restoration projects, invest in quieter and more energy-efficient trains, and optimize rail networks to minimize environmental impact.")
    
    await ctx.send(part1)
    await ctx.send(part2)
    await ctx.send(part3)
    await ctx.send(part4)

@bot.command(name="carbonfootprint_measures")
async def carbonfootprint_measures(ctx):
    await ctx.send("Promoting Sustainable Alternatives: Encourage the use of public transportation, cycling, walking, and carpooling. Investing in Green Technologies: Support research and development of electric vehicles, biofuels, and renewable energy sources for transportation. Regulatory Measures: Enforce stricter emissions standards, implement carbon pricing mechanisms, and regulate land use to minimize habitat destruction. Public Awareness and Education: Educate the public about the environmental impacts of transportation and encourage eco-friendly travel behaviors. Infrastructure Improvements: Invest in infrastructure for alternative transportation modes, such as bike lanes, pedestrian pathways, and electric vehicle charging stations.")

# Run the bot
bot.run('TOKEN_GOES_HERE')


