
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='//')

@bot.event
async def on_ready():
    print ("Pret a fonctionner !!")
    print ("Je démarre avec: " + bot.user.name)
    print ("Avec l'ID: " + bot.user.id)

@bot.command(pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command(pass_context=True)
async def AIDE(ctx):
    await bot.say("``` __ **Menu de Commandes:**__ ```")
    await bot.say(" - ")
    await bot.say("// devant chaque commandes")
    await bot.say("ping--> offre une réponse surprise du bot")
    await bot.say("info + 'joueur' --> Donne des informations sur le joueur")
    await bot.say("kick + 'joueur' --> Virer le joueur")
    await bot.say(" - ")
    await bot.say("``` __**Fin des commandes**__ ```")

    print ("L'utilisateur a utilisé 'help'.")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!! xSSS")
    print ("L'utilisateur a fait 'ping'. ")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("```Le nom de l'utilisateur est: {}```".format(user.name))
    await bot.say("```L'ID de l'utilisateur est: {}```".format(user.id))
    await bot.say("```Le statut de l'utilisateur est: {}```".format(user.status))
    await bot.say("```Le role de l'utilisateur est: {}```".format(user.top_role))
    await bot.say("```L'utilisateur à rejoint en: {}```".format(user.joined_at))
    print ("L'utilisateur a utilisé la commande 'info'.")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)
    print ("Un joueur a était viré")


bot.run("NDQ4MTgxNDAwNDU4NDkzOTcy.DeS-AA.aEaGUdn5WXKiKRhcTLhBd9m-bjk")