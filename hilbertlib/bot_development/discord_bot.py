import discord
from discord.ext import commands

class DiscordBot:
    def __init__(self, token, command_prefix='/'):
        self.token = token
        self.command_prefix = command_prefix
        self.bot = commands.Bot(command_prefix=command_prefix, intents=discord.Intents.all())
        self.triggers = {}

        @self.bot.event
        async def on_ready():
            print(f'Logged in as {self.bot.user}')

        @self.bot.event
        async def on_message(message):
            if message.author == self.bot.user:
                return

            # Trigger system
            if message.content in self.triggers:
                await self.triggers[message.content](message)

            await self.bot.process_commands(message)

    def run(self):
        self.bot.run(self.token)

    # 🔊 Broadcast to specific channel
    async def broadcast_channel(self, message: str, channel_id: int):
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(message)

    # 📩 Broadcast to specific user
    async def broadcast_user(self, message: str, user_id: int):
        user = await self.bot.fetch_user(user_id)
        if user:
            await user.send(message)

    # 🔊 Broadcast to all text channels
    async def broadcast_all_channel(self, message: str):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                try:
                    await channel.send(message)
                except:
                    continue  # skip channels the bot can't send messages in

    # 📩 Broadcast to all users in servers
    async def broadcast_all_user(self, message: str):
        for guild in self.bot.guilds:
            for member in guild.members:
                try:
                    await member.send(message)
                except:
                    continue  # skip users that have DMs disabled

    # ➕ Add custom command
    def add_command(self, command: str, description: str, function):
        @self.bot.command(name=command, help=description)
        async def custom(ctx, *args):
            await function(ctx, *args)

    # 💬 Add trigger for exact message
    def add_trigger(self, chat: str, function):
        self.triggers[chat] = function