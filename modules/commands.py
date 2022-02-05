from discord.ext.commands import CommandNotFound
from modules.logger import logger
from discord.ext import commands
from modules.functions import *
from modules.seasons import *
from configs import config
import discord

bot = commands.Bot(command_prefix='/')
bot.remove_command('help')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        logger(ctx.message.content.strip("/"), ctx.message.author, False)


@bot.command()
async def randomframe(ctx):
    output = random_episode_name("all")
    convert_return = convert_episode(output)

    name = convert_return[0]
    random_time = convert_return[1]

    await ctx.send(f'Sending random frame. ({random_time}).')
    await ctx.send(file=discord.File(f'/tmp/{name}'))

    delete_image(name)
    logger("randomframe", ctx.message.author, True)


@bot.command()
async def randomfromseason(ctx, season="all"):
    if name_to_database(season) == 0 or season == "all":
        logger("randomfromseason", ctx.message.author, False)

        embed = discord.Embed(title="Valid seasons are", color=0x00e1ff)
        for i in config.database:
            embed.add_field(name=i[1], value=i[0], inline=True)

        embed.set_footer(text="Made by nacabaro#2138")
        await ctx.send(embed=embed)
    else:
        output = random_episode_name(season)
        convert_return = convert_episode(output)

        name = convert_return[0]
        random_time = convert_return[1]
        season_name = name_to_database(season)[0]

        await ctx.send(f'''Sending random frame from {season_name}. ({random_time}).''')
        await ctx.send(file=discord.File(f'/tmp/{name}'))
        delete_image(name)

        logger("randomfromseason", ctx.message.author, True)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="RandomDigimonPicture help.",
                          description="Useful commands for RandomDigimonPicture.", color=0x00e1ff)
    embed.add_field(name="/randomness",
                    value="Random frame from all the seasons.", inline=True)
    embed.add_field(name="/randomfromseason <seasons>",
                    value="Send random picture from a specified season.", inline=True)
    embed.add_field(name="/version",
                    value="Show bot version.", inline=True)
    embed.set_footer(
        text="Made by nacabaro#2138.")

    logger("help", ctx.message.author, True)

    await ctx.send(embed=embed)


@bot.command()
async def version(ctx):
    await ctx.send(config.version)
