import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # 

bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_CHANNEL_ID = 1434916863225233478  #

@bot.event
async def on_ready():
    print(f"ログイン成功: {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f"🐰 **ようこそ！** {member.mention} さんが参加しました！")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f"👋 **{member.name}** さんがサーバーを退出しました…")

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

