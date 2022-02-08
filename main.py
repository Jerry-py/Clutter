import traceback
from pathlib import Path

import discord
from discord.ext import commands

import config
from utils import color, embed

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", help_command=None)

_modules_loaded, _modules_couldnt_load = "", ""
for file_path in Path("./modules").glob("**/*.py"):
    file_path = str(file_path).replace("/", ".")[:-3]
    file_name = file_path.split(".")[-1]
    try:
        bot.load_extension(file_path)
    except Exception:
        fail = str(traceback.format_exc()[:-1]).split("\n")
        fail = "\n   │".join(fail)
        length = len(f"Couldn't load {file_name}:") - 5
        that = "   ╭" + length * "─" + "╯"
        fail = f"{that}\n   │{fail}"
        _modules_couldnt_load += f"Couldn't load {file_name}:\n{fail}\n\n"
    else:
        _modules_loaded += f"   │{file_name}\n"


@bot.event
async def on_ready():
    print(color.green(f"\n\n\nLoaded:\n   ╭──╯\n{_modules_loaded}") + color.red(f"\n{_modules_couldnt_load}"))
    print(
        f"\nLogged in as:\n   ╭────────╯\n   │{bot.user.name}\n   │{bot.user.id}\n\nPycord version:\n   ╭──────────╯\n   │{discord.__version__}\n\nServers connected to:\n   ╭────────────────╯")
    for guild in bot.guilds:
        print(f"   │{guild.name}")


@bot.command(aliases=["rl"])
@commands.is_owner()
@commands.guild_only()
async def reload(ctx, module: str):
    await ctx.channel.trigger_typing()
    for path in Path("./modules").glob("**/*.py"):
        path = str(path).replace("/", ".")[:-3]
        name = path.split(".")[-1]
        if name != module:
            continue
        try:
            bot.reload_extension(path)
        except commands.ExtensionNotLoaded:
            try:
                bot.load_extension(path)
            except Exception:
                with open("./errorlogs/error.txt", mode="w") as file:
                    file.write(traceback.format_exc())
                with open("./errorlogs/error.txt", mode="rb") as file:
                    return await ctx.reply(embed=embed.error(ctx.guild.id, f"Couldn't reload {module}"),
                                           file=discord.File(file), mention_author=False)
        except Exception:
            with open("./errorlogs/error.txt", mode="w") as file:
                file.write(traceback.format_exc())
            with open("./errorlogs/error.txt", mode="rb") as file:
                return await ctx.reply(embed=embed.error(ctx.guild.id, f"Couldn't reload {module}"),
                                       file=discord.File(file), mention_author=False)
        else:
            return await ctx.reply(embed=embed.success(ctx.guild.id, f"Successfully reloaded {module}"),
                                   mention_author=False)
    await ctx.reply(embed=embed.error(ctx.guild.id, f"There is no such module named {module}"), mention_author=False)


@bot.command(aliases=["l"])
@commands.is_owner()
@commands.guild_only()
async def load(ctx, module: str):
    await ctx.channel.trigger_typing()
    for path in Path("./modules").glob("**/*.py"):
        path = str(path).replace("/", ".")[:-3]
        name = path.split(".")[-1]
        if name != module:
            continue
        try:
            bot.load_extension(path)
        except commands.ExtensionAlreadyLoaded:
            return await ctx.reply(embed=embed.error(ctx.guild.id, f"The module {module} is already loaded"),
                                   mention_author=False)
        except Exception:
            with open("./errorlogs/error.txt", mode="w") as file:
                file.write(traceback.format_exc())
            with open("./errorlogs/error.txt", mode="rb") as file:
                return await ctx.reply(embed=embed.error(ctx.guild.id, f"Couldn't load {module}"),
                                       file=discord.File(file), mention_author=False)
        else:
            return await ctx.reply(embed=embed.success(ctx.guild.id, f"Successfully loaded {module}"),
                                   mention_author=False)
    await ctx.reply(embed=embed.error(ctx.guild.id, f"There is no such module named {module}"), mention_author=False)


@bot.command(aliases=["ul"])
@commands.is_owner()
@commands.guild_only()
async def unload(ctx, module: str):
    await ctx.channel.trigger_typing()
    for path in Path("./modules").glob("**/*.py"):
        path = str(path).replace("/", ".")[:-3]
        name = path.split(".")[-1]
        if name != module:
            continue
        try:
            bot.unload_extension(path)
        except commands.ExtensionNotLoaded:
            return await ctx.reply(embed=embed.error(ctx.guild.id, f"The module {module} is already unloaded"),
                                   mention_author=False)
        except Exception:
            with open("./errorlogs/error.txt", mode="w") as file:
                file.write(traceback.format_exc())
            with open("./errorlogs/error.txt", mode="rb") as file:
                return await ctx.reply(embed=embed.error(ctx.guild.id, f"Couldn't unload {module}"),
                                       file=discord.File(file), mention_author=False)
        else:
            return await ctx.reply(embed=embed.success(ctx.guild.id, f"Successfully unloaded {module}"),
                                   mention_author=False)
    await ctx.reply(embed=embed.error(ctx.guild.id, f"There is no such module named {module}"), mention_author=False)


bot.run(config.bot_token)
