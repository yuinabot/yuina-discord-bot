import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # 入退室通知に必須

bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_CHANNEL_ID = 123456789012345678  # ← チャンネルIDを自分のに変更

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

@bot.command()
async def omikuji(ctx):
    results = [
        "大吉 ✨",
        "中吉 🙂",
        "小吉 😊",
        "吉 😌",
        "末吉 😐",
        "凶 😨",
        "大凶 💀"
    ]
    result = random.choice(results)
    await ctx.send(f"🔮 今日の運勢：**{result}**")

TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(TOKEN)
