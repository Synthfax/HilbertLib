from hilbertlib.bot_development.discord_bot import DiscordBot

bot = DiscordBot("BOT_TOKEN_HERE", command_prefix="!")

# Example command
async def say_hello(ctx, *args):
    await ctx.send("Hello!")

# Example trigger
async def greet_back(msg):
    await msg.channel.send("Hi there!")

bot.add_command("hello", "Say hello", say_hello)
bot.add_trigger("hi bot", greet_back)

@bot.bot.event
async def on_ready():
    print(f"Logged in as {bot.bot.user}")

    # await async functions properly
    try:
        await bot.broadcast_user("Hi", 123456789101112)
    except Exception as e:
        print(f"Failed to send to user: {e}")

    try:
        await bot.broadcast_all_channel("LMAO")
    except Exception as e:
        print(f"Failed to send to channels: {e}")

bot.run()
