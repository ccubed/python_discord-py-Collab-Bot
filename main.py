import discord
from discord.ext import commands

# For future use
# Do not modify unless you understand
# startup_extensions = []

# Make sure we have an overused and annoying prefix
# Add useless description
bot = commands.Bot(command_prefix="!", description="Hi! I'm a bot.")

# Obligatory Load Command that gives no feedback
@bot.command()
async def load(ctx, what : str):
    """Load a Module"""
    try:
        bot.load_extension(what)
    except ImportError as e:
        pass

# Obligatory Unload Command that gives no feedback
@bot.command()
async def unload(ctx, what : str):
    """Unload Modules"""
    bot.unload_extension(what)

# Everyone needs a command to disconnect their bot, let's make ours frustrating
@bot.command()
async def hidethepainharoldandkillyourself(ctx):
    """Kill the selfbot and potentially end harold's suffering"""
    await bot.logout()

# Obligatory status editing command
@bot.command()
async def status(ctx, what : str):
    """Set status"""
    await ctx.message.delete()
    if bot.is_ready():
        await bot.change_presence(game=discord.Game(name=what))

# Obligatory on ready, make sure this gives a super inane message
@bot.event
async def on_ready():
    print("Yo boi! We up in dis, fam!")

# Unnecessary namespace comparison for future use
# Definitely do not edit if unsure of purpose
if __name__ == "__main__":
    pass

    # Obligatory token inclusion
    # Is this a real token?
    # I don't know, who is going to actually try it out?
    bot.run("W10xv01289Gqw01tVas078510vASG07vb123tVa0sg701gv13t07va")
